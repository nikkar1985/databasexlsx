import pandas as pd

df = pd.read_excel('emails (10).xlsx',header=None, names=['Email', 'Name', 'Surname', 'City'])


print(f"Ο αρχικός πίνακας είχε {len(df)} γραμμές")
df_clean=df.drop_duplicates(subset=['Email']).copy()
print(f"Ο καθαρός πίνακας είχε {len(df_clean)} γραμμές")
panos_papagiannis = df_clean[(df_clean['Name']=='panos') & (df_clean['Surname']== 'papagiannis') & (df_clean['City']== 'kalamata')]

print(f"Βρέθηκαν {len(panos_papagiannis)} εγγραφές με το όνομα panos papagiannis και συγκεκριμένα η : ")
print(panos_papagiannis)
