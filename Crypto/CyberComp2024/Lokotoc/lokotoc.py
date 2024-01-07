#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii
import base64
import os


if not "FLAG" in os.environ:
    print(
        "Varovani: V environmentu neni FLAG, budu pouzivat ctf{fake_flag}. Pokud jsi tuto zpravu dostal od naseho serveru, nahlas to organizatorum!"
    )
    FLAG = b"ctf{fake_flag}"
else:
    FLAG = os.environ["FLAG"].encode()

# for i in range(15):
# 	FLAG = base64.b64encode(FLAG) # nafoukneme vlajku

key = os.urandom(32)  # AES-256 je bezpecnejsi nez AES-128
used_nonces = set()

print("Vitejte na nasem lokotoci!")
while 1:
    print("1. Zasifrovat zpravu")
    print("2. Zasifrovat vlajku")

    try:
        inp = int(input("Moznost: "))
        if inp not in [1, 2]:
            raise Exception()
    except:
        print("Skill issue..")
        break

    if inp == 1:
        plain = input("Plaintext k zasifrovani: ").encode()

    elif inp == 2:
        plain = FLAG

    try:
        nonce = int(input("Nonce: "))
        if nonce in used_nonces:  # nonce musi byt pouzita jen jednou
            raise Exception()
        used_nonces.add(nonce)
    except:
        print("Skill issue..")
        break
    ctr = Counter.new(128, initial_value=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    enc = cipher.encrypt(plain)

    print(binascii.hexlify(enc).decode())
