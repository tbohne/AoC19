import sys

def manhattan_dist(x, y):
    return abs(0 - x) + abs(0 - y)

if __name__ == '__main__':

    data = sys.stdin.readlines()
    wires = [wire.strip() for wire in data]

    wire_points = {}
    wire_points["ONE"] = []
    wire_points["TWO"] = []
    visited = {}
    visited["ONE"] = {}
    visited["TWO"] = {}

    wireIdx = "ONE"

    for wire in wires:

        x = y = 0
        step_cnt = 0

        for command in wire.split(","):

            direction = command[0]
            steps = int(command[1:])

            for _ in range(steps):
                if direction == "U":
                    y -= 1
                elif direction == "D":
                    y += 1
                elif direction == "L":
                    x -= 1
                elif direction == "R":
                    x += 1

                step_cnt += 1

                if (x, y) not in visited[wireIdx]:
                    visited[wireIdx][(x, y)] = step_cnt
                wire_points[wireIdx].append((x, y))

        wireIdx = "TWO"

    intersections = list(set(wire_points["ONE"]) & set(wire_points["TWO"]))
    part_one = min([int(manhattan_dist(pt[0], pt[1])) for pt in intersections])
    part_two = min([visited["ONE"][inter] + visited["TWO"][inter] for inter in intersections])
    print("p1: " + str(part_one))
    print("p2: " + str(part_two))
