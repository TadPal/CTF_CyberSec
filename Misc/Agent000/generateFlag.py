with open("Misc/Agent000/bash.txt", "r") as f:
    lines = f.readlines()
    flag = ""
    for i, line in enumerate(lines):
        if i % 2 != 0:
            flag += chr(int(line))
    print(flag)