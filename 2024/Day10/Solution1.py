
def readInput():
    with open("input.txt","r") as file:
        return file.read()

def checkForPath(pos,grid,acc):
    if pos[2] == 9:
        acc.append((pos[0],pos[1]))
    if 0 <= pos[0] < len(grid) and 0 <= pos[1]+1 < len(grid):
        if grid[pos[0]][pos[1]+1] == pos[2]+1:
            checkForPath((pos[0],pos[1]+1,pos[2]+1),grid,acc)
    if 0 <= pos[0] < len(grid) and 0 <= pos[1]-1 < len(grid):
        if grid[pos[0]][pos[1]-1] == pos[2]+1:
            checkForPath((pos[0],pos[1]-1,pos[2]+1),grid,acc)
    if 0 <= pos[0]-1 < len(grid) and 0 <= pos[1] < len(grid):
        if grid[pos[0]-1][pos[1]] == pos[2]+1:
            checkForPath((pos[0]-1,pos[1],pos[2]+1),grid,acc)
    if 0 <= pos[0]+1 < len(grid) and 0 <= pos[1] < len(grid):
        if grid[pos[0]+1][pos[1]] == pos[2]+1:
            checkForPath((pos[0]+1,pos[1],pos[2]+1),grid,acc)

if __name__ == "__main__":
    content = [list(line) for line in readInput().split("\n")]

    print(content)

    start_indices = []

    for i in range(len(content)):
        for j in range(len(content[0])):
            if content[i][j] == '0':
                start_indices.append((i,j,0))
                content[i][j] = 0
                continue
            if content[i][j].isnumeric():
                content[i][j] = int(content[i][j])
                continue
            content[i][j] = -10

    print(content)
    print(start_indices)

    score = 0
    if start_indices is not None:
        for index in start_indices:
            acc = []
            checkForPath(index,content,acc)
            score += len(set(acc))

    print(score)