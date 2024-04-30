#Exercise 3: E-commerce purchases

import pandas as pd 

df = pd.read_csv('Ecommerce_purchases.txt', sep=',')

#1
print(len(df))
print(len(df.columns))


#2
print(df['Purchase Price'].mean())

#3
print(df['Purchase Price'].max())
print(df['Purchase Price'].min())

#4
print(df['Language'].value_counts().get('en', 0))

#5
print(df['Job'].value_counts().get('Lawyer', 0))

#6
unique_periods = df['AM or PM'].unique()
if 'AM' in unique_periods:
    am_purchase_count = (df['AM or PM'] == 'AM').sum()
else:
    am_purchase_count = 0

if 'PM' in unique_periods:
    pm_purchase_count = (df['AM or PM'] == 'PM').sum()
else:
    pm_purchase_count = 0

print("AM: ", am_purchase_count)
print("PM: ", pm_purchase_count)

#7
print(df['Job'].value_counts().head(5))

#8
print(df[df['Lot'] == '90 WT']['Purchase Price'].values[0])

#9
print(df[df['Credit Card'] == 4926535242672853]['Email'].values[0])

#10
print(df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'] > 95)].shape[0])

#11
expiring_in_2025 = df[df['CC Exp Date'].str.endswith('/25')]
print(len(expiring_in_2025))

#12
df['Email Provider'] = df['Email'].str.split('@').str[1]
email_provider_counts = df['Email Provider'].value_counts()
print(email_provider_counts.head(5))