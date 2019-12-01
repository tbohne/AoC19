import sys
import math

def part_one():
    fuel_vals = [math.floor(int(mass.strip()) / 3) - 2 for mass in data]
    print("p1: " + str(sum(fuel_vals)))

def part_two():
    total_fuel = 0
    for mass in data:
        fuel = math.floor(int(mass.strip()) / 3) - 2
        while fuel > 0:
            total_fuel += fuel
            fuel = math.floor(fuel / 3) - 2
    print("p2: " + str(total_fuel))

if __name__ == '__main__':
    data = sys.stdin.readlines()
    part_one()
    part_two()
