from hdbcli import dbapi
import binascii
from datetime import datetime, date, time
import sys
import logging
import getpass
'''
_DBADDRESS_='localhost'
_DBPORT_=30015
_DBUSER_='SYSTEM'
_DBPW_='manager'
_SCHEMA_='SBODEMODE'
'''
is_null = True
while is_null:
	_DBADDRESS_ = raw_input("Please input the database address(default: localhost):  ")
	if not _DBADDRESS_:
		_DBADDRESS_='localhost'
	is_null = False
is_null_port = True
while is_null_port:
	_DBPORT_ = raw_input("Please input the database port number(default: 30015):  ")
	if not _DBPORT_:
		_DBPORT_=30015
	is_null_port = False
is_null_user = True	
while is_null_user:
	_DBUSER_ = raw_input("Please input the database username(e.g.user name):  ")
	if not _DBUSER_:
		continue
	else:
		is_null_user = False
is_null_pwd = True	
while is_null_pwd:
	#_DBPW_ = raw_input("Please input the database password:  ")
	_DBPW_ = getpass.getpass("Please input the database password:  ")
	if not _DBPW_:
		continue
	else:
		is_null_pwd = False
is_null_sch = True	
while is_null_sch:
	_SCHEMA_ = raw_input("Please input the schema(e.g.system):  ")
	if not _SCHEMA_:
		continue
	else:
		is_null_sch = False


con_db = dbapi.connect( user=_DBUSER_, password=_DBPW_, address=_DBADDRESS_, port=int(_DBPORT_), autocommit=False )
cursor_db = con_db.cursor()


cursor_db.execute("""select 'NOTE2331696_DB-fixing_' || host || '_' || database_name || '_' || to_char(current_timestamp, 'yyyy-mm-dd_hh24:mi:ss') || '.log' from m_database;
	""")
row_dir = cursor_db.fetchone()
file_dir = '/tmp/'+row_dir[0]
#file_dir = '/tmp/SAP_NOTE_FIX_2317027_log.txt'

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=file_dir,
                filemode='w')


cursor_db.execute("""set schema %s"""%(_SCHEMA_))
cursor_db.execute("""
	select A."SCHEMA_NAME", (select table_type from tables where schema_name = a.schema_name and table_name = a.table_name) as "TABLE_TYPE",A."TABLE_NAME","COUNT_ALL","COUNT_PRELOAD" from (
		select count(column_name) as "COUNT_ALL", table_name,schema_name from table_columns 
		where table_name in ( 
			select distinct table_name from table_columns where preload <> 'FALSE' 
		) 
		group by table_name, schema_name 
	) A 
	left outer join (
		select count(column_name) as "COUNT_PRELOAD",table_name,schema_name
		from table_columns  where preload <> 'FALSE' group by table_name, schema_name
	) B 
	on A.table_name = B.table_name  and A.schema_name = B.schema_name
	where "COUNT_ALL" <> "COUNT_PRELOAD" 
	and A.schema_name = '%s'
"""%(_SCHEMA_)
)
rownum = cursor_db.rowcount
result = cursor_db.fetchall()
table_names = []
failed_table_names = []

if len(result) > 0:

	print "\nPROCESS BEGIN..."
	for row in result:
	
		schema_name = row[0]
		table_type = row[1]
		table_name = row[2]
		
		count_preload = row[4]
		count_all = row[3]
		print "FIXING TABLE " + table_name + " ..."
		logging.info("TABLE " + table_name + " is being fixed!")
		
		cursor_db.execute("""set transaction autocommit ddl off""")
		
		try :
			logging.info("""call GET_OBJECT_DEFINITION(current_schema, '%s');"""%(table_name))
			cursor_db.execute("""call GET_OBJECT_DEFINITION(current_schema, '%s');"""%(table_name))
			
			row_object = cursor_db.fetchone()
			object_creation = row_object[4]
			object_creation = object_creation.split(";\n")
			logging.info("""CREATE %s TABLE %s LIKE %s WITH DATA; """%(table_type,table_name+'_TEMP',table_name))
			cursor_db.execute("""CREATE %s TABLE %s LIKE %s WITH DATA; """%(table_type,table_name+'_TEMP',table_name))
			logging.info("""rename table %s to %s; """%(table_name,table_name+'_BAK'))
			cursor_db.execute("""rename table %s to %s; """%(table_name,table_name+'_BAK'))
			logging.info("""select distinct index_name, index_type from indexes where schema_name = current_schema and table_name = '%s' and (CONSTRAINT <> 'PRIMARY KEY' or CONSTRAINT is null);"""%(table_name+'_BAK'))
			cursor_db.execute("""select distinct index_name, index_type from indexes where schema_name = current_schema and table_name = '%s' and (CONSTRAINT <> 'PRIMARY KEY' or CONSTRAINT is null);"""%(table_name+'_BAK'))
			
			result_index = cursor_db.fetchall()
			if len(result_index) > 0:
				for index in result_index:
					if index[1] == 'FULLTEXT':
						logging.info("""drop FULLTEXT index "%s"; """%(index[0]))
						cursor_db.execute("""drop FULLTEXT index "%s"; """%(index[0]))
					else:
						logging.info("""drop index "%s"; """%(index[0]))
						cursor_db.execute("""drop index "%s"; """%(index[0]))
			for i in range(0,len(object_creation)):
				logging.info(object_creation[i])
				cursor_db.execute(object_creation[i])
			logging.info("""insert into %s (select * from %s); """%(table_name,table_name+'_TEMP'))
			cursor_db.execute("""insert into %s (select * from %s); """%(table_name,table_name+'_TEMP'))
			logging.info("""drop table %s"""%(table_name+'_TEMP'))
			cursor_db.execute("""drop table %s"""%(table_name+'_TEMP'))
			#cursor_db.execute("""commit""")
			con_db.commit()
			table_names.append(table_name)
		except dbapi.Error,e:
			#con_db.rollback()
			cursor_db.execute(""" rollback""")
			logging.error("""SQL error %d:%s"""%(e.args[0],e.args[1]))
			failed_table_names.append(table_name)
			
	print ""
	print "******************Final result:******************"
	if len(failed_table_names) > 0:
		print "\n!!!CAUTION!!!\nFixing on below table failed!Need manually fix."
		for i in range(0,len(failed_table_names)):
			print failed_table_names[i]

	if len(table_names) > 0:	
		print "\nPlease drop backed up tables (below) manually!"
		for i in range(0,len(table_names)):
		#I have included ; on the end so that generated drop statemnts could be used
			print 'DROP TABLE "'+ _SCHEMA_ + '"."' +table_names[i]+'_BAK";'
		#cursor_db.execute("""drop table where table_name like '%_BAK'""")

	
	print ""
	print "See the log for more information. The log has written to " + file_dir
	print ""
else:
	print "No table need to be fixed."

cursor_db.close()
con_db.close()	