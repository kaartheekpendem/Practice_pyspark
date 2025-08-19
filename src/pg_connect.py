import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="Pendem12@",  host="localhost", port="5433")

cur = conn.cursor()

cur.execute('select * from incremental')

print(cur.fetchone())
