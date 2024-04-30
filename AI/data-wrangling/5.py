import pandas as pd
import numpy as np

data = {
    'value': [20.45, 22.89, 32.12, 111.22, 33.22, 100, 99.99],
    'product': ['table', 'chair', 'chair', 'mobile phone', 'table', 'mobile phone', 'table']
}
df_products = pd.DataFrame(data)


print(df_products)

aggregated_data = df_products.groupby('product').agg(
    min_price=('value', 'min'),
    max_price=('value', 'max'),
    mean_price=('value', 'mean')
).reset_index()

print(aggregated_data)
