import psycopg2
import time
import json


def write_to_db(timestamp,userName,device_name,detail_result):
  test_dict={}
  test_dict["detail_result"]={}
  test_dict["detail_result"]=detail_result
  


  try:
     connection = psycopg2.connect(user="iq2_admin",
                                    password="iq2_admin",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="iq2_data_pipeline")
     cursor = connection.cursor()

     print("Json is ",test_dict)

     postgres_insert_query = """ INSERT INTO healthdata \
     ( timestamp, "userName", device_name, detail_results) \
     VALUES (%s,%s,%s,%s)"""
     record_to_insert = (str(timestamp), userName, device_name,json.dumps(test_dict))
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

def extract_data_from_kinesis_stream(data_dict):
  print(type(data_dict))
  return data_dict["timestamp"],data_dict["userName"],data_dict["device_name"],data_dict["detail_result"]


def main():
  from boto import kinesis
  kinesis = kinesis.connect_to_region("us-east-2")
  shard_id = 'shardId-000000000000' #we only have one shard!
  shard_it = kinesis.get_shard_iterator("end-stream", shard_id, "LATEST")["ShardIterator"]

  while 1==1:
    out = kinesis.get_records(shard_it, limit=1)
    shard_it = out["NextShardIterator"]
    if len(out["Records"])>0:
      print(out["Records"][0]["Data"])
      data_dict=json.loads(out["Records"][0]["Data"])
      timestamp,userName,device_name,detail_result=extract_data_from_kinesis_stream(data_dict)
    # print(shard_it)    
      write_to_db(timestamp,userName,device_name,detail_result)
    time.sleep(0.1)


if __name__=="__main__":
  main()
