# pandas is super usefull! I use it every day for tabular data (such as time-series) and more...
import pandas as pd

# Load data from a CSV file into a DataFrame
data = pd.read_csv('data.csv')

# Load data from an Excel file into a DataFrame
data = pd.read_excel('data.xlsx')


data = pd.DataFrame({'time': pd.date_range('2020-01-01', periods=30,freq='MS'), 'ssr': np.random.randn(30)})
# Display the first few rows of the DataFrame
print(data.head())

# Display the basic information about the DataFrame
print(data.info())

# Compute summary statistics of the DataFrame
print(data.describe())


# Handle missing values
data.dropna()  # Drop rows with missing values
data.fillna(value)  # Fill missing values with a specific value

# Remove duplicates
data.drop_duplicates()

# Transform data types
data['ssr2'] = data['ssr'].astype('int')


# Selecting specific columns
selected_data = data[['ssr', 'time']]

# Filtering rows based on conditions
filtered_data = data[data['ssr'] > 0.03]

# Creating new columns
data['new_column'] = data['ssr'] + 323

# Grouping and aggregation
grouped_data = data.groupby(data.time.dt.month)['ssr'].mean()

# Basic data analysis
total = data['ssr'].sum()
average = data['ssr'].mean()

# Simple visualization
data['ssr'].plot(kind='hist')
plt.show()

# Merge two DataFrames based on a common key
merged_data = pd.merge(df1, df2, on='common_key_column')

# Join two DataFrames based on index
joined_data = df1.join(df2, how='inner')


# Convert a column to DateTime
data['date_column'] = pd.to_datetime(data['date_column'])

# Extracting date components
data['year'] = data['date_column'].dt.year
data['month'] = data['date_column'].dt.month



# Convert text to lowercase
data['text_column'] = data['text_column'].str.lower()

# Splitting text into multiple columns
data[['first_name', 'last_name']] = data['full_name'].str.split(' ', expand=True)



# Create a pivot table
pivot_table = data.pivot_table(index='category', columns='month', values='value', aggfunc='sum')



# Convert a column to categorical type
data['category_column'] = data['category_column'].astype('category')

# Encoding categorical variables
encoded_data = pd.get_dummies(data, columns=['category_column'])



# Resample time series data
resampled_data = data.resample('D').mean()  # Resample to daily frequency

# Rolling window calculations
rolling_mean = data['value_column'].rolling(window=7).mean()  # Calculate 7-day rolling mean


# Fill missing values using forward fill
data.fillna(method='ffill', inplace=True)

# Interpolate missing values
data['column'].interpolate(method='linear', inplace=True)

# Apply a function to each element of a DataFrame
result = data.applymap(lambda x: x*2)  # Multiply each element by 2

# Apply a function to each column or row
result = data.apply(lambda x: x.max() - x.min(), axis=0)  # Calculate range for each column


# Creating a MultiIndex DataFrame
arrays = [np.array(['A', 'A', 'B', 'B']), np.array(['one', 'two', 'one', 'two'])]
multi_index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
multi_index_data = pd.DataFrame({'data': [1, 2, 3, 4]}, index=multi_index)

# Accessing data from a MultiIndex DataFrame
value = multi_index_data.loc[('A', 'one')]



data = pd.DataFrame({'time': pd.date_range('2020-01-01', periods=30,freq='MS'), 'ssr': np.random.randn(30)})
data['ssr2'] = data['ssr'].astype('int')

# Identify and remove outliers using z-score
from scipy import stats
z_scores = np.abs(stats.zscore(data['ssr']))
outlier_threshold = 3
filtered_data = data[(z_scores < outlier_threshold)]


# Reading a large dataset in chunks
chunk_size = 1000
for chunk in pd.read_csv('large_data.csv', chunksize=chunk_size):
    process_chunk(chunk)


# Filter rows where a specific column meets a condition
filtered_data = data[data['ssr'] > 0.5]

# Filter rows where multiple conditions are met using logical operators (& for AND, | for OR)
filtered_data = data[(data['ssr'] > 0.5) & (data['ssr2'] == 0)]


# Filter rows where a string column contains a specific substring
filtered_data = data[data['text_column'].str.contains('substring')]


# Filter rows using the query() method with a boolean expression
filtered_data = data.query('ssr > 0.5 and ssr2 == 0')






