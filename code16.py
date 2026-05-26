import pandas as pd

df = pd.read_excel('emails (7).xlsx',header=None, names=['Email', 'Name', 'Surname'])


kostas_papadopoulos_df = df[(df['Name'] == 'kostas') & (df['Surname']== 'papadopoulos')]
posoi_kostas_papadopoulos = len(kostas_papadopoulos_df)
print(f"Οι εγγραφές με το όνομα kostas είναι στον αριθμό {posoi_kostas_papadopoulos}")
print("Και συγκεκριμένα είναι οι κάτωθι: ")
print(kostas_papadopoulos_df)
