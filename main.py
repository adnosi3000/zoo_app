from gui import displayLoginWindow
import db_backend as db

conn = db.connect("postgres", "postgres", "admin", "localhost", "5432")

displayLoginWindow(conn)




