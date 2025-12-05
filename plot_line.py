import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, x**3, color="blue", marker=".")
plt.show()
