
def getInput():
    with open("example.txt","r") as file:
        return file.read()

def getMiddle(list):
    return list[len(list)//2]

class linked:
    def __init__(self,value=None,next=None):
        self.next = next
        self.value = value

    def len(self):
        cursor = linked(next=self.next)
        lenght = 0 if self.value is None else 1
        while cursor.next is not None:
            lenght += 1
            cursor = cursor.next
        return lenght

    def append(self,value):
        if self.next is None:
            self.next = linked(value)
        else:
            self.next.append(value)

    def getByValue(self,value):
        if self.value == value:
            return self
        else:
            if self.next is None:
                return None
            return self.next.getByValue(value)

    def getByIndex(self,index):
        if index < 0:
            return None
        if index == 0:
            return self

        cursor = self.next
        i = 1
        while i < index:
            if cursor is None:
                return None
            cursor = cursor.next
            i+=1
        return cursor

    def getIndex(self,value):
        if value == self.value:
            return 0
        if self.next is None:
            return None
        return self.next.getIndex(value) + 1


if __name__ == '__main__':
    rules,updates = getInput().split("\n\n")
    rules = [(fst,snd) for fst,snd in [line.split("|") for line in rules.split("\n")]]
    updates = [elem for elem in [line.split(",") for line in updates.split("\n")]]

    sum = 0
    for update in updates:
        if update == [""]:
            continue
        updateRules = []

        for rule in rules:
            if rule[0] in update and rule[1] in update:
                updateRules.append(rule)

        start = None
        for rule in updateRules:
            if start is None:
                start = linked(rule[0],linked(rule[1]))
            else:
                if start.getByValue(rule[0]) is None and start.getByValue(rule[1]) is None:
                    continue
                elif start.getByValue(rule[0]) is None and start.getByValue(rule[1]).value == start.value:
                    start = linked(rule[0],start)
                elif start.getByValue(rule[0]) is not None and start.getByValue(rule[1]) is not None:
                    cursor = start.getByValue(rule[0])
                    isValid = False

                    for i in range(start.getIndex(rule[0]),start.len()):
                        if cursor.next.value == rule[1]:
                            isValid = True
                            break
                    
                    if not isValid:
                        tmp = start.next
                        start.getByValue(rule[0]).next = start.getByValue(rule[1])
                        start.getByValue(rule[0]).next.next = tmp



        txt = ""
        for i in range(start.len()):
            if i == start.len()-1:
                txt += f"{start.getByIndex(i).value}"
            else:
                txt += f"{start.getByIndex(i).value} -> "

        print(update)
        print(updateRules)
        print(txt)
        print()

        linkedList = linked(1)
        linkedList.append(5)
        linkedList.append(23)
        linkedList.append(3)
        print(linkedList.getIndex(5))
