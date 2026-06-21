import pandas as pd

df=pd.read_csv("kaggle/Railway_dataset.csv")

pd.DataFrame()

print("FIRST 10 rows:\n",df.head(10))

print("LAST 10 rows::\n",df.tail(10))

print("COLUMN of the dataframes::\n",df.columns)

print("DATA TYPES of column::\n",df.dtypes)

print("BASIC Analysis::\n",df.describe())

print("INFO about dataframe::\n",df.info())

print("NULL values in colums ::\n",df.isnull().sum())

df["Age"] = df[ "Age"]. fillna(df["Age"].mean())

print("AGE COLUMN after the filling null\n",df["Age"])

df["Cabin"].dropna(inplace=True)

print("After the drop null rows ::\n",df.head())

print(df.shape)