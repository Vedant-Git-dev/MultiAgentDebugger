from agents.metrics_agent import MetricsAgent
from agents.data_agent import DataAgent
from agents.error_agent import ErrorAgent
from agents.feature_agent import FeatureAgent
from agents.hypothesis_agent import HypothesisAgent
from priority_engine import PriorityEngine


class Orchestrator:

    def __init__(self):
        self.metrics = MetricsAgent()
        self.data = DataAgent()
        self.error = ErrorAgent()
        self.feature = FeatureAgent()
        self.hypothesis = HypothesisAgent()
        self.proiority_engine = PriorityEngine()

    def run(self, inputs):

        results = {}

        results["metrics"] = self.metrics.analyze(inputs["metrics"])
        results["data"] = self.data.analyze(inputs["data"])
        results["errors"] = self.error.analyze(inputs["errors"])
        results["features"] = self.feature.analyze(inputs["features"])
        results["diagnosis"] = self.hypothesis.analyze(results, inputs["data"]["class_ratio"])
        results["diagnosis"]["priority_order"] = self.proiority_engine.rank(results["diagnosis"]["proven_issues"], results["diagnosis"]["suspected_issues"])

        return results
