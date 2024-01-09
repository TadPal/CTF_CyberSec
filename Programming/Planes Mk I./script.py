from pwn import *
import json

c = remote("185.138.244.76", 9001)

line = json.loads(c.recvline().decode())
print(line.get("planes"))

c.close()