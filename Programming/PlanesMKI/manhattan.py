import json
from pwn import *


def get_data():  # communication: remote
    # line = json.loads(communication.recvline().decode())
    # if line["type"] != "Start":
    #     print(line)
    with open("./Programming/PlanesMKI/sampleData.json", "r") as f:
        line = json.load(f)

    planes = line.get("planes")
    airports = line.get("airports")
    no_fly_zones = line.get("no_fly_zones")

    for i, plane in enumerate(planes):
        plane["target"] = airports[plane["target"]]
        plane.update({"id": i})
        planes[i] = plane
    return planes, no_fly_zones, airports


def find_path(plane):
    open_tiles = []
    closed_tiles = []

    def set_tile_value(tile_s, target):
        tile_s["value"]["h"] = max(
            [
                abs(tile_s["x"] - target["x"]),
                abs(tile_s["y"] - target["y"]),
            ]
        )
        tile_s["value"]["f"] = tile_s["value"]["h"] + tile_s["value"]["g"]
        return tile_s

    def find_adjecent_tiles(tile, target):
        def check_forbidden_tiles(tile_to_check):
            check = {"x": tile_to_check["x"], "y": tile_to_check["y"]}
            for zone in no_fly_zones:
                if check == zone:
                    return True
            for o_tile in open_tiles:
                if o_tile == check:
                    return True
            for c_tile in closed_tiles:
                if c_tile == check:
                    return True
            for a_tile in airports:
                if a_tile == check:
                    if check["x"] == target["x"] and check["x"] == target["y"]:
                        return False
                    return True
            return False

        op = []

        for i in range(6):
            new_tile = {"x": 0, "y": 0, "value": {"f": 0, "h": 0, "g": 0}}
            match i:
                case 0:
                    new_tile["x"] = tile["x"]
                    new_tile["y"] = tile["y"] + 1
                case 1:
                    new_tile["x"] = tile["x"]
                    new_tile["y"] = tile["y"] - 1
                case 2:
                    new_tile["x"] = tile["x"] + 1
                    new_tile["y"] = tile["y"]
                case 3:
                    new_tile["x"] = tile["x"] - 1
                    new_tile["y"] = tile["y"]
                case 4:
                    new_tile["x"] = tile["x"] + 1
                    new_tile["y"] = tile["y"] - 1
                case 5:
                    new_tile["x"] = tile["x"] - 1
                    new_tile["y"] = tile["y"] + 1

            if check_forbidden_tiles(new_tile):
                continue
            else:
                new_tile["value"]["g"] = tile["value"]["g"] + 1
                new_tile = set_tile_value(new_tile, target)
                op += [new_tile]

        return op

    def check_orientation(coord, index):
        if coord["x"] > path[index - 1]["x"] and coord["y"] == path[index - 1]["y"]:
            return '"E"'

        elif coord["x"] < path[index - 1]["x"] and coord["y"] == path[index - 1]["y"]:
            return '"W"'

        elif coord["x"] == path[index - 1]["x"] and coord["y"] > path[index - 1]["y"]:
            return '"NE"'

        elif coord["x"] == path[index - 1]["x"] and coord["y"] < path[index - 1]["y"]:
            return '"SW"'

        elif coord["x"] < path[index - 1]["x"] and coord["y"] > path[index - 1]["y"]:
            return '"NW"'

        elif coord["x"] > path[index - 1]["x"] and coord["y"] < path[index - 1]["y"]:
            return '"SE"'

    target = {"x": plane["target"]["x"], "y": plane["target"]["y"]}
    tile = set_tile_value(
        tile_s={"x": plane["x"], "y": plane["y"], "value": {"f": 0, "h": 0, "g": 0}},
        target=target,
    )

    closed_tiles += [tile]

    while True:
        open_tiles += find_adjecent_tiles(tile=tile, target=target)
        if len(open_tiles) == 0:
            break
        best_tile = open_tiles[-1]
        index = 0
        found = False

        for i, tile in enumerate(open_tiles):
            if tile["value"]["f"] < best_tile["value"]["f"]:
                best_tile = tile
                index = i
            if tile["value"]["h"] == 0:
                index = i
                open_tiles.pop(index)
                closed_tiles += [tile]
                found = True
                break

        if found:
            # print(closed_tiles)
            break

        for i, tl in enumerate(open_tiles):
            if best_tile["value"]["f"] == tl["value"]["f"]:
                if tl["value"]["g"] > best_tile["value"]["g"]:
                    best_tile = tl
                    index = i

        tile = best_tile
        open_tiles.pop(index)
        closed_tiles += [best_tile]

    current = closed_tiles[-1]
    closed_tiles.reverse()
    path = [current]
    while current["value"]["g"] != 0:
        for tile in closed_tiles:
            if current["value"]["g"] - tile["value"]["g"] == 1:
                if current["x"] + 1 == tile["x"] and current["y"] + 1 == tile["y"]:
                    continue
                elif current["x"] - 1 == tile["x"] and current["y"] - 1 == tile["y"]:
                    continue
                elif (
                    abs(current["x"] - tile["x"]) > 1
                    or abs(current["y"] - tile["y"]) > 1
                ):
                    continue

                path += [tile]
                current = tile
                break
    path.reverse()

    plane_path = []
    for i, coord in enumerate(path):
        if i == 0:
            continue
        plane_path += [check_orientation(coord, i)]

    if len(plane_path) > plane["fuel"]:
        print(f'{plane["fuel"]}')

    for i in range(100 - len(path)):
        plane_path += ['"E"']

    return plane_path


######################################################################################################
###                                         MAIN                                                   ###
######################################################################################################
# for _ in range(100):
# com = remote("185.138.244.76", 9001)

# print(paths)
# while True:
#     i = 0
#     msg = ""
#     end = False
#     planes, no_fly_zones, airports = get_data()
#     paths = []

#     for plane in planes:
#         paths += [find_path(plane)]

#     while True:
#         ans = []

#         for path in paths:
#             ans += [path[i]]

#         msg = ",".join(ans)
#         msg = '{"type":"Command","command":[' + msg + "]}"
#         com.sendline(msg.encode())

#         msg = json.loads(com.recvline().decode())

#         if msg["type"] == "Error":
#             end = True
#             print(msg)
#         elif msg["type"] == "End" or msg["type"] == "Flag":
#             print(msg)
#             break
#         i += 1
#     if end:
#         break
# com.close()
for i in range(30):
    msg = ""
    planes, no_fly_zones, airports = get_data()
    paths = []

    for plane in planes:
        paths += [find_path(plane)]

    ans = []

    for path in paths:
        ans += [path[i]]

    msg = ",".join(ans)
    msg = '{"type":"Command","command":[' + msg + "]}"
