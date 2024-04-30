#Exercise 8: Wine
import numpy as np

red_wine_data = np.genfromtxt("winequality-red.csv", delimiter=";",
dtype=np.float32, deletechars=" ",skip_header=1)

print("size = ", red_wine_data.size*red_wine_data.itemsize)

print("1 : ")
arr_2d = np.array([red_wine_data[0], red_wine_data[5], red_wine_data[10]])
print(arr_2d)

print("2 : ")
alcoholFlag = np.any(red_wine_data[:, -2] >= 20)
print(alcoholFlag)

print("3 : ")
print(np.nanmean(red_wine_data[:,-2]))

print("4 : ")
ph_arr = np.sort(red_wine_data[:,-4])
print("min :", np.min(ph_arr))
print("max :", np.max(ph_arr))
print("mean :", np.nanmean(ph_arr))
print("25th :", np.percentile(red_wine_data[0:, 8], 25.0))
print("50th :", np.percentile(red_wine_data[0:, 8], 50.0))
print("75th :", np.percentile(red_wine_data[0:, 8], 75.0))


print("5 : ")
sorted_sulphates = np.argsort(red_wine_data[:, -3])
sorted_quality = red_wine_data[:, -1][sorted_sulphates]
top_20_quality = sorted_quality[:int(len(sorted_quality) * 0.2)]
average_quality = np.mean(top_20_quality)
print(average_quality)

print("6 : ")
sorted_quality = np.argsort(red_wine_data[:, -1])
best_quality_wines = red_wine_data[sorted_quality[-1]]
worst_quality_wines = red_wine_data[sorted_quality[0]]

print("best : ", best_quality_wines)
print("worst : ", worst_quality_wines)
