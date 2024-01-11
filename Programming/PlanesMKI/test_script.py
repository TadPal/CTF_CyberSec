import json

# sample: {"type":"Command","command":["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","NW","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","W","E","E","E","E","E","E","E"]}


def get_data():
    with open("./Programming/PlanesMKI/sampleData.json") as f:
        line = json.load(f)

    planes = line.get("planes")
    airports = line.get("airports")
    no_fly_zones = line.get("no_fly_zones")

    for i, plane in enumerate(planes):
        plane["target"] = airports[plane["target"]]
        plane.update({"last_pos": {"x": 0, "y": 0}})
        plane.update({"id": i})
        planes[i] = plane
    return planes, no_fly_zones


def generate_move_json(planes, no_fly_zones):
    moves = []

    def check_no_fly(plane: dict, intended_move: str):
        def check_move_allowed(x=0, y=0):
            allowed = True
            x_check = plane["x"] + x
            y_check = plane["y"] + y
            for zone in no_fly_zones:
                if (x_check == zone["x"] and y_check == zone["y"]) or (
                    x_check == plane["last_pos"]["x"]
                    and y_check == plane["last_pos"]["y"]
                ):
                    allowed = False
                    break
            return allowed

        def avoid_obstacle(intended_move: str):
            return '"X"'

        def set_last_pos():
            planes[plane["id"]]["last_pos"] = {
                "x": planes[plane["id"]]["x"],
                "y": planes[plane["id"]]["y"],
            }

        while True:
            match intended_move:
                case '"W"':
                    if check_move_allowed(x=-1):
                        set_last_pos()
                        planes[plane["id"]]["last_pos"] = {
                            "x": planes[plane["id"]]["x"],
                            "y": planes[plane["id"]]["y"],
                        }
                        planes[plane["id"]]["x"] -= 1
                        return intended_move
                    return avoid_obstacle('"W"')

                case '"E"':
                    if check_move_allowed(x=1):
                        set_last_pos()
                        planes[plane["id"]]["x"] += 1
                        return intended_move
                    return avoid_obstacle('"E"')

                case '"NW"':
                    if check_move_allowed(x=-1, y=1):
                        set_last_pos()
                        planes[plane["id"]]["x"] -= 1
                        planes[plane["id"]]["y"] += 1
                        return intended_move
                    return avoid_obstacle('"NW"')

                case '"NE"':
                    if check_move_allowed(y=1):
                        set_last_pos()
                        planes[plane["id"]]["y"] += 1
                        return intended_move
                    return avoid_obstacle('"NE"')

                case '"SE"':
                    if check_move_allowed(x=1, y=-1):
                        set_last_pos()
                        planes[plane["id"]]["x"] += 1
                        planes[plane["id"]]["y"] -= 1
                        return intended_move
                    return avoid_obstacle('"SE"')

                case '"SW"':
                    if check_move_allowed(y=-1):
                        set_last_pos()
                        planes[plane["id"]]["y"] -= 1
                        return intended_move
                    return avoid_obstacle('"SW"')

                case _:
                    print("YOU FUCKED UP")
                    return '"X"'

    for plane in planes:
        if plane["target"]["x"] == plane["x"] and plane["target"]["y"] == plane["y"]:
            moves = moves + ['"A"']
            continue

        if plane["target"]["x"] > plane["x"] and plane["target"]["y"] == plane["y"]:
            move = check_no_fly(plane, '"E"')

        elif plane["target"]["x"] < plane["x"] and plane["target"]["y"] == plane["y"]:
            move = check_no_fly(plane, '"W"')

        elif plane["target"]["x"] == plane["x"] and plane["target"]["y"] > plane["y"]:
            move = check_no_fly(plane, '"NE"')

        elif plane["target"]["x"] > plane["x"] and plane["target"]["y"] < plane["y"]:
            move = check_no_fly(plane, '"SE"')

        elif plane["target"]["x"] < plane["x"] and plane["target"]["y"] > plane["y"]:
            move = check_no_fly(plane, '"NW"')

        elif plane["target"]["x"] == plane["x"] and plane["target"]["y"] < plane["y"]:
            move = check_no_fly(plane, '"SW"')

        elif plane["target"]["x"] > plane["x"] and plane["target"]["y"] > plane["y"]:
            move = check_no_fly(plane, '"W"')

        else:
            move = check_no_fly(plane, '"E"')

        plane["fuel"] -= 1
        moves = moves + [move]

        # plane_reached = (plane["x"] == plane["target"]["x"]) and (
        #     plane["y"] == plane["target"]["y"]
        # )

        # if plane_reached:
        #     print(plane["fuel"])

    moves = ",".join(moves)
    return '{"type":"Command","command":[' + moves + "]}"


planes, no_fly_zones = get_data()

for _ in range(55):
    generate_move_json(planes, no_fly_zones)

print(generate_move_json(planes, no_fly_zones))
print(planes[4])
