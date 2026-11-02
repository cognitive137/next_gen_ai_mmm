import numpy as np
from scipy.optimize import minimize
from models.transformations import apply_hill_saturation

def objective_function(spend_vector, beta_trad, beta_ai, gamma, alpha, kappa):
    s_spend, a_spend = spend_vector
    s_sat = apply_hill_saturation(np.array([s_spend]), alpha, kappa)
    a_sat = apply_hill_saturation(np.array([a_spend]), alpha, kappa)

    revenue = (beta_trad * s_sat * (1.0 - gamma * a_sat)) + (beta_ai * a_sat)
    return -revenue

def optimize_budget(total_budget, beta_trad, beta_ai, gamma, alpha, kappa):
    x0 = [total_budget / 2, total_budget / 2]
    constraints = ({'type': 'ineq', 'fun': lambda x: total_budget - (x + x)})
    bounds = ((0, total_budget), (0, total_budget))

    result = minimize(
        objective_function, x0, 
        args=(beta_trad, beta_ai, gamma, alpha, kappa), 
        method='SLSQP', bounds=bounds, constraints=constraints
    )
    return result.x, result.x, -result.fun
