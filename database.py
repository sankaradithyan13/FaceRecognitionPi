import json
import re
import time
import MySQLdb
nonspace =re.compile(r'\S')

def iterparse(data):
    decoder = json.JSONDecoder()
    pos=0;
    while True:
        matched = nonspace.search(data,pos)
        if not matched:
            break
        pos = matched.start()
        decoded, pos = decoder.raw_decode(data,pos)
        yield decoded
    
def data_base(label,count):
    date = time.strftime("%d:%m:%y")
    name = date + 'a.json'
    print name
    
    with open(name,'a') as out_file:
        if label is 0:
            data = [{'ID ': label, 'Name' : 'Shubham', 'Time':time.strftime("%H:%M:%S")}]
            json.dump(data,out_file,indent=3)
        elif label is 1:
            data = [{'ID ': label, 'Name' : 'Sankar', 'Time':time.strftime("%H:%M:%S")}]
            json.dump(data,out_file,indent=3)
        elif label is 2:
            data = [{'ID ': label, 'Name' : 'Apurv', 'Time':time.strftime("%H:%M:%S")}]
            json.dump(data,out_file,indent=3)
        elif label is 3:
            data = [{'ID ': label, 'Name' : 'Rahul', 'Time':time.strftime("%H:%M:%S")}]
            json.dump(data,out_file,indent=3)
        elif label is 4:
            data = [{'ID ': label, 'Name' : 'Kirti', 'Time':time.strftime("%H:%M:%S")}]
            json.dump(data,out_file,indent=3)
        elif label is 5:
            data = [{'ID ': label, 'Name' : 'Prof.Lokhande', 'Time':time.strftime("%H:%M:%S")}]
            json.dump(data,out_file,indent=3)
            
    with open(name,'r') as out_file:
        out = list(iterparse(out_file.read()))
        print out[count]
