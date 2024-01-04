import os, random, json
from hashlib import sha256
from Crypto.Util.number import bytes_to_long
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

KEY = 42216996780082862919329905584502640654488977649427388128315738967444512602833
key = sha256(str(KEY).encode()).digest().hex()
print(key)