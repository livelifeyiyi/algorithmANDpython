#!/usr/bin/python

import threading
import time
import ConfigParser
import os
import conn_db
import logging
import argparse

file_dir = './log.txt'

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt = '%a,%d %b %Y %H:%M:%S',
                    filename = file_dir,
                    filemode = 'w')


class Thread(threading.Thread):
    def __init__(self,threadID, name, scripts, duration_time, think_time):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.scripts = scripts
        self.duration_time = duration_time
        self.think_time = think_time
    def run(self):
        
        print "Start " + self.name
        execute_sql(self.scripts, self.think_time, self.duration_time,self.name)
        db_con.commit()
        print "End " + self.name

def execute_sql(scripts,think_time,duration_time, thread_name):
    path = "./script/"+scripts
    filelist = os.listdir(path)
    t0 = time.time()
    t = t0
    while (t - t0) <= float(duration_time):
        #db_con = conn_db.conn_db(db_type,db_user,db_pwd,db_address,db_port,db_name)
        cursor_db = db_con.cursor()
        for filename in filelist:
            logging.info("Open file %s ----by thread %s"% (path +filename, thread_name))
            fo = open(path +filename, "r")
            sql_statements = fo.read()
            fo.close()
            print "Executing sql statement ..."
            sql_statement = sql_statements.split(";\n")
            for i in range(0,len(sql_statement)):
                logging.info("EXECUTING SQL: %s ----by thread %s"% (sql_statement[i], thread_name))
                cursor_db.execute(sql_statement[i])
                #print cursor_db.rowcount
                if(cursor_db.rowcount > 0):
                    result = cursor_db.fetchall()
                    for row in result:
                        print thread_name+"|"+str(row)
        cursor_db.close()
        #db_con.commit()
        #db_con.close()
        time.sleep(float(think_time))
        t = time.time()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read from the configure file, connect specific database and execute sql statements.')
    parser.add_argument("configure_filename", nargs='?',
                        help='The configure file name to read from, default:conf.ini')
    args = parser.parse_args()
    #if len(args) == 0:
    if args.configure_filename is None:
        args.configure_filename = 'conf.ini'
    
    conf = ConfigParser.ConfigParser()
    #conf.read("conf.ini")
    conf.read("./conf/%s"%args.configure_filename)
    sections = conf.sections()
    for i in sections:
        options = conf.options(i)
        value=conf.items(i)
    
    db_address = conf.get("DB_connection","DBaddress")
    db_port = conf.get("DB_connection","DBport")
    db_user = conf.get("DB_connection","DBuser")
    db_pwd = conf.get("DB_connection","DBpassword")
    db_name = conf.get("DB_connection","DBname")
    db_type = conf.get("DB_type","DB")
    thread_num = conf.get("threads_number","Threads_num")
    scripts = conf.get("script_folder_name","Scripts")
    duration_time = conf.get("duration_time","Duration")
    think_time = conf.get("think_time","Think")
    
    logging.info("Reading configure file...")
    #print db_type,thread_num,scripts,duration_time,think_time,db_address,db_port,db_user,db_pwd
    db_con = conn_db.conn_db(db_type,db_user,db_pwd,db_address,db_port,db_name)
    #db_con.autocommit(1)
    for i in range(0,int(thread_num)):
        thread = Thread(i, "Thread"+str(i), scripts, duration_time, think_time)
        thread.start()
        

