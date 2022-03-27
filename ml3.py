import matplotlib.pyplot as plt
from scipy import stats
x = [2, 9, 5, 5, 3, 7, 1, 8, 6, 2]
y = [69, 98, 82, 77, 71, 84, 55, 94, 84, 64]
slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope*x+intercept


mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
