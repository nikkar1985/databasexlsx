import pandas as pd

df = pd.read_excel('emails (7).xlsx',header=None, names=['Email', 'Name', 'Surname'])
df

kostas_df = df[df['Name'] == 'kostas']
posoi_kostas = len(kostas_df)

print(f"Οι εγγραφές με το όνομα kostas είναι στον αριθμό {posoi_kostas}")
print("Και συγκεκριμένα είναι οι κάτωθι: ")
print(kostas_df)
