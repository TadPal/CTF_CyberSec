from pwn import *

# Connect to the server
conn = remote("185.138.244.76", 7161)

conn.recvlines(11, keepends=True)

# Send the numbers '1', '2', '3', '31337' as ASCII
for i in range(1, 4):
    conn.sendline(str(i))
    conn.recvlines(2, keepends=True)

conn.sendline(str(31337))
conn.recvlines(4, keepends=True)

conn.send(struct.pack('<Q', 1))  # Send packed integer '1'
conn.recvline()
conn.recvline()

conn.send(struct.pack('<Q', 2))  # Send packed integer '2'
conn.recvline()
conn.recvline()

conn.send(struct.pack('<Q', 3))  # Send packed integer '3'
conn.recvline()
conn.recvline()

conn.send(struct.pack('<Q', 31337))  # Send packed integer '31337'
conn.recvline()
conn.recvline()

conn.send(struct.pack('<Q', 287495273150))  # Send packed integer '287495273150'
conn.recvlines(3)

conn.recvall()