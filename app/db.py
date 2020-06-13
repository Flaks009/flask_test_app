#from app.db_config import DB
import psycopg2
import pandas as pd

def insert(string_t):
    con = psycopg2.connect(dbname=DB.DBNAME, user=DB.USER, host=DB.HOST, password=DB.PASSWORD)
    cur = con.cursor()
    cur.execute("INSERT INTO test (string_t) VALUES(%s)", (string_t, ))
    con.commit()
    cur.close()
    con.close()

def list_db_sql():
    con = psycopg2.connect(dbname=DB.DBNAME, user=DB.USER, host=DB.HOST, password=DB.PASSWORD)
    items = pd.read_sql_query('SELECT * FROM test', con)
    items = items.to_dict()
    return items
