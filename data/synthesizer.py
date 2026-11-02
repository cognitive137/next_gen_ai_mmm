import numpy as np
import pandas as pd

def generate_synthetic_data(days=1095):
    np.random.seed(42)
    date_range = pd.date_range(start="2023-11-01", periods=days, freq="D")

    trend = np.linspace(100, 150, days)
    seasonality = 10 * np.sin(2 * np.pi * np.arange(days) / 365)
    noise = np.random.normal(0, 5, days)

    traditional_spend = np.random.uniform(500, 1500, days)
    ai_spend = np.zeros(days)

    break_point = 700
    ai_spend[break_point:] = np.random.uniform(300, 1000, days - break_point)
    traditional_spend[break_point:] = traditional_spend[break_point:] * 0.8

    df = pd.DataFrame({
        "date": date_range,
        "traditional_search_spend": traditional_spend,
        "ai_overview_spend": ai_spend,
        "trend": trend,
        "seasonality": seasonality
    })

    beta_trad = 0.15
    beta_ai = 0.08
    gamma = 0.05 

    revenue = 50 + df["trend"] + df["seasonality"] + noise
    revenue[:break_point] += beta_trad * df["traditional_search_spend"][:break_point]

    ai_effect = df["ai_overview_spend"][break_point:]
    trad_effect = df["traditional_search_spend"][break_point:]

    revenue[break_point:] += (beta_trad * trad_effect * (1.0 - gamma * (ai_effect / 1000))) + (beta_ai * ai_effect)
    df["revenue"] = revenue
    return df

if __name__ == "__main__":
    import os
    os.makedirs("data", exist_ok=True)
    data = generate_synthetic_data()
    data.to_csv("data/marketing_data.csv", index=False)
    print("Dataset successfully compiled with structural break tracking at Day 700.")
