import psycopg2


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



x = connect("postgres", "postgres", "admin", "localhost", "5432")    

# print(get_table_columns(x, "test"))



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


print(run_command_from_file(x, "test.sql"))

    
