from app.db_config import DB
import psycopg2
import pandas as pd

def list_rpi():
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query('SELECT * FROM rpi', con)
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
    items = pd.read_sql_query("SELECT * FROM desenho where numero_rpi = '%s'" % (rpi_cod), con)
    items = items.to_dict()
    return items

def rpi_marca(rpi_cod):
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query("SELECT * FROM marca where numero_rpi = '%s'" % (rpi_cod), con)
    items = items.to_dict()
    return items

def rpi_patente(rpi_cod):
    con = psycopg2.connect(host = DB.HOST, port=DB.PORT, user=DB.USER, password=DB.PASSWORD, database=DB.DATABASE)
    items = pd.read_sql_query("SELECT * FROM patente where numero_rpi = '%s'" % (rpi_cod), con)
    items = items.to_dict()
    return items