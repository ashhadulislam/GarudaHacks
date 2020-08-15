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


# stream = kinesis.create_stream("BotoDemo", 1)
# print(kinesis.describe_stream("BotoDemo"))


def get_range_heart_rate(rhythm_index):
    if rhythm_index==0:
        start=100
        stop=140
    elif rhythm_index==1:
        start=100
        stop=200
    elif rhythm_index==2:
        start=80
        stop=110
    elif rhythm_index==3:
        start=30
        stop=60
    elif rhythm_index==4:
        start=0
        stop=30
    elif rhythm_index==5:
        start=60
        stop=100

    return start,stop


# list_measure_groups=["IMU","GSR","NIRS","Temperature","ECG","PPG","Microphone_Audio"]
list_measure_groups=["IMU","GSR","ECG"]
device_name=["headband","fitbit","chest_mount"]

# seed random number generator
seed(1)
if len(sys.argv)>1:
    index=int(sys.argv[1])

# for i in range(500):
i=0
while 1==1:

    new_dict={}    
    
    new_dict["timestamp"]=int(time.time())        

    if len(sys.argv)==1:
        index=randint(0,10)%3
    # index=0

    new_dict["userName"]="user"+str(index+1)
    new_dict["device_name"]=device_name[index]




    if index==0:
        # "IMU"
        new_dict["detail_result"]={}
        new_dict["detail_result"][list_measure_groups[index]]={}
        new_dict["detail_result"][list_measure_groups[index]]["StepCount"]=randint(0,10)
        new_dict["detail_result"][list_measure_groups[index]]["BodyOrientationPitch"]=randint(0,180)
        new_dict["detail_result"][list_measure_groups[index]]["BodyOrientationRoll"]=randint(0,180)
        items=["upright","flat","inverted"]        
        new_dict["detail_result"][list_measure_groups[index]]["BodyOrientationString"]=items[random.randrange(len(items))]
        new_dict["detail_result"][list_measure_groups[index]]["BreathRate"]=randint(0,100)
    elif index==1:
        # "GSR"
        new_dict["detail_result"]={}
        new_dict["detail_result"][list_measure_groups[index]]={}
        new_dict["detail_result"][list_measure_groups[index]]["SkinConductance"]=randint(0,10)
        new_dict["detail_result"][list_measure_groups[index]]["SweatRate"]=random.uniform(0, 5)        
        items=["high","low","moderate"]        
        new_dict["detail_result"][list_measure_groups[index]]["SweatRateString"]=items[random.randrange(len(items))]
    elif index==2:
        # "ECG"
        new_dict["detail_result"]={}
        new_dict["detail_result"][list_measure_groups[index]]={}
        items=["tachycardia","atrial_fibrillation","atrial_flutter","bradycardia","ventricular_fibrillation","normal"]        
        rhythm_index=random.randrange(len(items))
        new_dict["detail_result"][list_measure_groups[index]]["HeartRhythmString"]=items[rhythm_index]
        start,stop = get_range_heart_rate(rhythm_index)        
        new_dict["detail_result"][list_measure_groups[index]]["HeartRate"]=random.randint(start, stop)



    print("loading ",json.dumps(new_dict))
    kinesis.put_record("end-stream", json.dumps(new_dict), "partitionkey")    
    time.sleep(0.2)


