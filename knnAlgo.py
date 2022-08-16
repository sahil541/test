import pandas as pd
import numpy as np
data = pd.read_csv('Iris.csv')
x = data.iloc[:,:-1].values
y = data.iloc[:,4].values
s_length = float(input("Enter the length of the sepal: "))
s_width = float(input("Enter the width of the sepal: "))
p_length = float(input("Enter the length of the petal: "))
p_width = float(input("Enter the width of the petal: "))
dis = []
def distance(s_length,s_width,p_length,p_width):
    for i in range(len(x)):
        dis.append(np.sqrt((x[i][0]-s_length)**2+(x[i][1]-s_width)**2+(x[i][2]-p_length)**2+(x[i][3]-p_width)**2))
    return dis
dis = distance(s_length,s_width,p_length,p_width)
dis = np.array(dis)
k = int(input("Enter the value of k: "))
ind = np.argsort(dis)[:k]
list = []
for i in ind:
    list.append(y[i])
list = np.array(list)
print(list)