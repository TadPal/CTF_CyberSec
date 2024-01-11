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
        airports_dict = line.get("airports")
        no_fly_zones_dict = line.get("no_fly_zones")

        airports = [(airport["x"], airport["y"]) for airport in airports_dict]

        no_fly_zones = [
            (no_fly_zone["x"], no_fly_zone["y"]) for no_fly_zone in no_fly_zones_dict
        ]
        no_fly_zones.sort(key=lambda x: x[0])

        for i, plane in enumerate(planes):
            plane["target"] = airports[plane["target"]]
            plane.update({"id": i})
            planes[i] = plane

        airports.sort(key=lambda x: x[0])

        return planes, no_fly_zones, airports, line
    else:
        return None, None, None, line
