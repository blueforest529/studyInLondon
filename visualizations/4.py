#Exercise 4: Matplotlib 2

import matplotlib.pyplot as plt

left_data = [5, 7, 11, 13, 17]
right_data = [0.1, 0.2, 0.4, 0.8, -1.6]
x_axis = [0.0, 1.0, 2.0, 3.0, 4.0]

fig, ax1 = plt.subplots()

ax1.plot(x_axis, left_data, color='black', label='Left Data')
ax1.set_ylabel('Big') 

ax2 = ax1.twinx()
ax2.plot(x_axis, right_data, color='red', label='Right Data')
ax2.set_ylabel('Small') 

fig.suptitle('Twin axes')


plt.show()