import numpy as np
import pandas as pd
import os

def generate_dataset(n_samples=5000):
    R = 8.314  # Gas constant
    log_A = np.random.uniform(np.log(1e3), np.log(1e13), n_samples)
    A = np.exp(log_A)
    Ea = np.random.uniform(30, 120, n_samples) * 1000  # kJ → J
    T = np.random.uniform(280, 350, n_samples)
    catalyst = np.random.randint(0, 2, n_samples)
    A = A * np.where(catalyst==1, 10, 1)
    k = A * np.exp(-Ea / (R * T))
    k *= np.random.uniform(0.95, 1.05, n_samples)
    
    df = pd.DataFrame({"A": A, "Ea": Ea, "T": T, "catalyst": catalyst, "k": k})
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/dataset.csv", index=False)
    print("Dataset saved to data/dataset.csv!")
    return df

if __name__ == "__main__":
    generate_dataset()
