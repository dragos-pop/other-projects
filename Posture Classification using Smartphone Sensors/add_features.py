import pandas as pd
import numpy as np

df = pd.read_csv("data/data_agg_Kalman_filtered.csv")

for col_to_use in df.columns:
    if col_to_use == "timestamp":
        continue

    if np.isnan(df[col_to_use][0]):
        df.drop(col_to_use, axis=1, inplace=True)
        continue

    new_col = []
    temp_mean = []
    sum_mean = 0
    temp_std = []
    x_max = []
    x_min = []

    if col_to_use == "timestamp" or col_to_use == "label": continue

    for i, row in df.iterrows():
        if row[col_to_use] >= 0:
            new_col.append(1)
        else:
            new_col.append(0)


        mean = (row[col_to_use] + sum_mean) / (i + 1)

        temp_mean.append(mean)

    df[f"{col_to_use}-polarity"] = new_col

df.to_csv("data/added_features.csv", index=False)