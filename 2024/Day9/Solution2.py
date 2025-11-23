
def readInput():
    with open("input.txt","r") as file:
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

def getFreeBlocks(disk_map):
    free_blocks = []

    current_block = []
    start_index = -1
    for i in range(len(disk_map)):
        if disk_map[i] == '.':
            if start_index == -1:
                start_index = i
            current_block.append(1)
        else:
            if not start_index == -1:
                free_blocks.append((start_index, sum(current_block)))
                current_block = []
                start_index = -1

    return free_blocks

def getUsedBlocks(disk_map):
    used_blocks = []

    current_block = []
    start_index = -1
    current_value = None

    for i in range(len(disk_map)):
        if not disk_map[i] == '.':
            if start_index == -1:
                current_block.append(disk_map[i])
                current_value = disk_map[i]
                start_index = i
                continue
            if not disk_map[i] in current_block:
                used_blocks.append((start_index,len(current_block),current_value))
                start_index = i
                current_block = [disk_map[i]]
                current_value = disk_map[i]
                continue
            current_block.append(disk_map[i])
        else:
            if not start_index == -1:
                used_blocks.append((start_index,len(current_block),current_value))
                start_index = -1
                current_block = []
                current_value = None
    if start_index != -1:
        used_blocks.append((start_index,len(current_block),current_value))

    return used_blocks

def rearrangeDiskMap(disk_map):
    free_blocks = getFreeBlocks(disk_map)
    used_blocks = getUsedBlocks(disk_map)

    for i in range(len(used_blocks)-1,-1,-1):
        moved = False
        for j in range(len(free_blocks)):
            if not moved:
                if free_blocks[j][1] >= used_blocks[i][1]:
                    if free_blocks[j][0] < used_blocks[i][0]:
                        for p in range(free_blocks[j][0],free_blocks[j][0]+used_blocks[i][1]):
                            disk_map[p] = used_blocks[i][2]
                        for p in range(used_blocks[i][0],used_blocks[i][0]+used_blocks[i][1]):
                            disk_map[p] = "."

                        if free_blocks[j][1] == used_blocks[i][1]:
                            free_blocks[j] = (-1,-1)
                        else:
                            free_blocks[j] = (free_blocks[j][0]+used_blocks[i][1],free_blocks[j][1]-used_blocks[i][1])
                        moved = True

if __name__ == "__main__":
    content = readInput()

    disk_map = generateDiskMap(content)
    rearrangeDiskMap(disk_map)

    result = 0
    for i in range(len(disk_map)):
        if disk_map[i] == '.':
            continue
        result += i * int(disk_map[i])

    print(result)