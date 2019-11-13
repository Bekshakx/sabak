import time
print (time.time())
start_time=time.time()
for i in range(10):
     i+=1
     time.sleep(2)
end_time=time.time()
delta=end_time-start_time
print(delta)