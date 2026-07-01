import pandas as pd
data = {
    "Age": [25, 40, 35, 28, 50],
    "MonthlyBill": [20, 80, 60, 35, 100],
    "Complaints": [1, 7, 3, 2, 9],
    "Churn": [0, 1, 0, 0, 1]
}
df = pd.DataFrame(data)
print(df)
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)
print(df.tail())
print(df.head())

x = df[["Age","MonthlyBill","Complaints"]]
y = df["Churn"]

