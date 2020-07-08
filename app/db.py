from app.db_config import DB
import psycopg2
import pandas as pd

def list_rpi():
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query('SELECT * FROM rpi ORDER BY rpi ASC', con)
    items = items.to_dict()
    return items

def list_marca():
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query('SELECT * FROM marca', con)
    items = items.to_dict()
    return items

def list_patente():
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query('SELECT * FROM patente', con)
    items = items.to_dict()
    return items

def list_desenho():
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query('SELECT * FROM desenho', con)
    items = items.to_dict()
    return items

def rpi_desenho(rpi_cod):
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query("SELECT * FROM desenho where (numero_rpi = '%s') AND (nome_do_procurador IS NULL)" % (rpi_cod), con)
    items = items.to_dict()
    return items

def rpi_marca(rpi_cod):
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query("SELECT * FROM marca where numero_rpi = '%s' AND procurador IS NULL" % (rpi_cod), con)
    items = items.to_dict()
    return items

def rpi_patente(rpi_cod):
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query("SELECT * FROM patente where numero_rpi = '%s' AND nome_do_procurador IS NULL" % (rpi_cod), con)
    items = items.to_dict()
    return items

def insert_email_desenho(num_ped, email):
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    cur = con.cursor()
    insert = "UPDATE desenho SET email = '%s' WHERE numero_do_pedido = '%s'" % (email, num_ped)
    cur.execute(insert)
    con.commit()
    cur.close()
    con.close()

def insert_email_patente(num_ped, email):
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    cur = con.cursor()
    insert = "UPDATE patente SET email = '%s' WHERE numero_do_pedido = '%s'" % (email, num_ped)
    cur.execute(insert)
    con.commit()
    cur.close()
    con.close()

def insert_email_marca(num_ped, email):
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    cur = con.cursor()
    insert = "UPDATE marca SET email = '%s' WHERE numero = '%s'" % (email, num_ped)
    cur.execute(insert)
    con.commit()
    cur.close()
    con.close()

