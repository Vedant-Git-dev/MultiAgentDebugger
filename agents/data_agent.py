class DataAgent:

    def analyze(self, d):

        ratio = d["class_ratio"]

        imbalance_score = max(ratio)
        imbalance_detected = imbalance_score > 0.7

        return {
            "imbalance_detected": imbalance_detected,
            "severity": round(imbalance_score, 2),
        }
