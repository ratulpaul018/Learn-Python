import pandas as pd

keyword = int(input("Enter 0 for search by Country name.\n1 for capital name.\n2currency name.\n3 for continent name:.\n "))
if keyword == 0:
    query = str(input("Enter a Country Name: "))
if keyword == 1:
    query = str(input("Enter a Capital Name: "))
if keyword == 2:
    query = str(input("Enter a Currency Name: "))
if keyword == 3:
    query = str(input("Enter a Continent Name: "))

query = query.capitalize()
file_path = "Country detail.xlsx"
df = pd.read_excel(file_path)
df.set_index(df.columns[keyword], inplace = True)
row = df.loc[f"{query}"]
print(row)