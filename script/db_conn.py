# https://gist.github.com/kimus/10012910

try:
    import cx_Oracle
except Exception as e:
    raise(( 
        "Error: importing cx_Oracle failed with the error {}, "
        "for details on installing cx_Oracle, have a look at: \n"
        "https://gist.github.com/kimus/10012910").format(e))

dbuser = "orengoreader"
dbpass = "orengoreader"
dbhost = "odb.cs.ucl.ac.uk"
dbport = 1521
dbsid = 'cathora1'

dsn = cx_Oracle.makedsn(dbhost, dbport, dbsid)

def connect():
    db_conn = cx_Oracle.connect(user=dbuser, password=dbpass, dsn=dsn)
    return db_conn

