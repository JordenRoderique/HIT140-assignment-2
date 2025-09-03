import pandas as pd

# Step 1: Load the cleaned datasets

df1 = pd.read_csv("clean_dataset1.csv")
df2 = pd.read_csv("clean_dataset2.csv")

# Step 2: Round 'hours_after_sunset' to one decimal place
# This helps align time values between both datasets for merging
df1['hours_after_sunset'] = df1['hours_after_sunset'].round(1)
df2['hours_after_sunset'] = df2['hours_after_sunset'].round(1)

# Step 3: Merge the datasets on 'month' and 'hours_after_sunset'
# This combines bat landing events with rat activity summaries
merged_df = pd.merge(df1, df2, on=['month', 'hours_after_sunset'], how='inner')

# Step 4: Generate descriptive statistics for key numerical variables
# This gives us count, mean, std, min, max, and percentiles
numerical_summary = merged_df[['risk', 'reward', 'rat_minutes', 'bat_landing_number', 'food_availability']].describe()
print("Numerical Summary Statistics:\n", numerical_summary)

# Step 5: Count frequency of each unique value in 'habit' (bat behavior)
# This helps us to understand which behaviors are most common
habit_counts = merged_df['habit'].value_counts(dropna=False)
print("\nHabit Frequency Counts:\n", habit_counts)

# Step 6: Count frequency of each season (0 = winter, 1 = spring)
# This helps us to see how much data comes from each season
season_counts = merged_df['season'].value_counts(dropna=False)
print("\nSeason Frequency Counts:\n", season_counts)