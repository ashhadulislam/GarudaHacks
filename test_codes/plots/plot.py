# import numpy as np
# import matplotlib.pyplot as plt


# def update_line(hl, i, new_data):
#     hl.set_data(np.arange(i+1), new_data[:i+1])

# n_data = 2
n_iter = 100
# data = np.random.rand(n_data, n_iter)

# plt.figure()
# plt.xlabel("iter")
# plt.ylabel("cost")
# plt.axis([0, n_iter, 0, 1])

# cost_plots = []
# for i in range(n_data):
#     cost_plot, = plt.plot([], [])
#     cost_plots.append(cost_plot)

# for i in range(n_iter):
#     for j, cost_plot in enumerate(cost_plots):
#         update_line(cost_plot, i, data[j])
#     plt.draw()
#     plt.pause(0.1)


import json

import matplotlib.pyplot as plt
import numpy as np


def extract_data_from_kinesis_stream(data_dict):
  print(type(data_dict))
  return data_dict["timestamp"],data_dict["userName"],data_dict["device_name"],data_dict["detail_result"]


def update_values(x,y):
    last=x[-1]    
    x=np.insert(x,0,last+1)
    x=x[:-1]
    

    y=np.insert(y,0,x[0]+1)
    y=y[:-1]
    print("x=",x," y=",y)

    return x,y


def plot_vals(x1,y1,x2,y2):

    # Some example data to display
    



    # for i in range(n_iter):
        
        
        # x,y=update_values(x,y)
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Body Orientation and Steps')
    ax1.plot(x1, y1)
    ax2.plot(x2, y2)    
    plt.draw()
    plt.pause(0.1)


def main():
  from boto import kinesis
  kinesis = kinesis.connect_to_region("us-east-2")
  shard_id = 'shardId-000000000000' #we only have one shard!
  shard_it = kinesis.get_shard_iterator("end-stream", shard_id, "LATEST")["ShardIterator"]
  timestamps=[i for i in range(20)]
  bodyorientationpitches=[i for i in range(20)]
  steps=[i for i in range(20)]

  while 1==1:
    out = kinesis.get_records(shard_it, limit=1)
    shard_it = out["NextShardIterator"]
    if len(out["Records"])>0:
      print(out["Records"][0]["Data"])
      data_dict=json.loads(out["Records"][0]["Data"])
      timestamp,userName,device_name,detail_result=extract_data_from_kinesis_stream(data_dict)
      
      timestamps.insert(0,timestamp)
      timestamps=timestamps[:-1]
      
      bodyorientationpitches.insert(0,detail_result["IMU"]["BodyOrientationPitch"])
      bodyorientationpitches=bodyorientationpitches[:-1]
  
  
      steps.insert(0,detail_result["IMU"]["StepCount"])
      steps=steps[:-1]
  
      x1=np.array(timestamps)
      y1=np.array(bodyorientationpitches)
  
      x2=np.array(timestamps)
      y2=np.array(steps)
  
      plot_vals(x1,y1,x2,y2)




if __name__=="__main__":
    main()