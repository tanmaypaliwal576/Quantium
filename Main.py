import pandas as pd 

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

combined = pd.concat([df1, df2, df3])

# Correct filter
pink = combined[combined["product"] == "pink morsel"]

# Calculate Sales
pink["Sales"] = pink["price"] * pink["quantity"]

# Keep required columns
final = pink[["date", "Sales", "region"]]

# Rename columns
final.columns = ["Date", "Sales", "Region"]

# Save output
final.to_csv("output.csv", index=False)

print("output.csv created successfully")
