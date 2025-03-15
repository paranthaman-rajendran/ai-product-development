import json

# Load Playwright test results
with open("test-results.json", "r") as file:
    results = json.load(file)

total_tests = len(results['suites'])
passed = sum(1 for test in results['suites'] if test['status'] == "passed")
failed = sum(1 for test in results['suites'] if test['status'] == "failed")

metrics = {
    "total_tests": total_tests,
    "passed": passed,
    "failed": failed,
    "pass_rate": round((passed / total_tests) * 100, 2) if total_tests > 0 else 0,
}

# Save metrics
with open("test-metrics.json", "w") as file:
    json.dump(metrics, file, indent=4)

print("✅ Test metrics generated successfully!")
