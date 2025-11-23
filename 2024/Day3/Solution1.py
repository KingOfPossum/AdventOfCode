import re

def readInput():
    with open("input.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    regex = re.compile(r"mul\(\d*,\d*\)")
    content = readInput()

    matches = [match[4:len(match)-1].split(",") for match in regex.findall(content)]

    sum = 0
    for match in matches:
        sum += int(match[0])*int(match[1])

    print(sum)