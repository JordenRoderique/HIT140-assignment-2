import pandas as pd

# Load the cleaned datasets
df1 = pd.read_csv("clean_dataset1.csv")
df2 = pd.read_csv("clean_dataset2.csv")

# Round 'hours_after_sunset' to one decimal place in both datasets
df1['hours_after_sunset'] = df1['hours_after_sunset'].round(1)
df2['hours_after_sunset'] = df2['hours_after_sunset'].round(1)

# Merge the datasets on 'month' and 'hours_after_sunset'
merged_df = pd.merge(df1, df2, on=['month', 'hours_after_sunset'], how='inner')

# Save the merged dataset
merged_df.to_csv("merged_dataset.csv", index=False)

# Optional: Print summary info
print("Merged dataset shape:", merged_df.shape)
print("Merged dataset columns:", merged_df.columns.tolist())