class FeatureAgent:

    def analyze(self, f):

        fi = f["feature_importance"]

        total = sum(fi.values())
        top_feature = max(fi, key=fi.get)
        dominance = fi[top_feature] / total

        return {
            "top_feature": top_feature,
            "dominance_score": round(dominance, 2),
            "warning": dominance > 0.6,
            "evidence": f"Top Feature Importance = {fi[top_feature]}"
        }
