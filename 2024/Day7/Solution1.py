from itertools import product

def readInput():
    with open("input.txt","r") as file:
        return file.read()

Operations = ['+','*']

if __name__ == "__main__":
    content = readInput().split("\n")
    testValues = [line.split(":")[0] for line in content]
    nums = [line.split(":")[1].split() for line in content if not line == ""]

    equations = list(zip(testValues, nums))

    #print(testValues)
    #print(nums)
    #print(equations)

    sum = 0

    for equation in equations:
        numOfOpperations = len(equation[1])-1
        possibleOperations = list(product(Operations, repeat=numOfOpperations))

        print(equation)
        print(possibleOperations)

        isValid = False
        for operation in possibleOperations:
            result = 0
            for i in range(len(operation)):
                if i == 0:
                    if operation[i] == "+":
                        result += int(equation[1][i]) + int(equation[1][i+1])
                        continue
                    result += int(equation[1][i]) * int(equation[1][i+1])
                    continue
                if operation[i] == "*":
                    result *= int(equation[1][i+1])
                    continue
                result += int(equation[1][i+1])
            if result == int(equation[0]):
                isValid = True
        if isValid:
            print("Equation is Valid!")
            sum += int(equation[0])

    print(sum)

