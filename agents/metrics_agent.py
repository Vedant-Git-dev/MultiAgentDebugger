class MetricsAgent:

    def analyze(self, m):

        findings = []

        if m["precision"] < 0.6:
            findings.append({
                "issue": "Low Precision",
                "severity": round(1 - m["precision"], 2),
            })

        if m["recall"] < 0.6:
            findings.append({
                "issue": "Low Recall",
                "severity": round(1 - m["recall"], 2),
            })

        gap = m["train_accuracy"] - m["test_accuracy"]

        if gap > 0.1:
            findings.append({
                "issue": "Overfitting",
                "severity": round(gap, 2),
            })

        return findings
