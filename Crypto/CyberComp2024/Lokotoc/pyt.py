import base64

test = b"ctf{fake_flag}"
for _ in range(15):
    test = base64.b64encode(test)

# for _ in range(15):
#     test = base64.b64decode(test)
print(f"{test}")