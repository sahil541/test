import pandas as pd
import numpy as np
data = pd.read_csv("ml_lab1.csv")
d = np.array(data)[:, :-1]
# Segregating the target that has +ve & -ve value
last_column = np.array(data)[:, -1]
print(last_column)


def train(c, t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break
    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
    return specific_hypothesis


print("The final hypothesis:", train(d, last_column))
