import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = "bob"
plt.plot(x, np.sin(x))
plt.savefig('sin')
