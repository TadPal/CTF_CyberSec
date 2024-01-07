from pwn import xor
import binascii

with open("./Crypto/CyberComp2024/Lokotoc/output.txt") as f:
    encrypted_flag = binascii.unhexlify(f.readline().strip())
    encrypted_test = binascii.unhexlify(f.readline().strip())

test_string = b"Fakt dlouha zprava ktera nevim co rika"
blob = xor(encrypted_test, encrypted_flag)

flag = xor(blob, test_string[: len(encrypted_flag)])
print(f"{flag=}")

# Works if nonce is the same
