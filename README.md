# Multi Agent Model Debugger

## Overview

This project is an intelligent analysis system designed to evaluate classification models trained on numerical tabular datasets. Instead of only reporting performance metrics, it investigates why a model behaves the way it does and produces a structured diagnosis that explains strengths, weaknesses, and possible causes of failure.

The goal is to make model evaluation meaningful by turning raw numbers into clear insights.


## What This Project Does

The system takes a tabular dataset, trains a classification model, evaluates its performance, and then runs a group of specialized analysis agents. Each agent studies a different aspect of the model. Their findings are combined into a final diagnostic report that explains what is happening inside the model and what should be checked next.

It does not just show results. It explains them.


## Agents and Their Roles

**Metrics Agent**
Analyzes performance metrics such as accuracy, precision, and recall. It detects whether scores indicate weak learning, imbalance effects, or unreliable predictions.

**Data Agent**
Examines class distribution and dataset structure. It identifies imbalance or suspicious distributions that could affect model behavior.

**Error Agent**
Studies prediction mistakes and compares false positives and false negatives. This helps determine whether the model is biased, confused, or generally weak.

**Feature Agent**
Evaluates feature importance and detects whether a single feature dominates predictions or whether all features contribute weakly.

**Reasoning Agent**
Combines outputs from all other agents and generates a structured diagnosis. It determines proven issues, suspected issues, explanations, and suggested next steps based on evidence.

**Priority Engine**
Ranks detected issues by importance so users know what should be fixed first instead of guessing where to start.


## Key Features

* Built specifically for classification tasks on structured tabular data
* Automatically trains a baseline model for analysis
* Detects issues such as low performance, imbalance, overfitting, and weak signal learning
* Separates confirmed problems from suspected ones
* Produces structured machine readable diagnostic reports
* Prioritizes issues by impact
* Explains reasoning instead of giving vague suggestions


## Why This Project Matters

Many machine learning projects stop after printing evaluation scores. Those numbers alone do not explain why a model succeeds or fails. This system acts like an automated reviewer that interprets results using evidence from data, predictions, and model behavior.

It is intentionally cautious. When there is not enough evidence to support a conclusion, it states that clearly instead of making assumptions. This makes its analysis more reliable and realistic.


## Example Insight

If a model performs nearly the same as predicting the majority class, the system detects that it is not learning meaningful patterns and flags it as a high priority issue.


## Use Cases

This project can help:

* Students understand model failure patterns
* Developers debug classification pipelines
* Practitioners validate model reliability
* Anyone who wants explanations rather than raw metrics


## Tech Stack

Python
Scikit learn
Streamlit
Rule based analysis agents with reasoning layer


## What I Learned Building This

Building this system required thinking beyond training models. It involved designing logic that evaluates evidence, avoids unsupported conclusions, and prioritizes real problems instead of surface level metrics. It helped me understand how real machine learning systems are analyzed, not just how they are built.


## Future Scope

Future versions may include support for regression tasks, dataset quality diagnostics, and automated improvement recommendations.


## Final Note

This project is not just a model trainer. It is a model understanding system that explains what the model is doing and why.