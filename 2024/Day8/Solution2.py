from itertools import permutations

def readInput():
    with open("input.txt") as file:
        return file.read()

def getFrequenciesChars(grid):
    frequencies = [char for line in grid for char in line if char.isalnum()]
    return set(frequencies)

def printContent(grid):
    for i in range(len(grid)):
        txt = ""
        for j in range(len(grid[i])):
            txt += grid[i][j]
        print(txt)

if __name__ == '__main__':
    content = [list(line) for line in readInput().split("\n")]

    frequencyChars = getFrequenciesChars(content)
    frequencyPos = {}

    for i in range(len(content)):
        for j in range(len(content[0])):
            if content[i][j] in frequencyChars:
                try:
                    frequencyPos[content[i][j]].append((i, j))
                except KeyError:
                    frequencyPos[content[i][j]] = [(i, j)]

    antennas = set()
    for key in frequencyPos.keys():
        frequencies = frequencyPos[key]
        frequencies = permutations(frequencies, 2)

        for frequencyPair in frequencies:
            dis = (frequencyPair[0][0] - frequencyPair[1][0],frequencyPair[0][1] - frequencyPair[1][1])

            antennas.add(frequencyPair[0])
            antennas.add(frequencyPair[1])

            outOfRange = False
            mulFactor = 1
            while not outOfRange:
                antenna = (frequencyPair[0][0] + dis[0] * mulFactor, frequencyPair[0][1] + dis[1] * mulFactor)

                if 0 <= antenna[0] < len(content) and 0 <= antenna[1] < len(content):
                    antennas.add(antenna)
                    mulFactor += 1
                    continue
                outOfRange = True

    for antenna in antennas:
        if content[antenna[0]][antenna[1]] not in frequencyPos:
            content[antenna[0]][antenna[1]] = "#"

    numberOfAntennas = len(antennas)

    printContent(content)
    print(f"Number of unique Antennas : {numberOfAntennas}")