
def getInput():
    with open("input.txt","r") as file:
        return file.read()

def getMiddle(list):
    return list[len(list)//2]

if __name__ == '__main__':
    rules,updates = getInput().split("\n\n")
    rules = [(fst,snd) for fst,snd in [line.split("|") for line in rules.split("\n")]]
    updates = [elem for elem in [line.split(",") for line in updates.split("\n")]]

    sum = 0
    for update in updates:
        if update == [""]:
            continue
        updateRules = []
        middle = getMiddle(update)
        isValid = True

        for rule in rules:
            if rule[0] in update and rule[1] in update:
                updateRules.append(rule)

        for elem in update:
            for rule in updateRules:
                if elem == rule[0]:
                    if update.index(elem) > update.index(rule[1]):
                        isValid = False
                elif elem == rule[1]:
                    if update.index(elem) < update.index(rule[0]):
                        isValid = False

        if isValid:
            sum += int(middle)

    print(f"SUM : {sum}")