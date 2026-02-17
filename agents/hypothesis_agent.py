from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))


class HypothesisAgent:

    def analyze(self, results, class_ratio):
        prompt = f"""
You are a strict machine learning audit system.

Your job is to diagnose model problems ONLY using provided evidence.

You must obey these rules:

RULES:
- Use ONLY the evidence provided.
- Do NOT invent causes.
- If evidence is insufficient, say "Insufficient evidence".
- Do NOT speculate.
- Prefer conservative conclusions.
- Distinguish between proven vs suspected issues.
- Compare model accuracy to majority class ratio. {max(class_ratio):.2f}
- If accuracy is within 0.02 of the highest class ratio, mark "Model not learning signal" as proven issue.


ANALYSIS DATA:
Metrics: {results["metrics"]}
Class Distribution: {results["data"]}
Errors: {results["errors"]}
Feature Info: {results["features"]}

OUTPUT FORMAT (STRICT JSON ONLY):

{{
  "proven_issues": [],
  "suspected_issues": [],
  "analysis": {{
      "model_learning_status": "",
      "error_pattern": "",
      "overfitting": "",
      "feature_dominance": ""
  }},
  "recommended_actions": [],
  "risk_level": "",
  "explanation": ""
}}
If a proven issue has a known statistical cause, infer that cause and suggest fixes.
Otherwise leave recommendations empty.
Sort issues by severity + impact level in priority section..

NO TEXT OUTSIDE JSON. and give concise, evidence-based analysis paragraphs in the "analysis" section. 
provide concise, paragraphs in the "explaination" section with combined insights from all sections.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return json.loads(response.choices[0].message.content.split("```")[1].strip())
