import matplotlib.pyplot as plt
import numpy as np

EXPAND = 3
SIZE = 120

x = np.linspace(-np.pi * EXPAND, np.pi * EXPAND, SIZE)
y = np.sin(x)

z = np.random.uniform(-0.5, 0.5, SIZE)

plt.plot(x, y, color="blue", marker=".")
plt.plot(x, y + z, color="green", marker=".")
plt.title("Plot of sin(x)")
plt.show()
