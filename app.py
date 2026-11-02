import streamlit as st
import numpy as np
import pandas as pd
from data.synthesizer import generate_synthetic_data
from optimization.allocator import optimize_budget
from models.transformations import apply_hill_saturation

st.set_page_config(page_title="Next-Gen AI MMM Framework", layout="wide")
st.title("📊 Next-Gen Open Source MMM Framework for Conversational AI Ads")
st.caption("IEOR Mathematical Allocation Engine Mapping Platform Cannibalization Drivers")

st.sidebar.header("Model Parameters")
total_budget = st.sidebar.slider("Total Available Daily Capital ($)", 500, 5000, 2500, step=100)
gamma = st.sidebar.slider("Stochastic Cannibalization Modifier (γ)", 0.0, 0.50, 0.25, step=0.01)

st.sidebar.subheader("Channel Response Weights")
beta_trad = st.sidebar.slider("Traditional Link Weight (β1)", 500, 2000, 1200, step=50)
beta_ai = st.sidebar.slider("AI Chat Citation Weight (β2)", 100, 1000, 500, step=50)

st.sidebar.subheader("Saturation Curves")
alpha = st.sidebar.slider("Hill Curve Alpha (α)", 0.5, 3.0, 1.2, step=0.1)
kappa = st.sidebar.slider("Half-Max Parameter (K)", 100, 2000, 500, step=50)

df = generate_synthetic_data()
opt_s, opt_a, max_rev = optimize_budget(total_budget, beta_trad, beta_ai, gamma, alpha, kappa)

eff_trad_pct = apply_hill_saturation(opt_s, alpha, kappa) * 100
eff_ai_pct = apply_hill_saturation(opt_a, alpha, kappa) * 100

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label="Optimal Traditional Link Spend", value=f"${opt_s:,.2f}")
    st.caption(f"Capacity Utilization Reached: **{eff_trad_pct:.1f}%**")
with c2:
    st.metric(label="Optimal AI Overview Spend", value=f"${opt_a:,.2f}")
    st.caption(f"Capacity Utilization Reached: **{eff_ai_pct:.1f}%**")
with c3:
    st.metric(label="Maximized Revenue Outcome", value=f"${max_rev:,.2f}")
    st.caption(f"Implied Portfolio ROAS: **{(max_rev/total_budget):.2f}x**")

st.markdown("---")
st.subheader("Historical Timeline Model Verification Matrix")
st.line_chart(df.set_index('date')[['revenue', 'traditional_search_spend', 'ai_overview_spend']])
