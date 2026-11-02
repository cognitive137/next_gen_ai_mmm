import streamlit as st
import numpy as np
import pandas as pd
from data.synthesizer import generate_synthetic_data
from optimization.allocator import optimize_budget
from models.transformations import apply_hill_saturation

st.set_page_config(page_title="Next-Gen AI MMM Framework", layout="wide")

# ==============================================================================
# CUSTOM VISUAL NAVIGATION
# ==============================================================================
st.sidebar.markdown("# 🧭 Application Navigation")
app_mode = st.sidebar.radio(
    "Select Interface View Workspace:",
    ["🚀 Live Optimization Engine", "📄 Strategic Whitepaper & Case Study"],
    index=0
)
st.sidebar.markdown("---")

# Execute Data Generation Matrix Natively
df = generate_synthetic_data()

# ==============================================================================
# WORKSPACE WORKFLOW 1: LIVE OPTIMIZATION ENGINE
# ==============================================================================
if app_mode == "🚀 Live Optimization Engine":
    st.title("📊 Next-Gen Open Source MMM Framework for Conversational AI Ads")
    
    st.markdown("""
    ### Executive Overview
    For decades, digital advertising relied on an unwritten rule: a user searches, clicks a sponsored link, and a conversion is tracked. Today, **Google's AI Overviews and AI Mode are transforming user behavior from clicking links to consuming direct on-page answers.** 

    When users get answers upfront from an AI summary, they stop clicking traditional sponsored blue links. This causes a major problem: **the platform's new feature is cannibalizing its own high-margin ad revenue.** This open-source framework uses advanced optimization theory (SLSQP) and Marketing Mix Modeling (MMM) to locate the exact portfolio sweet spot that maximizes returns under cannibalization vectors.
    """)
    st.markdown("---")

    # User-Friendly Sidebar Calibration Controls
    st.sidebar.header("💼 Budget & Platform Controls")
    total_budget = st.sidebar.slider("Total Daily Ad Budget ($)", 500, 5000, 2500, step=100)
    gamma = st.sidebar.slider("AI Ads Cannibalization Rate (How aggressively AI answers steal your link traffic)", 0.0, 0.50, 0.25, step=0.01)

    st.sidebar.subheader("📈 Max Revenue Potential per Channel")
    beta_trad = st.sidebar.slider("Traditional Blue Links (Max Revenue Power)", 500, 2000, 1200, step=50)
    beta_ai = st.sidebar.slider("AI Overview Citations (Max Revenue Power)", 100, 1000, 500, step=50)

    st.sidebar.subheader("🎯 Diminishing Returns Configuration")
    alpha = st.sidebar.slider("Diminishing Returns Speed (How fast adding more budget flatlines performance)", 0.5, 3.0, 1.2, step=0.1)
    kappa = st.sidebar.slider("Channel Saturation Point (Budget level where ad efficiency drops by 50%)", 100, 2000, 500, step=50)

    # Compute Optimization Algorithm Matrix
    opt_s, opt_a, max_rev = optimize_budget(total_budget, beta_trad, beta_ai, gamma, alpha, kappa)

    # Compute Capacity Saturation Variables
    eff_trad_pct = apply_hill_saturation(opt_s, alpha, kappa) * 100
    eff_ai_pct = apply_hill_saturation(opt_a, alpha, kappa) * 100

    # Layout Optimized Metrics Grid
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="Optimal Traditional Link Spend", value=f"${opt_s:,.2f}")
        st.caption(f"Channel Effectiveness (Capacity Used): **{eff_trad_pct:.1f}%**")
    with c2:
        st.metric(label="Optimal AI Overview Spend", value=f"${opt_a:,.2f}")
        st.caption(f"Channel Effectiveness (Capacity Used): **{eff_ai_pct:.1f}%**")
    with c3:
        st.metric(label="Maximized Total Projected Revenue", value=f"${max_rev:,.2f}")
        st.caption(f"Implied Portfolio Return (ROAS): **{(max_rev/total_budget):.2f}x**")

    st.markdown("---")
    st.subheader("Historical 3-Year Model Validation Timeline")
    st.caption("Notice the structural break at Day 700 when AI Overviews are introduced, causing traditional search revenues to decay while AI spend climbs.")
    
    # Generate interactive line chart from generated data
    st.line_chart(df.set_index('date')[['revenue', 'traditional_search_spend', 'ai_overview_spend']])

# ==============================================================================
# WORKSPACE WORKFLOW 2: STRATEGIC WHITEPAPER & CASE STUDY
# ==============================================================================
else:
    st.title("📄 Strategic Whitepaper: Monetizing the Conversational AI Shift")
    st.caption("Author: Columbia IEOR Graduate Framework Integration Strategy")
    st.markdown("---")
    
    st.header("Executive Summary")
    st.markdown("""
    The transition of digital surfaces toward frontier generative AI models has broken traditional click-through performance marketing frameworks. As documented in public market shifts, search ad growth systematically slows down when users shift toward zero-click environments. 
    This paper introduces the macro-econometric and optimization logic behind the `Conv-MMM` project, detailing exactly what structural risk we are solving, how non-linear curves isolate marginal decay, and the ultimate evolutionary pivot of ad monetization.
    """)
    
    st.subheader("1. What Exactly Are We Solving?")
    st.markdown("""
    We are solving the **Strategic Cannibalization Dilemma of Zero-Click Intent**. 
    
    For two decades, advertising inventory was transactional and linear: a user typed a query, clicked a link, and paid a set Cost-Per-Click (CPC). Modern conversational engines (like Google AI Overviews or ChatGPT search) compress this timeline by synthesizing multi-source research into a single, comprehensive, fluid summary text box directly on the native screen surface. 
    
    Because the user consumes the solution without leaving the portal, traditional blue-link inventories face structural traffic decay. If a company continues to blindly throw money at traditional search, they run into massive, unseen overhead and flatlining conversions. This framework calculates how to identify that structural break and optimally pivot capital distribution to protect macro returns.
    """)

    st.subheader("2. Deep Technical Breakdown of the Applied Mathematics")
    st.markdown("""
    To decouple overlapping platform channel metrics without individual tracking cookies, this framework models budget allocation as a **Constrained Non-Linear Optimization Challenge** rooted in two continuous econometric curves:
    
    #### A. The Adstock Transformation (Memory Carryover Mechanics)
    Advertising exposure possesses a lingering memory effect that decays geometrically. We calculate the *Effective Exposure Time Tensor* using an Infinite Impulse Response (IIR) filter:
    
    $$Adstock(x_t) = x_t + \theta \cdot Adstock(x_{t-1})$$
    
    Where $\theta$ represents the memory retention parameter tracking consumer attention stickiness across operational cycles.
    
    #### B. The Hill Function Curve (Diminishing Marginal Efficiency)
    Marketing channels do not scale indefinitely; they reach a capacity wall. We map effective spend vectors through an asymmetric, non-linear Hill saturation function to extract precise **Channel Effectiveness Parameters (Capacity Used)**:
    
    $$Hill(x) = \frac{x^\alpha}{x^\alpha + K^\alpha}$$
    
    Where $K$ represents the scale threshold defining half-maximal saturation (efficiency drops 50%), and $\alpha$ dictates the speed and steepness at which the return rate flatlines.
    
    #### C. The Global Portfolio Solver (SLSQP Grid)
    Our objective function introduces a **Stochastic Cannibalization Modifier ($\gamma$)**, which forces the optimizer to treat the efficiency of legacy search links as a function of AI chat display intensity. We compute the global maximum using Sequential Least Squares Programming (SLSQP):
    
    $$\max_{S, A} \quad \text{Revenue} = \beta_1 \cdot Hill(S_t) \cdot \left[1.0 - \gamma \cdot Hill(A_t)\right] + \beta_2 \cdot Hill(A_t)$$
    $$\text{Subject to the Boundary Wall:} \quad S_t + A_t \le \text{Total Budget Allocation (B)}$$
    """)

    # Inline Structural Visual Representation Table
    st.subheader("3. Historical Precedents of Successful Strategic Disruption")
    st.markdown("Firms that survive platform paradigm changes choose to weaponize their new disruption rather than defending legacy cash cows:")
    
    st.table(pd.DataFrame({
        "Company": ["Netflix", "Apple", "Adobe", "Google Ads Team"],
        "Dying Cash Cow Inventory": ["High-margin physical DVD shipping", "Dominant iPod hardware lines", "$1,000+ Upfront software suites", "High-monetization Search Links (CPC)"],
        "Disruptive Vehicle Asset": ["Digital video streaming access", "Premium iPhone infrastructure", "Continuous Monthly SaaS subscriptions", "AI Overview Citations & Agents"],
        "Strategic Tactical Fix": ["Absorbed short-term overhead, scaled volume globally.", "Pivoted unit loss into premium high-tier ecosystem margins.", "Traded immediate upfront cash for recurring lifetime value.", "Injecting conversational native ads & monetization triggers."]
    }))

    st.subheader("4. Conclusion: Moving from $\$0.50$ Cost-Per-Click to $3-5\%$ Transaction Commissions")
    st.markdown("""
    The transition toward Conversational Search and Autonomous AI Shopping Agents marks the death of the legacy **Cost-Per-Click (CPC)** monetization framework. When bots or AI systems execute the mundane parts of product search on behalf of humans, charging a merchant 50 cents for an arbitrary link impression becomes irrelevant.
    
    **The Strategic Evolution:** Google and major search engines must pivot from charging for *intent traffic generation* to charging for **direct transaction fulfillment (Cost-Per-Acquisition / CPA)**. 

    Instead of collecting small fractional click fees, the new model transforms the platform into an end-to-end transaction hub. When an AI summary interface directly handles flight bookings, grocery ordering, or service scheduling natively inside the conversation interface, the platform takes an integrated 3% to 5% commission cut of the actual verified purchase total.
By scaling transaction cut monetization, the platform converts what was a low-margin text summary into an incredibly high-value, friction-free commerce machine. This shift dramatically elevates customer lifetime value metrics and generates much higher revenue yields than legacy web page blue links could ever support.
""")
