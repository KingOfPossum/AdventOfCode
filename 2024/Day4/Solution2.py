import re

def readInput():
    with open("input.txt","r") as file:
        return file.read()

if __name__ == "__main__":
    content = readInput().split()
    regex = re.compile("MAS|SAM")

    sum = 0
    for i in range(len(content)-1):
        for j in range(len(content)-1):
            if i > 0 and j+1 < len(content) and j > 0 and j+1 < len(content):
                word1 = content[i-1][j-1] + content[i][j] + content[i+1][j+1]
                word2 = content[i+1][j-1] + content[i][j] + content[i-1][j+1]

                if regex.match(word1) and regex.match(word2):
                    sum += 1

    print(sum)