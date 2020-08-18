# import testdata
import json
from boto import kinesis
import sys

# seed the pseudorandom number generator
from random import seed
from random import randint
import time
import random

kinesis = kinesis.connect_to_region("us-east-2")
print(kinesis.list_streams())

seed(1)

i=0
while 1==1:

    new_dict={}    
    new_dict["timestamp"]=int(time.time())        
    new_dict["dataNum"]="data"+str(i)
    new_dict["device_name"]="dev"
    new_dict["HeartRate"]=random.randint(60, 120)

    print("loading ",json.dumps(new_dict))
    kinesis.put_record("end-stream", json.dumps(new_dict), "partitionkey")    
    time.sleep(0.2)
    i+=1


