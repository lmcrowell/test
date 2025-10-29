"Basic plotting file"

import matplotlib.pyplot as plt

x_vals = []
y_vals = []

for x in range(0,5):
    y = x + 1
    x_vals.append(x)
    y_vals.append(y)

plt.plot(x_vals, y_vals, marker = 'o')
plt.xlabel("X-Values")
plt.ylabel("Y-Values")
plt.title("Test Plot")
plt.show()