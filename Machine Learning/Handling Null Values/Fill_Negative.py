import pandas as pd

df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())

# check null values
print(df.isnull().sum())

# fill with negative values
new_df = df.fillna(-999)

print(new_df.isnull().sum())
print(new_df.nunique())
print(new_df['Gender'].value_counts())
