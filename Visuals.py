import pandas as pd
import plotly.express as px

# Step 1: Load the cleaned datasets
df1 = pd.read_csv("clean_dataset1.csv")
df2 = pd.read_csv("clean_dataset2.csv")

# Step 2: Round 'hours_after_sunset' to align time values
df1['hours_after_sunset'] = df1['hours_after_sunset'].round(1)
df2['hours_after_sunset'] = df2['hours_after_sunset'].round(1)

# Step 3: Merge datasets on 'month' and 'hours_after_sunset'
merged_df = pd.merge(df1, df2, on=['month', 'hours_after_sunset'], how='inner')

# Step 4: Bar chart - Risk vs Reward
risk_reward_counts = merged_df.groupby(['risk', 'reward']).size().reset_index(name='count')
fig1 = px.bar(risk_reward_counts, x='risk', y='count', color='reward', barmode='group',
              title='Risk vs Reward Behavior')
fig1.show()

# Step 5: Histogram - Distribution of Rat Minutes
fig2 = px.histogram(merged_df, x='rat_minutes', nbins=30, title='Distribution of Rat Minutes')
fig2.show()

# Step 6: Boxplot - Food Availability by Risk
fig3 = px.box(merged_df, x='risk', y='food_availability',
              title='Food Availability by Risk Behavior')
fig3.show()

# Step 7: Bar chart - Frequency of Bat Habits
habit_counts = merged_df['habit'].value_counts().reset_index()
habit_counts.columns = ['habit', 'count']
fig4 = px.bar(habit_counts, x='habit', y='count', title='Frequency of Bat Habits')
fig4.show()

# Step 8: Pie chart - Season Distribution
season_counts = merged_df['season'].value_counts().reset_index()
season_counts.columns = ['season', 'count']
fig5 = px.pie(season_counts, names='season', values='count', title='Season Distribution')
fig5.show()