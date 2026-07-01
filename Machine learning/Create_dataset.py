import pandas as pd
import random

random.seed(42)

data = []

for _ in range(50):
    age = random.randint(20, 60)
    bill = random.randint(20, 120)
    complaints = random.randint(0, 10)

    # Simple rule to generate churn
    if bill > 70 or complaints > 5:
        churn = 1
    else:
        churn = 0

    data.append([age, bill, complaints, churn])

df = pd.DataFrame(
    data,
    columns=["Age", "MonthlyBill", "Complaints", "Churn"]
)

df.to_csv("churn_dataset.csv", index=False)

print("Dataset created successfully!")
print(df.head())