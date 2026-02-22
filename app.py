import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import numpy as np

from orchestrator import Orchestrator

st.title("Multi Agent Model Debugger")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:

    df = pd.read_csv(file)

    st.write("Dataset Preview")
    st.dataframe(df.head())

    target = st.selectbox("Select Target Column", df.columns)


    if st.button("Run Analysis"):

        X = df.drop(columns=[target])
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = Pipeline([
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression())
        ])

        model.fit(X_train, y_train)

        preds = model.predict(X_test)

        metrics = {
                "accuracy": accuracy_score(y_test, preds),
                "precision": precision_score(y_test, preds, average="weighted"),
                "recall": recall_score(y_test, preds, average="weighted"),
                "train_accuracy": model.score(X_train, y_train),
                "test_accuracy": model.score(X_test, y_test)
                }
        
        cm = confusion_matrix(y_test, preds)

        fp = cm.sum(axis=0) - cm.diagonal()
        fn = cm.sum(axis=1) - cm.diagonal()

        errors = {
            "false_positives": int(fp.sum()),
            "false_negatives": int(fn.sum())
        }
        
        class_counts = y.value_counts(normalize=True).tolist()

        data_info = {
            "class_ratio": class_counts
        }

        values = np.abs(model.named_steps["classifier"].coef_[0])
        feature_importance = dict(zip(X.columns, values / np.sum(values)))

        features = {
            "feature_importance": feature_importance
        }

        inputs = {
            "metrics": metrics,
            "data": data_info,
            "errors": errors,
            "features": features
        }

        orch = Orchestrator()
        report = orch.run(inputs)

        st.subheader("Diagnosis Report")
        st.write(report["diagnosis"]["explanation"])
