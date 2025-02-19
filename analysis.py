import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
# This reads the data from the given file path and stores it in a Pandas DataFrame.
file_path = "./big_social_media_data.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
# This shows the number of rows, columns, data types, and non-null values for each column.
print(df.info())

# Display summary statistics of numerical columns
# This gives insights like mean, min, max, and percentiles of numerical data.
print(df.describe())

# Display the first five rows of the dataset
# This helps to understand the structure and content of the data.
print(df.head())

# Convert 'Post_Date' column to datetime format
# This ensures that date-related operations (like sorting, filtering) work correctly.
df['Post_Date'] = pd.to_datetime(df['Post_Date'])

# Count the number of posts per platform
# This calculates how many posts exist for each social media platform.
platform_counts = df['Platform'].value_counts()

# Plot the number of posts per platform
# This visualization helps to see which platform has the most or least posts.
plt.figure(figsize=(10, 6))
sns.barplot(x=platform_counts.index, y=platform_counts.values)
plt.title("Number of Posts per Platform")
plt.xlabel("Platform")
plt.ylabel("Number of Posts")
plt.xticks(rotation=45)  # Rotates labels for better readability
plt.show()

# Calculate average engagement metrics per platform
# This groups data by platform and calculates the average likes, comments, shares, and views.
platform_engagement = df.groupby('Platform')[['Likes', 'Comments', 'Shares', 'Views']].mean().reset_index()

# Plot engagement metrics per platform
# This visualization compares how different platforms perform in terms of engagement.
plt.figure(figsize=(12, 6))
sns.barplot(x="Platform", y="Likes", data=platform_engagement, color="blue", label="Likes")
sns.barplot(x="Platform", y="Comments", data=platform_engagement, color="red", label="Comments", alpha=0.7)
sns.barplot(x="Platform", y="Shares", data=platform_engagement, color="green", label="Shares", alpha=0.5)
sns.barplot(x="Platform", y="Views", data=platform_engagement, color="orange", label="Views", alpha=0.3)

plt.title("Average Engagement per Platform")
plt.xlabel("Platform")
plt.ylabel("Average Count")
plt.legend()
plt.xticks(rotation=45)  # Rotates labels for better readability
plt.show()