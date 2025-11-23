import os
import time


def readInput():
    with open("input.txt","r") as file:
        return file.read()

def getGuardPos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in ['v','^','>','<']:
                return i,j
    return None

def printGrid(grid):
    print("\033[H\033[3J", end="")
    for i in range(len(grid)):
        txt = ""
        for j in range(len(grid[i])):
            txt += grid[i][j]
        print(txt)
    print()
    print("-" * 20)
    print()

def moveGuard(grid):
    guardPos = getGuardPos(grid)
    guardDir = grid[guardPos[0]][guardPos[1]]
    if guardDir == "v":
        if guardPos[0] >= len(grid)-2:
            grid[guardPos[0]][guardPos[1]] = "X"
            printGrid(grid)
            return
        if grid[guardPos[0]+1][guardPos[1]] == "#":
            grid[guardPos[0]][guardPos[1]] = "<"
            printGrid(grid)
            return
        grid[guardPos[0]][guardPos[1]] = "X"
        grid[guardPos[0]+1][guardPos[1]] = "v"
    elif guardDir == "^":
        if guardPos[0] == 0:
            grid[guardPos[0]][guardPos[1]] = "X"
            printGrid(grid)
            return

        if grid[guardPos[0]-1][guardPos[1]] == "#":
            grid[guardPos[0]][guardPos[1]] = ">"
            printGrid(grid)
            return
        grid[guardPos[0]][guardPos[1]] = "X"
        grid[guardPos[0]-1][guardPos[1]] = "^"
    elif guardDir == ">":
        if guardPos[1] == len(grid[0]) - 1:
            grid[guardPos[0]][guardPos[1]] = "X"
            printGrid(grid)
            return

        if grid[guardPos[0]][guardPos[1]+1] == "#":
            grid[guardPos[0]][guardPos[1]] = "v"
            printGrid(grid)
            return
        grid[guardPos[0]][guardPos[1]] = "X"
        grid[guardPos[0]][guardPos[1]+1] = ">"
    elif guardDir == "<":
        if guardPos[1] == 0:
            grid[guardPos[0]][guardPos[1]] = "X"
            printGrid(grid)
            return

        if grid[guardPos[0]][guardPos[1]-1] == "#":
            grid[guardPos[0]][guardPos[1]] = "^"
            printGrid(grid)
            return
        grid[guardPos[0]][guardPos[1]] = "X"
        grid[guardPos[0]][guardPos[1]-1] = "<"
    printGrid(grid)


if __name__ == "__main__":
    content = [list(line) for line in readInput().split("\n")]
    printGrid(content)

    while getGuardPos(content) is not None:
        moveGuard(content)
        time.sleep(0.005)

    sum = 0
    for i in range(len(content)-1):
        for j in range(len(content[0])-1):
            if content[i][j] == "X":
                sum += 1

    print(sum)
    while True:
        pass