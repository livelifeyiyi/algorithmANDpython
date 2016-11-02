from hdbcli import dbapi
import MySQLdb
import pymssql
from DBUtils import PooledDB

def conn_db(db_type,db_user,db_pwd,db_address,db_port,db_name):
    if db_type == "HANA":
        print "HANA connecting..."
        #db_con = dbapi.connect( user=db_user, password=db_pwd, address=db_address, port=int(db_port), autocommit=True )
        pool = PooledDB.PooledDB(dbapi,user=db_user, password=db_pwd, address=db_address, port=int(db_port), autocommit=True)
        db_con = pool.connection()
    if db_type == "MySQL":
        print "Mysql connecting..."
        #db_con = MySQLdb.connect( db_address, db_user, db_pwd, db_name )
        #pool = PooledDB.PooledDB(creator=MySQLdb, mincached=1, maxcached=20, host=, port=)
        pool = PooledDB.PooledDB(MySQLdb,host=db_address,user=db_user,passwd=db_pwd,db=db_name)
        db_con = pool.connection()
    if  db_type == "SQL Server":
        print "SQL Server connecting..."
        #db_con = pymssql.connect( db_address, db_user, db_pwd, db_name ) 
        
        pool = PooledDB.PooledDB(pymssql,host=db_address,user=db_user,passwd=db_pwd,db=db_name)
        db_con = pool.connection()
    return db_con