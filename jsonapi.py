import pandas as pd

df = pd.read_excel('emails (10).xlsx',header=None, names=['Email', 'Name', 'Surname', 'City'])


df_clean = df.drop_duplicates(subset=['Email']).copy()
print(df_clean)
json_output = df_clean.to_json(orient='records', force_ascii=False , indent=4)

print(json_output)

with open('users_clean.json', 'w', encoding='utf-8') as f:
  f.write(json_output)
