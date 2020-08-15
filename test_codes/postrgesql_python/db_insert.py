import psycopg2
import time
import json

test_dict={}
test_dict["ECG"]={}
test_dict["ECG"]["HeartRhythmString"]="normal"
test_dict["ECG"]["HeartRate"]=str(61)


try:
   connection = psycopg2.connect(user="iq2_admin",
                                  password="iq2_admin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="iq2_data_pipeline")
   cursor = connection.cursor()

   print("Json is ",test_dict)

   postgres_insert_query = """ INSERT INTO healthdata ( timestamp, "userName", device_name, detail_results) VALUES (%s,%s,%s,%s)"""
   record_to_insert = (str(int(time.time())), 'test', 'test_device',json.dumps(test_dict))
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
