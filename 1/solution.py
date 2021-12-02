#!/usr/bin/python3

def data():
    file = open('input.txt')
    return list(map(lambda str: int(str.strip("\n")), file.readlines()))

def run():
    increases = 0
    lines = data()

    for i in range(len(lines) - 1):
        increases += 1 if lines[i] < lines[i+1] else 0

    return increases

print(run())
