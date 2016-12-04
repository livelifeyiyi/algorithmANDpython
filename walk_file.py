import os
import re
path = 'E:\\(O_O)!\\learnSth'
def find_procedure(path):
    if os.path.isdir(path):
        for fpath,path,fnames in os.walk(path):
            for fname in fnames:
                fname_path = os.path.join(fpath,fname)
                fo = open(fname_path, 'r')
                text = fo.read()
                result = re.findall('create procedure', text, flags=re.IGNORECASE)
                
                #if "create procedure" in text:
                if result != []:
                    print fname_path
                #print os.path.join(fpath,fname)
                fo.close()
#find_procedure(path)
#print os.walk(path)

def calculate_bytes(path):
    for root, dirs, files in os.walk(path):
        print root, "consums",
        print sum(os.path.getsize(os.path.join(root,name)) for name in files),
        print "bytes in", len(files),"none-directory files"
calculate_bytes(path)