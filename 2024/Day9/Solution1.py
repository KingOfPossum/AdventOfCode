
def readInput():
    with open("example.txt","r") as file:
        return [int(num) for num in list(file.readline())]

def generateDiskMap(_input):
    disk_map = []
    type = -1
    for i in range(len(_input)):
        type = (-1) ** (i + 1)
        for j in range(_input[i]):
            if type == -1:
                disk_map.append(str(i // 2))
            elif type == 1:
                disk_map.append('.')
    return disk_map

def rearrangeDiskMap(disk_map):
    finished = False
    for i in range(len(disk_map) - 1, -1, -1):
        if not finished:
            current = disk_map[i]
            for j in range(len(disk_map) - (len(disk_map) - i)):
                if disk_map[j] == '.':
                    disk_map[j], disk_map[i] = current, '.'
                    break
                if i - 1 == j:
                    finished = True
    print("".join(disk_map))

if __name__ == "__main__":
    content = readInput()
    print(content)

    disk_map = generateDiskMap(content)
    print(disk_map)
    rearrangeDiskMap(disk_map)

    result = 0
    for i in range(len(disk_map)):
        if disk_map[i] == '.':
            continue
        result += i * int(disk_map[i])

    print(result)