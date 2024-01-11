import json
from pwn import *


def get_data():
    with open("./Programming/PlanesMKI/sampleData.json", "r") as f:
        line = json.load(f)
    #   with open("./Programming/PlanesMKI/sampleData.json", "w") as f:
    #       f.write(json.dumps(line))

    planes = line.get("planes")
    airports_dict = line.get("airports")
    no_fly_zones_dict = line.get("no_fly_zones")

    airports = [(airport["x"], airport["y"]) for airport in airports_dict]
    airports.sort(key=lambda x: x[0])

    no_fly_zones = [
        (no_fly_zone["x"], no_fly_zone["y"]) for no_fly_zone in no_fly_zones_dict
    ]
    no_fly_zones.sort(key=lambda x: x[0])

    for i, plane in enumerate(planes):
        plane["target"] = airports[plane["target"]]
        plane.update({"id": i})
        planes[i] = plane

    return planes, no_fly_zones, airports
