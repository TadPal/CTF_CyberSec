import json
from pwn import *


def get_data(communication: remote):
    line = json.loads(communication.recvline().decode())

    if line["type"] == "Start":
        # with open("./Programming/PlanesMKI/sampleData.json", "r") as f:
        #     line = json.load(f)
        # with open("./Programming/PlanesMKI/sampleData.json", "w") as f:
        #     f.write(json.dumps(line))

        planes = line.get("planes")
        airports = line.get("airports")
        no_fly_zones = line.get("no_fly_zones")

        for i, plane in enumerate(planes):
            plane["target"] = airports[plane["target"]]
            plane.update({"id": i})
            planes[i] = plane

        return planes, no_fly_zones, airports, line
    else:
        return None, None, None, line
