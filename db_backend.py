import psycopg2

def connect(dbname, user, password, host, port):
    try:
        return psycopg2.connect(f"dbname={dbname} user={user} password={password} host={host} port={port}")
    except Exception as error:
        print("Unable to connect to server: ", error)
        return None

def get_data_sql(conn, sql_table):
    cur = conn.cursor()
    return cur.execute("SELECT * from " + sql_table)
    
x = connect("postgres", "postgres", "admin", "localhost", "5432")    
print(get_data_sql(x, "test"))
    
