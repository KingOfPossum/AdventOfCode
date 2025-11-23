import re

def readInput():
    with open("input.txt","r") as file:
        return file.read()

if __name__ == "__main__":
    regex = re.compile(r"(?=(XMAS|SAMX))")
    normalContent = readInput().split()
    transposedContent = ["".join([normalContent[i][j] for i in range(len(normalContent))]) for j in range(len(normalContent[0]))]

    diagonalLRContent = []
    for i in range(len(normalContent)):
        list = []
        for j in range(i+1):
              list.append(normalContent[i-j][j])
        diagonalLRContent.append("".join(list))

    for j in range(len(normalContent)-1,0,-1):
        list = []
        for i in range(len(normalContent)-1,j - 1,-1):
            list.append(normalContent[i][j+((len(normalContent)-1)-i)])
        diagonalLRContent.append("".join(list))

    diagonalRLContent = []
    for i in range(len(normalContent)):
        list = []
        for j in range(len(normalContent)-1,len(normalContent)-i-1,-1):
            list.append(normalContent[i-(len(normalContent) - j)][j])
        diagonalRLContent.append("".join(list))

    for j in range(len(normalContent)):
        list = []
        for i in range(len(normalContent)-1,len(normalContent)-j-2,-1):
            list.append(normalContent[i][j-((len(normalContent)-1)-i)])
        diagonalRLContent.append("".join(list))

    horizontalMatches = sum([len(regex.findall(line)) for line in normalContent])
    verticalMatches = sum([len(regex.findall(line)) for line in transposedContent])
    diagonalLRMatches = sum([len(regex.findall(line)) for line in diagonalLRContent])
    diagonalRLMatches = sum([len(regex.findall(line)) for line in diagonalRLContent])

    print(sum([horizontalMatches,verticalMatches,diagonalLRMatches,diagonalRLMatches]))