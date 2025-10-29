"Basic plotting file"

import matplotlib.pyplot as plt

x_vals = []
y_vals = []
z_vals = []

for x in range(0,5):
    y = x + 1
    z = x**2
    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)

plt.figure(1)
plt.plot(x_vals, y_vals, marker = 'o', color = 'b')
plt.plot(x_vals, z_vals, linestyle = '-', color = 'r')
plt.xlabel("X-Values")
plt.legend(["Y-Values", "Z-Values"])
plt.title("Test Plot")
plt.show()