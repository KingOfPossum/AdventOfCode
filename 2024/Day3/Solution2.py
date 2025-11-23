import re

def readInput():
    with open("input.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    content = readInput()

    mulRegex = re.compile(r"mul\(\d*,\d*\)")
    doRegex = re.compile(r"do\(\)")
    dontRegex = re.compile(r"don't\(\)")

    splitContent = doRegex.split(content)
    splitContent = [dontRegex.split(cont) for cont in splitContent]

    sum = 0
    for do in splitContent:
        matches = [match[4:len(match)-1].split(",") for match in mulRegex.findall(do[0])]

        for match in matches:
            sum += int(match[0]) * int(match[1])

    print(sum)