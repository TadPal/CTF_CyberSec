import json
from pwn import *
from getData import get_data
from getFakeData import get_data as get_fake
from findPath import find_path
import threading

planes, no_fly_zones, airports = get_fake()
paths1 = []
paths2 = []


def get_paths(planes, no_fly_zones, airports, result):
    for plane in planes:
        result.append(find_path(plane, no_fly_zones, airports))


index = int(len(planes) / 2)
planes1 = planes[:index]
planes2 = planes[index:]

t1 = threading.Thread(target=get_paths, args=(planes1, no_fly_zones, airports, paths1))
t2 = threading.Thread(target=get_paths, args=(planes2, no_fly_zones, airports, paths2))

t1.start()
t2.start()

t1.join()
t2.join()

paths = paths1 + paths2

print(paths)

# com = remote("185.138.244.76", 9002)

# while True:
#     i = 0
#     msg = ""
#     end = False
#     planes, no_fly_zones, airports, line = get_data(com)

#     if planes is None:
#         print(line)

#     paths = []

#     for plane in planes:
#         paths.append(find_path(plane, no_fly_zones, airports))

#     while True:
#         ans = []

#         for path in paths:
#             ans += [path[i]]

#         msg = ",".join(ans)
#         msg = '{"type":"Command","command":[' + msg + "]}"
#         com.sendline(msg.encode())

#         msg = json.loads(com.recvline().decode())
#         print(msg)

#         if msg["type"] == "Error":
#             end = True
#             print(msg)
#         elif msg["type"] == "End" or msg["type"] == "Flag":
#             print(msg)
#             break
#         i += 1
#     if end:
#         break
# com.close()
