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
            grid[guardPos[0]][guardPos[1]] = "|"
            printGrid(grid)
            return
        if grid[guardPos[0]+1][guardPos[1]] == "#":
            grid[guardPos[0] + 1][guardPos[1]] = "O"
            grid[guardPos[0]][guardPos[1]] = "<"
            printGrid(grid)
            return
        grid[guardPos[0]][guardPos[1]] = "|"
        grid[guardPos[0]+1][guardPos[1]] = "v"
    elif guardDir == "^":
        if guardPos[0] == 0:
            grid[guardPos[0]][guardPos[1]] = "|"
            printGrid(grid)
            return

        if grid[guardPos[0]-1][guardPos[1]] == "#":
            grid[guardPos[0] - 1][guardPos[1]] = "O"
            grid[guardPos[0]][guardPos[1]] = ">"
            printGrid(grid)
            return
        grid[guardPos[0]][guardPos[1]] = "|"
        grid[guardPos[0]-1][guardPos[1]] = "^"
    elif guardDir == ">":
        if guardPos[1] == len(grid[0]) - 1:
            grid[guardPos[0]][guardPos[1]] = "-"
            printGrid(grid)
            return

        if grid[guardPos[0]][guardPos[1]+1] == "#":
            grid[guardPos[0]][guardPos[1] + 1] = "O"
            grid[guardPos[0]][guardPos[1]] = "v"
            printGrid(grid)
            return
        grid[guardPos[0]][guardPos[1]] = "-"
        grid[guardPos[0]][guardPos[1]+1] = ">"
    elif guardDir == "<":
        if guardPos[1] == 0:
            grid[guardPos[0]][guardPos[1]] = "-"
            printGrid(grid)
            return

        if grid[guardPos[0]][guardPos[1]-1] == "#":
            grid[guardPos[0]][guardPos[1] - 1] = "O"
            grid[guardPos[0]][guardPos[1]] = "^"
            printGrid(grid)
            return
        grid[guardPos[0]][guardPos[1]] = "-"
        grid[guardPos[0]][guardPos[1]-1] = "<"
    printGrid(grid)


if __name__ == "__main__":
    content = [list(line) for line in readInput().split("\n")]
    printGrid(content)

    while getGuardPos(content) is not None:
        moveGuard(content)
        time.sleep(0.005)

    obstacles = []
    for i in range(len(content)-1):
        for j in range(len(content)-1):
            if content[i][j] == "O":
                obstacles.append((i,j))

    print(obstacles)
    print(len(obstacles))

    obstacleCombinations = []
    for fst in obstacles:
       for snd in obstacles:
            for third in obstacles:
                if fst == snd or fst == third or snd == third:
                    continue
                obstacleCombinations.append((fst, snd, third))

    print(len(obstacleCombinations))

    obstacleRectangles = []
    for obstacles in obstacleCombinations:
        fst,snd,third = obstacles[0],obstacles[1],obstacles[2]

        if fst[0] == snd[0]-1 and  snd[1] > fst[1] and third[1] == snd[1]-1 and third[0] > snd[0]:
            obstacleRectangles.append(obstacles)
        elif snd[1] == fst[1]-1 and snd[0] > fst[0] and third[0] == snd[0]-1 and third[1] < snd[1]:
            obstacleRectangles.append(obstacles)
        elif snd[0] == fst[0]-1 and snd[1] < fst[1] and third[1] == snd[1]+1 and third[0] < fst[0]:
            obstacleRectangles.append(obstacles)
        elif snd[1] == fst[1]+1 and snd[0] < fst[0] and third[0] == snd[1]+1 and third[1] > fst[1]:
            obstacleRectangles.append(obstacles)

    print(obstacleRectangles)
    print(len(obstacleRectangles))

    while True:
        pass