import sqlite3

conn = sqlite3.connect('hotels.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table_name in tables:
    table = table_name[0]
    print(f"\n=== {table} ===")
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        print()

conn.close()
