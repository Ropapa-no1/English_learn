import pandas as pd

# Excel-fájl elérési útja
excel_fajl_path = 'data\szavak.xlsx'

# Excel-fájl beolvasása egy pandas DataFrame-be
df = pd.read_excel(excel_fajl_path, sheet_name=0)
print (df)

nev_lista = df['Magyar'].tolist()
eletkor_lista = df['Angol'].tolist()
varos_lista = df['Kategória'].tolist()


df.loc[df['Magyar'] == 'gyors', 'Tudásszint'] += 1



# DataFrame kiíratása
print(df)

print (nev_lista)

print (df['Magyar'][0])


# df.to_excel(excel_fajl_path, index=False)

# Példa DataFrame létrehozása
# data = {'Név': ['John', 'Alice', 'Bob'],
#         'Életkor': [28, 24, 22],
#         'Város': ['New York', 'Los Angeles', 'Chicago']}
# df = pd.DataFrame(data)

# # Életkor módosítása
# df.loc[df['Név'] == 'Alice', 'Életkor'] = 25

# # Kiíratás
# print(df)