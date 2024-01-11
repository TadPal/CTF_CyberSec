from pwn import *
import json

c = remote("185.138.244.76", 9001)

line = json.loads(c.recvline().decode())
print(line.get("planes"))

c.sendline(
    b'{"type":"Command","command":["NW", "NE", "NW", "NE", "NE", "NW", "SE", "NE", "NW", "NW", "NW", "SW", "NW", "NE", "NE", "SE", "SE", "NW", "NW", "NW", "NE", "SW", "NE", "SE", "NE", "NW", "NW", "SW", "NW", "NE"]}'
)

print(c.recvline().decode())
c.close()
