# Transaction Outbox Pattern: Ensuring Atomicity Between DB Updates and Blockchain Submission

## Overview

The **Transaction Outbox Pattern** is a design pattern that ensures atomicity and reliable message delivery between a database and an external system (in this case, blockchain submission). It solves the critical problem of maintaining data consistency when updates must be coordinated between a local database and a remote distributed ledger.

---

## Core Concept

Instead of directly publishing events or submitting transactions to blockchain after updating your database, the pattern uses a two-phase approach:

### Phase 1: Atomic Database Write

- Update your main business tables (e.g., `orders`, `customers`)
- Simultaneously insert an "outbox" record into an `outbox` table in the **same database transaction**
- Either both succeed together or both fail together (guaranteed atomicity)

### Phase 2: Asynchronous External Submission

- A separate background worker/poller reads unprocessed records from the outbox table
- Submits the event or transaction to the blockchain
- Once confirmed on-chain, marks the outbox record as processed
- Handles retries and failures independently

---

## Why It Matters for Your Blockchain Adapter

### The Problem It Solves

Without the outbox pattern, you face serious consistency risks:

| Scenario                                                       | Risk                                    |
| -------------------------------------------------------------- | --------------------------------------- |
| DB update succeeds but blockchain submission fails             | Data inconsistency between systems      |
| Blockchain submission succeeds but DB crashes before recording | Duplicate blockchain submissions        |
| Network partition between systems                              | Lost messages and orphaned transactions |
| Timeout during external API call                               | Unclear whether operation succeeded     |

### The Solution: Visual Flow

```
┌──────────────────────────────────────────┐
│ Database Transaction (Atomic - All or Nothing)  │
│                                          │
│ ├─ UPDATE orders SET status='pending'   │
│ ├─ UPDATE inventory SET qty=qty-1       │
│ └─ INSERT INTO outbox (event_data)      │ ← Stored in same transaction
│                                          │
└──────────────────────────────────────────┘
             ↓
    ✓ Transaction Commits
    (Both DB changes + outbox entry succeed or both fail)
             ↓
┌──────────────────────────────────────────┐
│ Background Outbox Poller (Independent)   │
│                                          │
│ 1. SELECT * FROM outbox                 │
│    WHERE processed_at IS NULL           │
│                                          │
│ 2. FOR EACH unprocessed record:         │
│    - Extract blockchain payload         │
│    - Submit transaction to blockchain   │
│    - Wait for confirmation (tx hash)    │
│                                          │
│ 3. UPDATE outbox SET                    │
│    processed_at=NOW(),                  │
│    blockchain_tx_hash='0x...'           │
│                                          │
└──────────────────────────────────────────┘
```

---

## Implementation Strategy

### Database Schema

```sql
-- Main application table (example: orders)
CREATE TABLE orders (
  id UUID PRIMARY KEY,
  customer_id UUID NOT NULL,
  amount DECIMAL(18, 2) NOT NULL,
  status VARCHAR(50) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- The Outbox Table
CREATE TABLE outbox (
  id BIGSERIAL PRIMARY KEY,
  aggregate_id UUID NOT NULL,              -- Reference to order, payment, etc.
  aggregate_type VARCHAR(255) NOT NULL,    -- Type of entity (e.g., 'Order', 'Payment')
  event_type VARCHAR(255) NOT NULL,        -- Type of event (e.g., 'ORDER_CREATED', 'PAYMENT_SUBMITTED')
  payload JSONB NOT NULL,                  -- The full event/transaction data
  created_at TIMESTAMP DEFAULT NOW(),
  processed_at TIMESTAMP,                  -- NULL until successfully processed
  blockchain_tx_hash VARCHAR(255),         -- Once mined: the blockchain transaction hash
  blockchain_network VARCHAR(50),          -- Which network (mainnet, testnet, etc.)
  retry_count INT DEFAULT 0,
  max_retries INT DEFAULT 5,
  last_error TEXT,
  next_retry_at TIMESTAMP
);

-- Index for efficient polling
CREATE INDEX idx_outbox_unprocessed
  ON outbox(created_at)
  WHERE processed_at IS NULL;

-- Index for replay/debugging
CREATE INDEX idx_outbox_aggregate
  ON outbox(aggregate_type, aggregate_id);
```

### Write Path: Database Update + Outbox Entry

**Pseudocode for Order Submission Flow:**

```
BEGIN TRANSACTION

  TRY:
    1. UPDATE orders
       SET status = 'blockchain_pending', updated_at = NOW()
       WHERE id = :order_id

    2. INSERT INTO outbox (
         aggregate_id,
         aggregate_type,
         event_type,
         payload,
         blockchain_network
       ) VALUES (
         :order_id,
         'Order',
         'ORDER_SUBMITTED_TO_BLOCKCHAIN',
         {
           'orderId': order_id,
           'amount': order.amount,
           'customer': order.customer_id,
           'productIds': [product1, product2],
           'timestamp': NOW(),
           'dataHash': keccak256(order_data)  -- For blockchain verification
         },
         'ethereum-mainnet'
       )

    COMMIT  -- Both succeed atomically

  CATCH:
    ROLLBACK  -- Both fail atomically
    THROW exception
```

### Read Path: Asynchronous Outbox Processor

**Pseudocode for background worker:**

```
EVERY 5 seconds (configurable):

  SELECT * FROM outbox
  WHERE processed_at IS NULL
    AND (next_retry_at IS NULL OR next_retry_at <= NOW())
  ORDER BY created_at ASC
  LIMIT 10  -- Process in batches

  FOR EACH outbox_record:
    TRY:
      -- Extract the blockchain payload
      blockchain_tx = outbox_record.payload

      -- Sign the transaction (using Vault/HSM)
      signed_tx = signWithPrivateKey(blockchain_tx)

      -- Submit to blockchain
      tx_hash = blockchain.submitTransaction(signed_tx)

      -- Wait for confirmation (configurable: 1-15 blocks)
      receipt = blockchain.waitForConfirmation(tx_hash, confirmations=6)

      IF receipt.status == SUCCESS:
        -- Mark as processed
        UPDATE outbox
        SET processed_at = NOW(),
            blockchain_tx_hash = tx_hash,
            blockchain_network = receipt.network,
            retry_count = 0
        WHERE id = outbox_record.id

        -- Optional: Update main table status
        UPDATE orders
        SET status = 'confirmed_on_blockchain',
            blockchain_tx = tx_hash
        WHERE id = outbox_record.aggregate_id

        LOG INFO: "Transaction confirmed: ${tx_hash}"

      ELSE:
        -- On-chain failure (e.g., out of gas, reverted)
        HANDLE FAILURE with exponential backoff

    CATCH blockchain_timeout_error:
      -- Network issue, retry with exponential backoff
      CALCULATE next_retry = NOW() + exponential_backoff(retry_count)
      UPDATE outbox
      SET retry_count = retry_count + 1,
          next_retry_at = next_retry,
          last_error = 'Blockchain timeout'
      WHERE id = outbox_record.id

      IF retry_count >= max_retries:
        -- Move to DLQ for manual intervention
        INSERT INTO dead_letter_queue SELECT * FROM outbox WHERE id = ...
        LOG ERROR: "Max retries exceeded for outbox record"
```

---

## Key Benefits for Blockchain Integration

| Benefit                    | Why It Matters                                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------------------------------- |
| ✅ **Guaranteed Delivery** | No lost transactions between DB and blockchain—every event eventually reaches the ledger                   |
| ✅ **Idempotency**         | Can safely retry failed submissions without creating duplicates; use blockchain tx hash as idempotency key |
| ✅ **Decoupling**          | Database updates don't depend on blockchain network latency or availability                                |
| ✅ **Observability**       | Outbox table provides complete audit trail of what was submitted, when, and what the result was            |
| ✅ **Disaster Recovery**   | Can replay failed submissions by querying the outbox; great for disaster recovery and debugging            |
| ✅ **Scalability**         | DB writes are fast (synchronous + local); blockchain submissions happen asynchronously                     |
| ✅ **Compliance**          | Complete immutable record for audits and regulatory requirements                                           |

---

## Implementation Considerations

### Polling Strategies

#### 1. Time-Based Polling (Simple)

```
Run every 5-10 seconds
Pros: Simple, works for low-throughput
Cons: Latency overhead, CPU busy-wait
```

#### 2. Change Data Capture (CDC) - Advanced

```
Use Kafka/Debezium to detect new outbox inserts
Pros: Near real-time delivery, efficient
Cons: More complex infrastructure
```

#### 3. Hybrid Approach (Recommended)

```
Use CDC for immediate processing
Fall back to time-based polling for resilience
```

### Idempotency Keys

Always include idempotency mechanisms:

```json
{
  "idempotency_key": "order-123-v1",
  "timestamp": "2026-01-28T10:30:00Z",
  "nonce": 12345,
  "previous_tx_hash": null
}
```

This prevents duplicate submissions if retries occur.

### Error Handling Categories

| Error Type                                            | Handling Strategy                                        |
| ----------------------------------------------------- | -------------------------------------------------------- |
| **Transient (Network timeout, temporary congestion)** | Exponential backoff retry                                |
| **Permanent (Invalid signature, bad data format)**    | Send to DLQ, alert operator                              |
| **Gas-related (Insufficient funds, out of gas)**      | Manual intervention required                             |
| **Nonce mismatch**                                    | Detect previous successful submission, mark as processed |

---

## Monitoring & Observability

### Key Metrics to Track

```
-- Outbox Health
1. COUNT(outbox WHERE processed_at IS NULL)
   → Alert if > threshold (backlog building up)

2. AVG(processed_at - created_at)
   → Measure end-to-end latency

3. COUNT(outbox WHERE retry_count > 0) / total
   → Retry rate (indicator of blockchain network issues)

4. SUM(case when last_error IS NOT NULL)
   → Failed submissions (requires manual intervention)
```

### Log Entry Example

```json
{
  "timestamp": "2026-01-28T10:35:20Z",
  "trace_id": "abc-123",
  "event": "outbox_processed",
  "outbox_id": 567,
  "aggregate_id": "order-789",
  "event_type": "ORDER_SUBMITTED",
  "blockchain_network": "ethereum-mainnet",
  "blockchain_tx_hash": "0x1234...abcd",
  "processing_duration_ms": 2500,
  "retry_count": 0,
  "status": "success"
}
```

---

## Comparison with Alternatives

| Approach           | Pros                                | Cons                                  |
| ------------------ | ----------------------------------- | ------------------------------------- |
| **Outbox Pattern** | Guaranteed delivery, simple, proven | Requires polling/CDC infrastructure   |
| **Saga Pattern**   | Good for distributed transactions   | Complex compensation logic            |
| **Event Sourcing** | Complete audit trail                | Significant redesign required         |
| **Dual-writes**    | Simple conceptually                 | ❌ UNSAFE: race conditions guaranteed |

---

## Best Practices

1. **Never do dual-writes** (DB + blockchain in separate transactions)
   - Always use outbox pattern for reliability

2. **Make outbox entries immutable**
   - Once inserted, never delete; only mark as processed
   - Keeps full audit trail

3. **Implement idempotency keys**
   - Handle retries without creating duplicates on-chain

4. **Use exponential backoff**
   - Don't hammer blockchain during network issues
   - Example: 1s → 2s → 4s → 8s → 16s → stop

5. **Monitor outbox table growth**
   - Archive processed records periodically for performance
   - Create partitions by month for easier maintenance

6. **Set max retry limits**
   - Move unprocessable records to Dead Letter Queue (DLQ)
   - Alert operations for manual intervention

7. **Test chaos scenarios**
   - Simulate blockchain unavailability
   - Verify outbox handles it gracefully
   - Validate no data loss occurs

---

## Conclusion

The Transaction Outbox Pattern is **essential for your blockchain adapter** to guarantee data consistency and reliable delivery between legacy financial systems and decentralized ledgers. It decouples database transactions from blockchain operations, allowing each system to work at its own pace while guaranteeing no messages are lost.

This pattern is widely used in fintech, payment systems, and other mission-critical applications where data integrity cannot be compromised.
