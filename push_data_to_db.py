# import pandas as pd
#
# df = pd.read_csv("data/Bdichtheid2025.csv", on_bad_lines="skip", sep=";")
# print(df.head())
# print(df.shape[0])
#
# import sqlite3
# conn = sqlite3.connect("data/buurt_data.db")
# cur = conn.cursor()
# cur.execute('''DROP TABLE IF EXISTS buurt_data''')
# cur.execute('''CREATE TABLE buurt_data (gemeente TEXT, bevolkingsdichtheid_per_km2 REAL)''')
# conn.commit()
#
# for index, row in df.iterrows():
#     cur.execute("INSERT INTO buurt_data (gemeente, bevolkingsdichtheid_per_km2) VALUES (?, ?)",
#                 (row['Gemeente'], row['Inwoners per km² land']))
#
# conn.commit()
# conn.close()
# print("Data inserted into database successfully.")

# import pandas as pd
# df = pd.read_csv("data/CBSWijkenBuurten.csv", on_bad_lines="skip", sep=";")
# import sqlite3
# conn = sqlite3.connect("data/buurt_data.db")
# cur = conn.cursor()
# cur.execute('''DROP TABLE IF EXISTS buurt_data_2''')
# df.to_sql('buurt_data_2', conn, if_exists='replace', index=False)
# conn.commit()
# conn.close()

# gemeenten = df[df['RegioS'].str.startswith('GM')]
# print(gemeenten.head())
# print(gemeenten.shape[0])

import pandas as pd
df = pd.read_excel("data/gemeenten-alfabetisch-2024.xlsx")
print(df.head())
import sqlite3
conn = sqlite3.connect("data/buurt_data.db")
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS gemeenten''')
df.to_sql('gemeenten', conn, if_exists='replace', index=False)
conn.commit()
conn.close()