class PriorityEngine:

    IMPACT = {
        "Model not learning signal": 10,
        "Severe class imbalance": 9,
        "Overfitting": 7,
        "Underfitting": 7,
        "Low Recall": 6,
        "Low Precision": 5,
        "Data leakage": 10
    }

    def rank(self, proven, suspected):

        ranked = []

        for issue in proven:
            score = self.IMPACT.get(issue, 1) * 2
            ranked.append((issue, score))

        for issue in suspected:
            score = self.IMPACT.get(issue, 1)
            ranked.append((issue, score))

        ranked.sort(key=lambda x: x[1], reverse=True)
        

        return [i[0] for i in ranked]
