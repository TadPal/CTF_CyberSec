from time import time


def find_path(plane, no_fly_zones, airports):
    open_tiles = []
    closed_tiles = []
    path = []

    def set_tile_value(tile, target):
        tile["value"]["h"] = max(
            [
                abs(tile["x"] - target[0]),
                abs(tile["y"] - target[1]),
            ]
        )
        if tile["x"] - target[0] == tile["y"] - target[1]:
            tile["value"]["h"] = tile["value"]["h"] + abs(tile["x"] - target[0])

        tile["value"]["f"] = tile["value"]["h"] + tile["value"]["g"]

    def check_orientation(position, index, path):
        if (
            position["x"] > path[index - 1]["x"]
            and position["y"] == path[index - 1]["y"]
        ):
            return '"E"'

        elif (
            position["x"] < path[index - 1]["x"]
            and position["y"] == path[index - 1]["y"]
        ):
            return '"W"'

        elif (
            position["x"] == path[index - 1]["x"]
            and position["y"] > path[index - 1]["y"]
        ):
            return '"NE"'

        elif (
            position["x"] == path[index - 1]["x"]
            and position["y"] < path[index - 1]["y"]
        ):
            return '"SW"'

        elif (
            position["x"] < path[index - 1]["x"]
            and position["y"] > path[index - 1]["y"]
        ):
            return '"NW"'

        elif (
            position["x"] > path[index - 1]["x"]
            and position["y"] < path[index - 1]["y"]
        ):
            return '"SE"'

    def find_adjecent_tiles(tile, last_tile):
        open_list = []
        new_tile = {}
        isFinal = False

        # Check all hexagonal neighbors
        for i in range(6):
            add = True
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

            cmp = (new_tile["x"], new_tile["y"])

            # Check if tile isn't forbidden
            if cmp == target:
                isFinal = True

            if isFinal:
                new_tile["value"]["g"] = tile["value"]["g"] + 1
                set_tile_value(new_tile, last_tile)
                open_list += [new_tile]
                return open_list

            for airport in airports:
                if cmp == airport:
                    add = False
                    break
            if add:
                for i, c_tile in enumerate(closed_tiles):
                    if new_tile["x"] == c_tile["x"] and new_tile["y"] == c_tile["y"]:
                        add = False
                        break
            if add:
                for o_tile in open_tiles:
                    if new_tile["x"] == o_tile["x"] and new_tile["y"] == o_tile["y"]:
                        add = False
                        break
            if add:
                for zone in no_fly_zones:
                    if cmp == zone:
                        add = False
                        break

            # If it is not forbidden add it to the open list
            if add:
                new_tile["value"]["g"] = tile["value"]["g"] + 1
                set_tile_value(new_tile, last_tile)
                open_list += [new_tile]

        return open_list

    ###########################################################################
    ################################    MAIN    ###############################
    ###########################################################################

    # Initial plane state
    target = (plane["target"][0], plane["target"][1])
    initial_direction = plane["direction"]
    tile = {"x": plane["x"], "y": plane["y"], "value": {"f": 0, "h": 0, "g": 0}}
    set_tile_value(tile=tile, target=target)

    # Add first tile to closed_tiles
    closed_tiles += [tile]

    # Until last tile is found
    while True:
        open_tiles += find_adjecent_tiles(tile, target)
        open_tiles.sort(key=lambda x: x["value"]["f"])

        best_tile = open_tiles[0]
        index = 0
        found = False

        for i, op_tile in enumerate(open_tiles):
            if op_tile["value"]["h"] == 0:
                open_tiles.pop(index)
                closed_tiles += [op_tile]
                found = True
                break
        if found:
            break

        for i, tl in enumerate(open_tiles):
            if best_tile["value"]["f"] == tl["value"]["f"]:
                if best_tile["value"]["g"] < tl["value"]["g"]:
                    best_tile = tl
                    index = i
            if best_tile["value"]["f"] < tl["value"]["f"]:
                break

        tile = best_tile
        open_tiles.pop(index)
        closed_tiles += [best_tile]

    ####################################################
    ################### BACKTRACKING ###################
    ####################################################
    closed_tiles.sort(key=lambda x: x["value"]["g"], reverse=True)
    backtrack = closed_tiles[0]
    path = [backtrack]

    while backtrack["value"]["g"] != 0:
        for i, cl_tile in enumerate(closed_tiles):
            if backtrack["value"]["g"] - cl_tile["value"]["g"] == 1:
                # Check if tile is adjecent
                if (
                    backtrack["x"] + 1 == cl_tile["x"]
                    and backtrack["y"] + 1 == cl_tile["y"]
                ):
                    continue
                elif (
                    backtrack["x"] - 1 == cl_tile["x"]
                    and backtrack["y"] - 1 == cl_tile["y"]
                ):
                    continue
                elif (
                    abs(backtrack["x"] - cl_tile["x"]) > 1
                    or abs(backtrack["y"] - cl_tile["y"]) > 1
                ):
                    continue

                path += [cl_tile]
                backtrack = cl_tile
                closed_tiles.pop(i)
                break

    path.reverse()

    plane_path = []
    for i, position in enumerate(path):
        if i == 0:
            continue
        plane_path += [check_orientation(position, i, path)]

    for i in range(100 - len(path)):
        plane_path += ['"E"']

    return plane_path
