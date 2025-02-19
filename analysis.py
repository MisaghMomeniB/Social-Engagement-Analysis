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