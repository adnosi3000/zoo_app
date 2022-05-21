import psycopg2
from maingui import main_gui


def connect(dbname, user, password, host, port):
    '''connects to sql database'''
    try:
        return psycopg2.connect(f"dbname={dbname} user={user} password={password} host={host} port={port}")
    except Exception as error:
        print("Unable to connect to server: ", error)
        return None


def get_table_columns(conn, sql_table):
    '''gathers all column names from certain table'''
    cur = conn.cursor()
    cur.execute(f"select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='{sql_table}' ")
    return cur.fetchall()


def run_command_from_file(conn, txtfile):
    '''runs sql commands from selected file in folder'''
    outs = {}
    
    with open(txtfile, "r") as file:
        data = file.readlines()
        print(data)
        for id_operation, x in enumerate(data):
            try:
                cur = conn.cursor()
                cur.execute(x.strip("\n"))
                outs[id_operation+1] = cur.fetchall()
                conn.commit()
                cur.close()
            except Exception as error:
                print("Error: ", error)
                
    return outs

def login(conn, login, password, table='users'):
    sql = f"select * from public.{table}"
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    
    credentials = (login, password)
    for x in data:
        if x == credentials:
            return True
    
    return False

def createLoginTest(conn, username, password):
    print("wywołuje funkcje createLoginTest")
    out = login(conn, username, password)
    print(out)
    if out == True:
        return main_gui()
    else:
        return lambda: None

    




    
