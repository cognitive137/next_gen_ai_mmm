# Next-Gen Open Source MMM Framework for Conversational AI Ads

An enterprise-grade, privacy-first Marketing Mix Modeling (MMM) engine optimized for modern generative search platforms. This framework leverages Columbia IEOR principles (optimization, econometrics, and stochastics) to quantify and safely mitigate internal product cannibalization caused by on-page conversational layers like Google AI Overviews.

---

## 🎯 Ads Core Business & Context

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

## 📐 Framework & Execution

Instead of using outdated tracking cookies, this engine uses advanced data science and optimization theory to solve the cannibalization problem in four clear steps:

### Step 1: Decompose the Search Channel (The Variables)
Standard data tools lump all Google advertising data into one single bucket. This framework explicitly splits search traffic into two distinct, competing variables:
*   **Traditional Search Spend ($S_t$):** The legacy, high-margin sponsored blue links that rely on user clicks.
*   **AI Overview Spend ($A_t$):** The new, conversational ad spaces injected directly inside the AI's generated response summary.

### Step 2: Calculate the "Memory Effect" (Adstock Transformation)
Advertising does not disappear instantly; its impact decays over time as people remember a brand. The code uses an infinite impulse response decay filter to transform raw daily dollar spend into **effective spend** over a rolling historical timeline:
$$Adstock(x_t) = x_t + \theta \cdot Adstock(x_{t-1})$$
*Where $\theta$ is the memory retention factor tracking how long an ad stays in a customer's head.*

### Step 3: Map Diminishing Returns (Hill Saturation Curve)
Pumping infinite money into an ad channel does not yield infinite returns. Every platform hits a saturation wall where spending an extra dollar gives you zero marginal revenue. The code maps effective spend through a non-linear Hill curve to calculate your exact **Capacity Utilization / Effectiveness Parameter**:
$$Hill(x) = \frac{x^\alpha}{x^\alpha + K^\alpha}$$
*Where $K$ is the inflection point where ad performance drops by exactly 50%, and $\alpha$ controls how aggressively the returns flatline.*

### Step 4: Solve the Cannibalization Optimization Equation (SLSQP)
This is the core IEOR engine. We create a strategic formula where traditional search revenue is multiplied by a **Stochastic Cannibalization Penalty ($\gamma$)** that scales up as AI Overview impressions scale up. The engine then uses calculus gradients via the Sequential Least Squares Programming (SLSQP) method to solve the equation:

$$\max_{S, A} \quad \text{Revenue} = \beta_1 \cdot Hill(S_t) \cdot \left[1.0 - \gamma \cdot Hill(A_t)\right] + \beta_2 \cdot Hill(A_t)$$

$$\text{Subject to the Boundary Constraint:} \quad S_t + A_t \le \text{Total Wallet Budget (B)}$$

The optimizer searches every possible spend combination to locate the exact mathematical sweet spot that protects your baseline business margins under the platform shift.

---

## 🏃 Local Setup Instructions
To run this production framework cleanly on your machine, drop these operational commands directly into your CLI environment:
```bash
pip install -r requirements.txt
python data/synthesizer.py
streamlit run app.py
```
