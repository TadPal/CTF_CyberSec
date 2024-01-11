import json
from pwn import *
from getData import get_data
from getFakeData import get_data as get_fake
from findPath import find_path
from time import time

# ts = time()

# planes, no_fly_zones, airports = get_fake()
# paths = []

# for plane in planes:
#     paths.append(find_path(plane, no_fly_zones, airports))

# print(f"It took {time()-ts} seconds")

com = remote("185.138.244.76", 9002)

while True:
    i = 0
    msg = ""
    end = False
    planes, no_fly_zones, airports, line = get_data(com)

    if planes is None:
        print(line)

    paths = []

    for plane in planes:
        paths.append(find_path(plane, no_fly_zones, airports))

    while True:
        ans = []

        for path in paths:
            ans += [path[i]]

        msg = ",".join(ans)
        msg = '{"type":"Command","command":[' + msg + "]}"
        com.sendline(msg.encode())

        msg = json.loads(com.recvline().decode())
        print(msg)

        if msg["type"] == "Error":
            end = True
            print(msg)
        elif msg["type"] == "End" or msg["type"] == "Flag":
            print(msg)
            break
        i += 1
    if end:
        break

com.close()
