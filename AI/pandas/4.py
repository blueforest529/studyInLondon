#Exercise 4: Handling missing values
import pandas as pd 

# 데이터 불러오기
df = pd.read_csv('iris.txt', sep=',')

# 'flower' 열 삭제
df = df.drop(columns=['flower'])

df['sepal_length'] = pd.to_numeric(df.loc[:,'sepal_length'], errors='coerce')
df['sepal_width'] = pd.to_numeric(df.loc[:,'sepal_width'], errors='coerce')

df.fillna({
        0:df.sepal_length.mean(),
        2:df.sepal_width.median(),
        3:0,
        4:0
    })
    
print(df)

df.iloc[122] = 0

medians = df.median()
df.fillna(medians, inplace=True)

print(df)