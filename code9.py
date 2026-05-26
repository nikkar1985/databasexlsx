import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_excel('emails (2).xlsx', header=None, names=['Email'])
df_clean = df.drop_duplicates(subset=['Email'])
print(df)
print(f"Αρχικές γραμμές : {len(df)}")
print(f"Μετά τον καθαρισμό από διπλοεγγραφές είναι : {len(df_clean)}")
print(df_clean.head())

print("\n")
print("Ανάλυση των email που έχουμε στην database μας ")
df_clean['Domain'] = df_clean['Email'].astype(str).str.split('@').str[1]
domain_counts =df_clean['Domain'].value_counts()
print(domain_counts)


plt.figure(figsize=(8, 6))

domain_counts.plot(kind='barh', color='skyblue', edgecolor='black')


plt.title('Κατανομή χρηστών ανά email provider', fontsize=14, fontweight='bold')

plt.xlabel('Πάροχοι emails', fontsize=12)
plt.ylabel('Πλήθος χρηστών', fontsize=12)

plt.grid(axis='x', linestyle='--', alpha = 0.7)

plt.tight_layout()

plt.show()

