import logging
file_dir = './log.txt'

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt = '%a,%d %b %Y %H:%M:%S',
                    filename = file_dir,
                    filemode = 'w')

logging.info("info")       
##multi_thread
 import thread 
 import time 
 import logging 
 import logging.config 
 logging.config.fileConfig('logging.conf') 
 # create logger 
 logger = logging.getLogger('simpleExample') 
 # Define a function for the thread 
 def print_time( threadName, delay): 
	 logger.debug('thread 1 call print_time function body') 
	 count = 0 
	 logger.debug('count:%s',count)    