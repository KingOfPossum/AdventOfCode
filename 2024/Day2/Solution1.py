
def readInput():
    with open("input.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    content = readInput()
    content = [line.split() for line in content.split("\n") if line != ""]

    list = []
    for line in content:
        nums = []
        for num in line:
            nums.append(int(num))
        list.append(nums)

    print(content)
    print(list)

    sum = 0

    for line in list:
        ascending = False
        isSafe = True

        if line[0] < line[1]:
            ascending = True

        for i in range(len(line) - 1):
            if ascending:
                if line[i] > line[i+1] or abs(line[i+1] - line[i]) not in [1,2,3]:
                    isSafe = False
            else:
                if line[i] < line[i+1] or abs(line[i] - line[i+1]) not in [1,2,3]:
                    isSafe = False

        if isSafe:
            print(line)
            sum += 1

    print(sum)