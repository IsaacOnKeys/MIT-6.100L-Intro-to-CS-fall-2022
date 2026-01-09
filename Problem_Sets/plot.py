import matplotlib.pyplot as plt

nVals = []
linear = []
quadratic = []
cubic = []
exponential = []


for i in range(0, 30):
    nVals.append(i)
    linear.append(i)
    quadratic.append(i**2)
    cubic.append(i**3)
    exponential.append(1.5**i)
plt.subplot(2, 2, 1)
plt.plot(nVals, linear)
plt.title("linear")

plt.subplot(2, 2, 2)
plt.title("quadratic")
plt.plot(nVals, quadratic)

plt.subplot(2, 2, 3)
plt.title("cubic")
plt.ylim(0, 1.5**30)
plt.plot(nVals, cubic)

plt.subplot(2, 2, 4)
plt.title("explonential")
plt.ylim(0, 1.5**30)
plt.scatter(nVals, exponential)
plt.show()
