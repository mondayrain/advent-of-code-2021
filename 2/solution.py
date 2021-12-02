#!/usr/bin/python3
from functools import reduce

def data():
    file = open('input.txt')
    return list(map(lambda str: str.strip("\n"), file.readlines()))

def reducer(position, movement):
    direction, amount = movement.split(" ")

    if direction == "forward":
        return (position[0] + int(amount), position[1])
    else:
        return (position[0], position[1] + int(amount)) if direction == "down" else (position[0], position[1] - int(amount))

def run():
    positions = data()
    horizontal, depth = reduce(reducer, positions, (0, 0))
    return horizontal * depth

print(run())