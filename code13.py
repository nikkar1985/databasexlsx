import pandas as pd
import matplotlib.pyplot as plt
import re



df=pd.read_excel('emails (4).xlsx', header=None, names=['Email'])
df_clean = df.drop_duplicates(subset=['Email'])
print(df)
print(f"Αρχικές γραμμές : {len(df)}")
print(f"Μετά τον καθαρισμό από διπλοεγγραφές είναι : {len(df_clean)}")
print(df_clean.head())

def validate_email(email):
  pattern=r'[a-z0-9]+@[a-z]+\.[a-z]{2,3}'
  return bool(re.match(pattern, str(email)))  


df_clean['Is_Valid']= df_clean['Email'].apply(validate_email)

df_valid= df_clean[df_clean['Is_Valid']== True].copy()
df_invalid = df_clean[df_clean['Is_Valid']== False]

print(f" Έγκυρα email για ανάλυση είναι : {len(df_valid)}")
print(f"Μη έγκυρα email για ανάλυση είναι : {len(df_invalid)}")


if len(df_valid)>0:
  print("Έγκυρα μαιλ")
  print(df_valid['Email'])

if len(df_invalid) >0 :
  print("\n Οι λανθασμένες εγγραφές είναι:")
  print(df_invalid['Email'])


df_valid['Domain'] = df_valid['Email'].astype(str).str.split('@').str[1]

domain_counts = df_valid['Domain'].value_counts()

print(domain_counts)

domain_counts.plot(kind='bar', color='skyblue', edgecolor='black', rot=45)


plt.title('Κατανομή χρηστών ανά email provider', fontsize=14, fontweight='bold')

plt.xlabel('Πάροχοι emails', fontsize=12)
plt.ylabel('Πλήθος χρηστών', fontsize=12)

plt.grid(axis='y', linestyle='--', alpha = 0.7)

plt.tight_layout()

plt.show()

df_valid.to_excel('validanalysis.xlsx', index=False)
print("\n")
