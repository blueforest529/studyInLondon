#Exercise 2: Pandas plot 2
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
        'name':['christopher','marion','maria','mia','clement','randy','remi'],
        'age':[70,30,22,19,45,33,20],
        'gender':['M','F','F','F','M','M','M'],
        'state':['california','dc','california','dc','california','new york','porto'],
        'num_children':[4,2,1,0,3,1,0],
        'num_pets':[5,1,0,2,2,2,3]
        })


plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['num_children'], color='red', alpha=0.5) 
plt.title('Scatter plot: Number of children and age')
plt.xlabel('age')
plt.ylabel('num_children')

plt.show()
