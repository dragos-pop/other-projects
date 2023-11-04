# 09:06:10 - sitting
# 09:14:20 - standing
# 09:21:54 - laying
# 09:31:10 - standing (break)
# 09:36:50 - laying
# 09:48:48 - sitting
# 09:59:36 - standing
# 10:06:29 - laying
# 10:15:15 - standing
# 10:20:19 - sitting
# 10:30:00 - end

import pandas as pd
from datetime import datetime

df = pd.read_csv("data/added_features.csv")
labels = []

times = {datetime.strptime("2023-06-09 09:06:10", "%Y-%m-%d %H:%M:%S"): "sitting",
         datetime.strptime("2023-06-09 09:14:20", "%Y-%m-%d %H:%M:%S"): "standing",
         datetime.strptime("2023-06-09 09:21:54", "%Y-%m-%d %H:%M:%S"): "laying",
         datetime.strptime("2023-06-09 09:31:10", "%Y-%m-%d %H:%M:%S"): "standing",
         datetime.strptime("2023-06-09 09:36:50", "%Y-%m-%d %H:%M:%S"): "laying",
         datetime.strptime("2023-06-09 09:48:48", "%Y-%m-%d %H:%M:%S"): "sitting",
         datetime.strptime("2023-06-09 09:59:36", "%Y-%m-%d %H:%M:%S"): "standing",
         datetime.strptime("2023-06-09 10:06:29", "%Y-%m-%d %H:%M:%S"): "laying",
         datetime.strptime("2023-06-09 10:15:15", "%Y-%m-%d %H:%M:%S"): "standing",
         datetime.strptime("2023-06-09 10:20:19", "%Y-%m-%d %H:%M:%S"): "sitting",
         datetime.strptime("2023-06-09 10:30:00", "%Y-%m-%d %H:%M:%S"): "end"}

# 2023-06-09 09:06:09.999236959

for _, row in df.iterrows():
    date = datetime.strptime(row.timestamp.split(".")[0], "%Y-%m-%d %H:%M:%S")

    label = None

    for time in times:
        if date >= time:
            label = times[time]

    labels.append(label)

df["label"] = labels

df.to_csv("data/data_complete.csv", index=False)

