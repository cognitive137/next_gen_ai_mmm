import numpy as np

def apply_adstock(spend, theta):
    """Geometric infinite impulse response decay transformation."""
    adstocked = np.zeros_like(spend)
    adstocked = spend
    for t in range(1, len(spend)):
        adstocked[t] = spend[t] + theta * adstocked[t-1]
    return adstocked

def apply_hill_saturation(adstocked_spend, alpha, kappa):
    """Non-linear Hill function mapping diminishing marginal returns."""
    # Prevent division by zero errors
    if kappa == 0:
        return np.zeros_like(adstocked_spend)
    return (adstocked_spend ** alpha) / ((adstocked_spend ** alpha) + (kappa ** alpha))
