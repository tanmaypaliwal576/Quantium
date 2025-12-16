import pandas as pd 

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

combined = pd.concat([df1, df2, df3])

# Filter pink morsel
pink = combined[combined["product"] == "pink morsel"]

# FIX: clean and convert data types
pink["price"] = pink["price"].str.replace("$", "", regex=False).astype(float)
pink["quantity"] = pink["quantity"].astype(int)

# Correct Sales calculation
pink["Sales"] = pink["price"] * pink["quantity"]

# Final output
final = pink[["date", "Sales", "region"]]
final.columns = ["Date", "Sales", "Region"]

final.to_csv("output.csv", index=False)

print(final.head())
print("output.csv created successfully")


