from boto import kinesis
import time

kinesis = kinesis.connect_to_region("us-east-2")
shard_id = 'shardId-000000000000' #we only have one shard!
shard_it = kinesis.get_shard_iterator("end-stream", shard_id, "LATEST")["ShardIterator"]
while 1==1:
    out = kinesis.get_records(shard_it, limit=1)
    shard_it = out["NextShardIterator"]
    if len(out["Records"])>0:
    	print(out["Records"][0]["Data"])
    # print(shard_it)    
    time.sleep(0.3)




# {'MillisBehindLatest': 0, 
# 'NextShardIterator': 'AAAAAAAAAAFF9/mBhBuL7fpnx+/w6YomDqex3tSNgI9ZI57g7i92nH2A/yTng4OQSTOtYbSHzwy+KA32ezEV/32oAYrMfkRuDQnnIvJvbaTBCDZdQSJLL+UTZthKkGUNoSwh8iGEohXHZjnra1R/Ky2JQwD/RU/WyWKVxhnsGiyHfltq72rgQ5y5raMhI4i0XGrY6Cc3kK4Ieu8V0rikCfNVl7Pjz26n', 
# 'Records': 
# [
# 	{
# 	'ApproximateArrivalTimestamp': 1597406867.724, 
# 	'Data': '{"deviceID": 59, "userName": "user59", "timeStamp": 1597406867, "param1": 9, "param2": 7, "param3": 2, "param4": 9}', 'PartitionKey': 'partitionkey', 'SequenceNumber': '49609830172400645887225606482176990396391791989677359106'}]}