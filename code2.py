import pandas as pd
df=pd.read_excel('emails (2).xlsx', header=None, names=['Email'])
print(df)
df_clean = df.drop_duplicates(subset=['Email'])
print(df_clean.head())
