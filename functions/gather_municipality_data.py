import json
import sqlite3
import pandas as pd
import os


def gather_municipality_info():
    conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "buurt_data.db"))
    cur = conn.cursor()
    cur.execute('''
        SELECT *, CAST(substr(Perioden, 1, 4) AS INTEGER) AS Year
        FROM gemeenten
        LEFT JOIN buurt_data
        ON gemeenten.Gemeentenaam = buurt_data.gemeente
        LEFT JOIN buurt_data_2
        ON gemeenten.GemeentecodeGM = buurt_data_2.RegioS
        GROUP BY gemeenten.GemeentecodeGM
        ORDER BY MAX(Year) DESC;

    ''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    return json.dumps({"data": json.loads(df.to_json(orient="records"))})

print(gather_municipality_info())