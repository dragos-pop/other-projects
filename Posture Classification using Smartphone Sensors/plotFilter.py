import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/data_v1.csv")
df2 = pd.read_csv("data/data_Kalman_filtered.csv")

for col in df.columns:
    if col == "timestamp": continue

    plt.plot(df[col], label="original")
    plt.plot(df2[col], label="filtered")
    plt.title(col)
    plt.legend()
    plt.savefig(f"figs/{str(col).replace('/', '-')}.png")
    plt.close()