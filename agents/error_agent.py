class ErrorAgent:

    def analyze(self, e):

        fp = e["false_positives"]
        fn = e["false_negatives"]
        total = fp + fn

        if total == 0:
            return {"issue": "No errors detected"}

        fp_rate = fp / total
        fn_rate = fn / total
        
        if fp_rate > fn_rate:
            dominant = "False Positives"
            severity = fp_rate

        elif fn_rate == fp_rate:
            dominant = "Balanced Errors"
            severity = fp_rate  
        else:
            dominant = "False Negatives"
            severity = fn_rate

        return {
            "dominant_error": dominant,
            "severity": round(severity, 2),
        }
