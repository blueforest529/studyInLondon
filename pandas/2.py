#Exercise 2: Electric power consumption

import pandas as pd 
import datetime

# Q2
df = pd.read_csv('household_power_consumption.txt', sep=';', na_values='?')
print(len(df))

# Q3
def update_types(df):
    df.drop(['Time', 'Sub_metering_2', 'Sub_metering_3'], axis = 1, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df.set_index(keys='Date', inplace=True)
    df.index = df.index.astype('datetime64[ns]')
    return df

new_df = update_types(df)

print(new_df.head().index)
print(new_df.dtypes)

#4
print(df.describe())

#5

print(df.dropna(inplace=True))
print(df.isna().sum())


#6
new_df.loc[:,'Sub_metering_1'] = new_df.loc[:,'Sub_metering_1'].apply(lambda x: (x+1)*0.06)
print(new_df['Sub_metering_1'])

#7
selected_rows = new_df[(new_df.index >= '2008-12-27') & (new_df['Voltage'] >= 242 ) ]
print(selected_rows.head().to_markdown())

#8
print(new_df.iloc[88887])


#9
max_global_active_power_row = new_df[new_df['Global_active_power'] == new_df['Global_active_power'].max()]
max_date = max_global_active_power_row.index.values[0]
print(max_date)


#10
filtered_df = new_df.dropna(subset=['Global_active_power', 'Global_reactive_power', 'Voltage'])
sorted_df = filtered_df.sort_values(by=['Global_active_power', 'Voltage'], ascending=[False, True])
print(sorted_df.tail().to_markdown())

#11
daily_average = new_df.groupby(new_df.index.date)['Global_active_power'].mean()
print(daily_average)

