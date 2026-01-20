import pandas as pd
import numpy as np

np.random.seed(42)
n = 200

data = pd.DataFrame({
    "ipk_1": np.random.uniform(2.0, 4.0, n),
    "ipk_2": np.random.uniform(2.0, 4.0, n),
    "ipk_3": np.random.uniform(2.0, 4.0, n),
    "ipk_4": np.random.uniform(2.0, 4.0, n),
    "sks": np.random.randint(80, 150, n),
    "hadir": np.random.uniform(60, 100, n),
    "organisasi": np.random.randint(0, 2, n),
    "mengulang": np.random.randint(0, 6, n)
})

# target yg ingin di capai
data["lama_studi"] = (
    10
    - (data[["ipk_1", "ipk_2", "ipk_3", "ipk_4"]].mean(axis=1) - 2) * 2
    - (data["hadir"] / 100)
    + (data["mengulang"] * 0.5)
).round(1)

data.to_csv("regression/data/mahasiswa.csv", index=False)
data.head()