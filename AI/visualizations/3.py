import pandas as pd
import matplotlib.pyplot as plt

x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]

plt.figure(figsize=(8, 6))

plt.scatter(x, y, color='blue', s=12**2, zorder=3) 
plt.plot(x, y, color='red', linestyle='dashdot', linewidth=3)

plt.title('Display marker')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.xlim(1, 8)
plt.ylim(1, 8)

plt.show()
