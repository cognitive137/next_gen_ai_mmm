import streamlit as st
import numpy as np
import pandas as pd
from data.synthesizer import generate_synthetic_data
from optimization.allocator import optimize_budget
from models.transformations import apply_hill_saturation

st.set_page_config(page_title="Next-Gen AI MMM Framework", layout="wide")
st.title("📊 Next-Gen Open Source MMM Framework for Conversational AI Ads")
st.caption("IEOR Mathematical Allocation Engine Mapping Platform Cannibalization Drivers")

# Initialize Tabs
tab1, tab2 = st.tabs(["🚀 Live Optimization Engine", "📄 Strategic Case Study Blueprint"])

with tab1:
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

with tab2:
    st.header("Strategic Case Study: Monetizing the Conversational AI Paradigm Shift")
    
    st.subheader("1. The Core Business Crisis")
    st.markdown("""
    **The Problem:** For over two decades, digital marketing relied entirely on a simple transaction: a user searched for something, clicked a sponsored blue link, a tracking cookie fired, and Google proved its return on investment (ROI). Today, this high-margin ecosystem faces an existential threat from two fronts:
    1. **Privacy Infrastructure Erosion:** Updates like Apple's App Tracking Transparency (ATT) and regulatory laws (GDPR, CCPA) have permanently blinded click-level user tracking.
    2. **On-Page Session Cannibalization:** The rise of generative layers like Google's AI Overviews shifts user behavior from *navigational clicking* to *on-page consumption*. If an AI cleanly answers a user's question upfront, they do not click traditional sponsored links. This internal platform cannibalization drops core ad revenues.
    """)
    
    st.subheader("2. Why This is Worth Solving")
    st.markdown("""
    Firms cannot simply turn off AI Overviews without ceding the entire internet search engine market to emerging competitors like Perplexity or OpenAI. Therefore, the trillion-dollar challenge is finding the mathematical inflection point where a brand can safely scale conversational AI ad exposures *without* completely draining their high-margin legacy search traffic performance. 
    
    Because individual cookie tracking is gone, **Marketing Mix Modeling (MMM)** uses top-line aggregated time-series data to cleanly capture this cross-elasticity friction via macro-econometric modeling.
    """)
    
    st.subheader("3. Historical Precedents of Strategic Cannibalization")
    st.markdown("""
    Great technology history proves that companies who survive a structural break choose to aggressively lead their own disruption rather than desperately trying to protect a dying cash cow:
    * **Apple vs. The iPod:** Apple intentionally designed the iPhone to natively include complete music-player capabilities, willingly killing their dominant standalone hardware product (the iPod) to migrate users into a vastly more valuable, sticky, smartphone-plus-app ecosystem.
    * **Netflix vs. Physical DVDs:** In 2007, Netflix weaponized the massive cash flows from their core high-margin physical DVD subscription base to bankroll a low-margin, high-infrastructure infrastructure shift into video streaming, establishing global category dominance.
    * **Adobe vs. Perpetual Licensing:** Adobe boldly killed their $1,000+ upfront physical software packages to enforce a cheaper monthly cloud subscription framework, enduring massive short-term revenue hits from Wall Street to secure incredibly predictable, compounding recurring user equity over the long-term.
    """)
