import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#1
df = pd.read_excel("catalog_products.xlsx")
count_of_the_rows = len(df)
count_of_the_columns = len(df.columns)
print(count_of_the_rows)
print(count_of_the_columns)
print(df.isnull().sum())
print(df.head(6))
print(df.dtypes)

#2
for column in df.columns:
    if df[column].dtype == "int64":
        df[column] = df[column].astype(float)
        avg = df[column].mean()
        df[column] = df[column].fillna(avg)

#3
df["total_value"] = df["col_2"] * df["col_3"]
df["log_price"] = np.log(df["col_2"])
df["double_stock"] = df["col_3"] * 2

#4
df["col_2"].hist(bins=20)
plt.title("Histogram of col_2")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()