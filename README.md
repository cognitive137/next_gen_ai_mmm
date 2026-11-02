# Next-Gen Open Source MMM Framework for Conversational AI Ads

An enterprise-grade, privacy-first Marketing Mix Modeling (MMM) engine optimized for modern generative search platforms. This framework leverages Columbia IEOR principles (optimization, econometrics, and stochastics) to quantify and safely mitigate internal product cannibalization caused by on-page conversational layers like Google AI Overviews.

---

## 🎯 The Strategic Core: Business Context & Case Study

### 1. The Core Problem
For twenty years, digital advertising relied entirely on click-level multi-touch attribution (MTA). A user typed a commercial query, clicked a sponsored destination URL, and a cookie tracked the sale. 

Today, this paradigm is dead. Platform security frameworks (e.g., Apple's ATT) have blocked deterministic tracking, while **Generative Search Interfaces transform user behavior from link clicking to direct information synthesis**. Because the AI interface synthesizes multi-source answers directly on-page, traditional high-margin blue-link inventories face structural cannibalization. Marketing teams face falling click metrics but don't know how to track the value of conversational impressions.

### 2. Why This is Vital to Solve
Firms cannot simply withdraw from conversational search layers without surrendering entire market share domains to native AI platforms. The core optimization problem is finding the absolute sweet spot: **How can a brand optimally distribute capital across standard search and conversational units to maximize aggregate revenue without hitting walls of aggressive diminishing marginal returns?** 

### 3. Historical Precedents of Successful Cannibalization
This framework models a classic technology management dilemma. Historically, standard industry survivors proactively cannibalize themselves before a competitor does:
* **Apple:** Proactively targeted the iPod hardware line with the launch of the iPhone, converting hardware buyers into ecosystem lifers.
* **Netflix:** Utilized physical mail cash flows to bootstrap initial low-margin cloud streaming data center overhead.
* **Adobe:** Terminated high-margin upfront software pricing suites to switch to long-term SaaS subscription models.

---

## 🛠️ Repository Architecture
```text
next-gen-ai-mmm/
│
├── data/                  # Time-Series Synthesizers
│   └── synthesizer.py     # Simulates structural breaks & cross-elasticity decay
├── models/                # Econometric Transformation Kernels
│   └── transformations.py # Implements Infinite Impulse Response Adstock & Hill Curves
├── optimization/          # IEOR Constraint Solvers
│   └── allocator.py       # SciPy SLSQP non-linear optimization routine
├── app.py                 # Interactive Streamlit Web Interface Dashboard
└── requirements.txt       # Production Dependencies
```

## 📐 Mathematical Framework & Execution Sub-Steps

### Sub-Step 1: Time-Series De-averaging
Traditional search spends are cleanly decomposed into two competing, endogenous variables: Traditional Search Impressions ($S_t$) and AI Overview Impressions ($A_t$) to accurately measure separate channel actions.

### Sub-Step 2: Adstock (Memory Lag Transformations)
Captures rolling historical consumer memory retention parameters via an infinite impulse response model:
$$Adstock(x_t) = x_t + \theta \cdot Adstock(x_{t-1})$$

### Sub-Step 3: Diminishing Returns Mapping
Passes adstocked exposure arrays through an asymmetric non-linear Hill saturation function to isolate exact capacity utilization thresholds before marginal efficiency trends flatline:
$$Hill(x) = \frac{x^\alpha}{x^\alpha + K^\alpha}$$

### Sub-Step 4: Non-Linear Constrained SLSQP Optimization
The core engine sets up a portfolio matrix to locate a global optimum, using a stochastic cannibalization parameter ($\gamma$) to model the revenue decay that AI views impose on traditional links:
$$\max_{S, A} \quad \text{Revenue} = \beta_1 \cdot Hill(S_t) \cdot \left[1.0 - \gamma \cdot Hill(A_t)\right] + \beta_2 \cdot Hill(A_t)$$
$$\text{Subject to:} \quad S_t + A_t \le \text{Total Budget (B)} \quad \text{and} \quad S_t, A_t \ge 0$$

---

## 🏃 Local Setup Instructions
To run this production framework cleanly on your machine, drop these operational commands directly into your CLI environment:
```bash
pip install -r requirements.txt
python data/synthesizer.py
streamlit run app.py
```
