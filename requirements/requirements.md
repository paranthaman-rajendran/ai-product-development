# Loan Application Portal - Functional Requirements

## 1. Loan Application Submission

- Users must fill in their personal details, loan amount, and tenure.
- The form should validate required fields before submission.
- Successful submission should show a confirmation message.

## 2. Credit Score Check

- System should fetch and display the user's credit score.
- Applications with a credit score below 600 must be automatically rejected.
- Users with rejected applications should receive a clear rejection message explaining the reason.
- Credit score checks should be performed before proceeding with loan processing.
- System should maintain a record of rejected applications for compliance purposes.

## 3. Interest Rate Calculation

- Interest rate should be calculated based on loan amount and tenure.
- Salaried and self-employed users should have different interest rates.

## 4. Approval and Disbursement

- Approved loans should trigger an email confirmation.
- Rejected applications should display a rejection reason.
