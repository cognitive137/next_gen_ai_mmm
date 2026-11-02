import numpy as np
from scipy.optimize import minimize
from models.transformations import apply_hill_saturation

def objective_function(spend_vector, base_beta_trad, base_beta_ai, gamma, alpha, kappa, post_exposure_eff):
    s_spend, a_spend = spend_vector
    
    # 1. Map raw spends to standard saturation curves (0.0 to 1.0)
    s_sat = apply_hill_saturation(np.array([s_spend]), alpha, kappa)[0]
    a_sat = apply_hill_saturation(np.array([a_spend]), alpha, kappa)[0]
    
    # 2. DYNAMIC PARADIGM SHIFT EQUATIONS:
    # As AI ad spend scales up, its revenue power accelerates exponentially,
    # supercharged by the Post-Exposure Interaction Depth Effectiveness parameter.
    dynamic_beta_ai = base_beta_ai * (1.0 + (a_spend / 1000.0) ** 1.5) * (post_exposure_eff / 100.0)
    
    # Traditional blue links organically decay as AI adoption (gamma * a_sat) increases.
    dynamic_beta_trad = base_beta_trad * max(0.0, (1.0 - gamma * a_sat))
    
    # Combined Portfolio Structural Equation
    revenue = (dynamic_beta_trad * s_sat) + (dynamic_beta_ai * a_sat)
    
    return -revenue

def optimize_budget(total_budget, base_beta_trad, base_beta_ai, gamma, alpha, kappa, post_exposure_eff):
    x0 = [total_budget / 2, total_budget / 2]
    constraints = ({'type': 'ineq', 'fun': lambda x: total_budget - (x[0] + x[1])})
    bounds = ((0, total_budget), (0, total_budget))
    
    result = minimize(
        objective_function, x0, 
        args=(base_beta_trad, base_beta_ai, gamma, alpha, kappa, post_exposure_eff), 
        method='SLSQP', bounds=bounds, constraints=constraints
    )
    return float(result.x[0]), float(result.x[1]), float(-result.fun)
