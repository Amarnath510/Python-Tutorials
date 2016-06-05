import time

time_t = time.localtime(time.time())
print(time_t)

time_normal = time.asctime(time.localtime(time.time()))
print(time_normal)