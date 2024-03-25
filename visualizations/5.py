#Exercise 5: Matplotlib subplots
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(7, 4))

fig.subplots_adjust(hspace=0.5, wspace=0.5)


for i in range(1, 7):
    row = (i-1) // 3
    col = (i-1) % 3
    
    ax = axes[row, col]
    
    ax.text(0.5, 0.5, f'(2,3,{i})', ha='center')
    
    ax.set_title(f'Title {i}')

plt.show()
