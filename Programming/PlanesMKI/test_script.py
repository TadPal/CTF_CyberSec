d1 = {"x": 1, "y": 2}
d2 = {"x": 1, "y": 2, "values": {}}

print(d1 == d2)

s = (d1["x"], d1["y"])
print(type(s))
