import streamlit as st
import numpy as np
import pandas as pd
from data.synthesizer import generate_synthetic_data
from optimization.allocator import optimize_budget
from models.transformations import apply_hill_saturation

st.set_page_config(page_title="Next-Gen AI MMM Framework", layout="wide")

# ==============================================================================
# APPLICATION NAVIGATION SURFACES
# ==============================================================================
st.sidebar.markdown("# 🧭 Application Navigation")
app_mode = st.sidebar.radio(
    "Select Interface View Workspace:",
    ["🚀 Live Optimization Engine", "📄 Strategic Whitepaper & Case Study"],
    index=0
)
st.sidebar.markdown("---")

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

    st.sidebar.header("💼 Budget & Platform Controls")
    total_budget = st.sidebar.slider("Total Daily Ad Budget ($)", 500, 5000, 2500, step=100)
    gamma = st.sidebar.slider("AI Ads Cannibalization Rate (How aggressively AI answers steal your link traffic)", 0.0, 0.50, 0.25, step=0.01)

    st.sidebar.subheader("📈 Max Revenue Potential per Channel")
    beta_trad = st.sidebar.slider("Traditional Blue Links (Max Revenue Power)", 500, 2000, 1200, step=50)
    beta_ai = st.sidebar.slider("AI Overview Citations (Max Revenue Power)", 100, 1000, 500, step=50)

    st.sidebar.subheader("🎯 Diminishing Returns Configuration")
    alpha = st.sidebar.slider("Diminishing Returns Speed (How fast adding more budget flatlines performance)", 0.5, 3.0, 1.2, step=0.1)
    kappa = st.sidebar.slider("Channel Saturation Point (Budget level where ad efficiency drops by 50%)", 100, 2000, 500, step=50)

    opt_s, opt_a, max_rev = optimize_budget(total_budget, beta_trad, beta_ai, gamma, alpha, kappa)

    eff_trad_pct = apply_hill_saturation(opt_s, alpha, kappa) * 100
    eff_ai_pct = apply_hill_saturation(opt_a, alpha, kappa) * 100

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
    st.line_chart(df.set_index('date')[['revenue', 'traditional_search_spend', 'ai_overview_spend']])

# ==============================================================================
# WORKSPACE WORKFLOW 2: STRATEGIC WHITEPAPER & CASE STUDY
# ==============================================================================
else:
    st.title("📄 Strategic Whitepaper: Monetizing the Conversational AI Shift")
    st.caption("Author: Sana Habeeb | Columbia IEOR Framework Integration Strategy")
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
    #### The Strategic Objective of the Mathematics
    Before diving into individual adjustments, it is vital to establish what we are using the mathematics for. Because privacy frameworks have permanently hidden individual click-level user cookies, we cannot track human actions line-by-line. Instead, **we are using macro-econometric time-series data to treat corporate marketing budgets like an investment portfolio optimization asset.** 
    
    We use advanced calculus and statistical transformations to build an artificial sandbox. This sandbox isolates how ad dollars slowly build memory momentum, identifies the exact moment a channel becomes over-saturated, and mathematically punishes the legacy search channel based on how aggressively the new AI channel is expanding. By translating corporate ad spend into smooth, continuous curves, we can use numerical optimization to find the exact portfolio allocation split that maximizes revenue without wasting capital.
    
    #### A. The Adstock Transformation (Quantifying Consumer Memory Momentum)
    We use this formula because marketing investments do not evaporate overnight. An ad seen today triggers a residual psychological impact that lingers in a consumer's head and decays slowly over time. The Adstock algorithm calculates this rolling friction by transforming raw daily marketing dollar spend into a metric called *effective exposure spend*. This allows the model to know exactly how much historical memory momentum a brand has built up in the market at any given second.
    
    #### B. The Hill Function Curve (Pinpointing the Diminishing Efficiency Wall)
    We use this curve because marketing channels do not scale in a straight line forever; they hit physical capacity limits. Pumping infinite budget into an ad interface eventually reaches a point of flatlining marginal utility where an extra dollar yields zero extra sales. The Hill function creates a non-linear saturation curve that maps effective spend to a precise *Capacity Utilization Percentage*. This metrics tells business leaders exactly when they are approaching a saturation wall and when to stop over-spending on an ad format.
    
    #### C. The Global Portfolio Solver (The Sequential Least Squares Gradient Engine)
    We use this optimization engine to solve the final capital distribution problem. The framework builds a custom structural equation where the revenue potential of traditional search links is dynamically multiplied by an active *Stochastic Cannibalization Modifier*. As your AI Overview exposures scale up, this parameter mathematically erodes and discounts the value of traditional clicks. 
    
    Because the resulting formula is highly non-linear and bound by real-world constraints (e.g., your combined spend cannot exceed your daily corporate budget, and you cannot spend negative money), we deploy the Sequential Least Squares Programming (SLSQP) algorithm. The engine maps the slope of the revenue curve and rolls capital toward its highest mathematical efficiency, locating the absolute peak return on investment.
    """)

    st.subheader("3. Historical Precedents of Successful Strategic Disruption")
    st.markdown("""
    Strategic product cannibalization is not unique to generative AI; it is a fundamental pattern in technology management. Firms that survive structural platform breaks choose to weaponize their new disruption rather than desperately trying to protect a dying cash cow:
    
*   Netflix (Physical DVDs vs. Digital Streaming): In 2007, Netflix's primary financial cash cow was shipping physical DVDs in red envelopes. When streaming technology emerged, management realized it was an excellent product-market fit but would actively destroy their core mailing customer base. Instead of hiding the new tech to preserve legacy margins, Netflix aggressively bundled streaming into their plans and utilized high physical DVD revenues to bankroll massive digital streaming server overhead, eventually scaling transaction volume to achieve global dominance.
*   Apple (The iPod vs. The iPhone): In the mid-2000s, the standalone iPod was Apple’s flagship revenue engine. During internal product development, Steve Jobs recognized that cellular devices would eventually bundle music playback natively. Rather than leaving this weapon to a competitor, Apple intentionally designed the iPhone to entirely wipe out the standalone iPod market. They accepted the death of their number-one hardware line because they successfully transitioned occasional device buyers into premium, lifetime smartphone ecosystem subscribers.
*   Adobe (Upfront Perpetual Licenses vs. Continuous SaaS Cloud Models): Adobe historically generated large upfront injections of capital by selling boxed software suites (like Photoshop) for over $1,000. In 2013, they radically shifted to the Creative Cloud monthly subscription model. This move intentionally cut off their largest short-term revenue source and caused panic on Wall Street. However, by lowering the cost barrier to entry, Adobe vastly expanded their total active user base, trading short-term margin deficits for highly predictable, compounding recurring customer lifetime value.
*   The Modern Google Ads Evolution (Legacy Search Clicks vs. Conversational AI Modalities): Google currently finds itself navigating this exact historical blueprint. Traditional text-based search queries with high-margin cost-per-click values are being organically cannibalized by conversational summaries. Just as Apple sacrificed the iPod and Netflix shifted away from mail, the modern search engine must aggressively scale native conversational ad units. They must use portfolio optimization models to capture the user session at the new conversational source rather than attempting to force traffic backward into legacy web page links.
""")
st.subheader("4. Conclusion: Moving from $0.50 Cost-Per-Click to 3-5% Transaction Commissions")
st.markdown("""
The transition toward Conversational Search and Autonomous AI Shopping Agents marks the death of the legacy Cost-Per-Click (CPC) monetization framework. When bots or AI systems execute the mundane parts of product search on behalf of humans, charging a merchant 50 cents for an arbitrary link impression becomes irrelevant.
The Strategic Evolution: Google and major search engines must pivot from charging for intent traffic generation to charging for direct transaction fulfillment (Cost-Per-Acquisition / CPA).
Instead of collecting small fractional click fees, the new model transforms the platform into an end-to-end transaction hub. When an AI summary interface directly handles flight bookings, grocery ordering, or service scheduling natively inside the conversation interface, the platform takes an integrated 3% to 5% commission cut of the actual verified purchase total.
By scaling transaction cut monetization, the platform converts what was a low-margin text summary into an incredibly high-value, friction-free commerce machine. This shift dramatically elevates customer lifetime value metrics and generates much higher revenue yields than legacy web page blue links could ever support.
""")
