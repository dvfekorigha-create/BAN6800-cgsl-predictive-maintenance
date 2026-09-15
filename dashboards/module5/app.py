
import json
import warnings
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

warnings.filterwarnings("ignore")

BASE = Path(__file__).resolve().parent
MODEL_PATH = BASE / "model" / "best_model.joblib"
META_PATH = BASE / "model" / "model_metadata.json"
DATA = BASE / "data"

st.set_page_config(
    page_title="CGSL Predictive Maintenance Dashboard",
    page_icon="⚙️",
    layout="wide",
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@st.cache_data
def load_csv(name):
    return pd.read_csv(DATA / name)

model = load_model()
meta = load_json(META_PATH)
sample = load_json(DATA / "sample_request.json")["features"]
shap_df = load_csv("shap_global_importance.csv")
local_df = load_csv("local_shap_explanation.csv")
cf_df = load_csv("counterfactual_explanation.csv")
risk_df = load_csv("operational_robustness_results.csv")

st.title("⚙️ CGSL AI-Enabled Predictive Maintenance")
st.caption("Stakeholder decision-support dashboard | BAN6800 Module 5")

with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Select view",
        [
            "Business Overview",
            "Prediction",
            "What Drives Predictions",
            "What-If Analysis",
            "Fairness & Ethics",
            "Model Information",
        ],
    )
    st.divider()
    st.info(
        "This proof-of-concept supports human-supervised maintenance "
        "decision-making. It does not autonomously control equipment."
    )

# ---------- Business Overview ----------
if page == "Business Overview":
    st.subheader("Business Overview")
    st.write(
        "This dashboard translates the Module 4 predictive model into "
        "business-facing information for exploring equipment failure risk."
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Model", "Gradient Boosting")
    c2.metric("Test Accuracy", f"{meta['accuracy']*100:.2f}%")
    c3.metric("Recall", f"{meta['recall']*100:.2f}%")
    c4.metric("ROC-AUC", f"{meta['roc_auc']*100:.2f}%")

    st.markdown("### What the model is designed to do")
    st.write(
        "Estimate the probability that an equipment observation belongs "
        "to the failure class so that maintenance teams can investigate "
        "higher-risk cases using appropriate engineering and operational context."
    )

    st.markdown("### Model performance at the Module 4 default threshold")
    perf = pd.DataFrame({
        "Metric": ["Accuracy", "Precision", "Recall", "F1-score", "ROC-AUC"],
        "Value": [
            meta["accuracy"], meta["precision"], meta["recall"],
            meta["f1_score"], meta["roc_auc"]
        ],
    })
    fig = px.bar(perf, x="Metric", y="Value", range_y=[0, 1],
                 text=perf["Value"].map(lambda x: f"{x:.2f}"))
    fig.update_traces(textposition="outside")
    fig.update_yaxes(tickformat=".0%")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Plain-language explanation")
    st.info(
        "The model looks for patterns across 334 transformed equipment-related "
        "variables. It produces a failure probability. A probability at or above "
        "the current 0.50 analytical threshold is classified as 'failure risk'. "
        "The output is decision support and requires human review."
    )

# ---------- Prediction ----------
elif page == "Prediction":
    st.subheader("Prediction")
    st.write(
        "Enter or adjust selected model-ready variables. The remaining variables "
        "retain the Module 4 sample-request values."
    )

    top_features = shap_df.head(8)["Feature"].tolist()
    values = list(sample)

    cols = st.columns(2)
    for i, feature in enumerate(top_features):
        idx = int(feature.split("_")[1])
        current = float(values[idx])
        # Wide but bounded numeric input; engineering interpretation is intentionally not inferred.
        with cols[i % 2]:
            values[idx] = st.number_input(
                feature,
                value=current,
                key=f"pred_{feature}",
                help="Transformed model-ready variable; no physical sensor meaning is inferred."
            )

    X = np.asarray(values, dtype=float).reshape(1, -1)
    proba = model.predict_proba(X)[0]
    failure_p = float(proba[1])
    threshold = float(meta["default_classification_threshold"])
    prediction = "Failure risk" if failure_p >= threshold else "No failure risk"

    st.divider()
    a, b, c = st.columns(3)
    a.metric("Failure probability", f"{failure_p*100:.2f}%")
    b.metric("No-failure probability", f"{proba[0]*100:.2f}%")
    c.metric("Classification", prediction)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=failure_p * 100,
        title={"text": "Estimated failure probability"},
        gauge={"axis": {"range": [0, 100]}, "threshold": {"line": {"width": 4}, "value": threshold*100}}
    ))
    st.plotly_chart(fig, use_container_width=True)

    if failure_p >= threshold:
        st.warning(
            "The current model threshold classifies this observation as failure risk. "
            "This is an analytical alert for human review, not an autonomous maintenance instruction."
        )
    else:
        st.success(
            "The current model threshold classifies this observation below the failure-risk threshold. "
            "Normal engineering controls and monitoring still apply."
        )

# ---------- Explainability ----------
elif page == "What Drives Predictions":
    st.subheader("What Drives Predictions?")
    st.write(
        "SHAP explains which transformed variables contributed most strongly to "
        "the model's predictions. Positive/negative direction should be interpreted "
        "as model behavior, not as proof of physical causation."
    )

    show_n = st.slider("Number of leading variables", 5, min(15, len(shap_df)), 8)
    d = shap_df.head(show_n).sort_values("Mean_Absolute_SHAP")
    fig = px.bar(
        d, x="Mean_Absolute_SHAP", y="Feature", orientation="h",
        title="Global feature importance (mean absolute SHAP)"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Plain-language interpretation")
    st.info(
        "The largest bars are the variables that, on average, had the greatest "
        "influence on model output. The dataset uses transformed/anonymized variables, "
        "so the dashboard does not assign unsupported physical meanings to Feature_0, "
        "Feature_70, and other feature IDs."
    )

    st.markdown("### Module 4 local explanation example")
    local_show = local_df.head(10).copy()
    local_show["Direction"] = np.where(
        local_show["SHAP_Value"] >= 0,
        "Increased model output",
        "Decreased model output",
    )
    st.dataframe(local_show, use_container_width=True, hide_index=True)

# ---------- What-if ----------
elif page == "What-If Analysis":
    st.subheader("What-If Analysis")
    st.write(
        "The Module 4 counterfactual analysis illustrates how changing selected "
        "transformed inputs can alter the model's predicted probability. These are "
        "model explanations, not engineering instructions or recommended set-points."
    )

    display = cf_df.copy()
    display["Probability (%)"] = display["Updated_Failure_Probability"] * 100
    fig = px.bar(
        display.head(12).sort_values("Probability (%)"),
        x="Probability (%)", y="Feature", orientation="h",
        hover_data=["Original_Value", "Counterfactual_Value"],
        title="Counterfactual scenario probabilities from Module 4"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Example scenario")
    selected = st.selectbox("Select a transformed variable", cf_df["Feature"].tolist())
    row = cf_df[cf_df["Feature"] == selected].iloc[0]
    x1, x2, x3 = st.columns(3)
    x1.metric("Original value", f"{row['Original_Value']:,.2f}")
    x2.metric("Counterfactual value", f"{row['Counterfactual_Value']:,.2f}")
    x3.metric("Updated failure probability", f"{row['Updated_Failure_Probability']*100:.2f}%")

    st.warning(
        "Counterfactual changes show model sensitivity. They must not be interpreted "
        "as instructions to physically change equipment without engineering validation."
    )

# ---------- Fairness ----------
elif page == "Fairness & Ethics":
    st.subheader("Fairness & Ethical Compliance")
    st.write(
        "The fairness analysis follows the Module 4 report. The public proxy dataset "
        "does not contain defensible demographic/protected attributes."
    )

    f1, f2, f3 = st.columns(3)
    f1.metric("Demographic parity", "Not assessable")
    f2.metric("Equalized odds", "Not assessable")
    f3.metric("Disparate impact", "Not assessable")

    st.info(
        "No protected groups were fabricated or synthetically assigned. Numerical "
        "demographic fairness values would be misleading without a valid protected-group attribute."
    )

    st.markdown("### Operational risk-segment robustness")
    st.caption("These are operational prediction bands, NOT demographic or protected groups.")
    st.dataframe(risk_df, use_container_width=True, hide_index=True)

    st.markdown("### Transparency statement")
    st.write(
        "The model estimates failure risk from patterns in the available transformed "
        "features. It cannot establish physical causation, replace engineering judgment, "
        "guarantee future performance, or establish demographic fairness from this proxy dataset."
    )

    st.markdown("### Human oversight")
    st.write(
        "Outputs require human review. Before production deployment, CGSL would need "
        "a governed production dataset, prospective validation, monitoring, documented "
        "fairness testing where appropriate, and compliance review."
    )

# ---------- Model info ----------
else:
    st.subheader("Model Information")
    left, right = st.columns(2)
    with left:
        st.markdown("**Project**")
        st.write(meta["project"])
        st.markdown("**Organization**")
        st.write(meta["organization"])
        st.markdown("**Model**")
        st.write(meta["model_type"])
        st.markdown("**Dataset**")
        st.write(meta["dataset"])
        st.markdown("**Model-ready features**")
        st.write(meta["number_of_features"])
    with right:
        st.markdown("**Training observations**")
        st.write(f"{meta['training_observations']:,}")
        st.markdown("**Testing observations**")
        st.write(f"{meta['testing_observations']:,}")
        st.markdown("**Default threshold**")
        st.write(meta["default_classification_threshold"])
        st.markdown("**Peak analytical F1 threshold**")
        st.write(meta["analytical_threshold_sensitivity_peak_f1"])
        st.markdown("**Autonomous control**")
        st.write("No")

    st.divider()
    st.markdown("### Model limitations")
    limitations = [
        "The public UCI dataset is a proxy rather than CGSL's governed production population.",
        "Feature IDs are transformed/anonymized; unsupported physical meanings are not assigned.",
        "Fairness metrics requiring protected attributes are not assessable on the proxy.",
        "The model supports prediction, not causal diagnosis or autonomous equipment control.",
        "The default threshold is analytical; production threshold selection requires business and engineering validation.",
        "Prospective monitoring and drift/performance review are required before production use.",
    ]
    for item in limitations:
        st.markdown(f"- {item}")

st.divider()
st.caption(
    "BAN6800 Module 5 | CGSL Predictive Maintenance | Human-supervised decision support | "
    "Proof-of-concept dashboard"
)
