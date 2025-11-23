
def readInput():
    with open("input.txt","r") as file:
        return file.read()

if __name__ == "__main__":
    content = readInput().split(" ")

    iterations = 25

    stones = content
    print(stones)
    for i in range(iterations):
        new_stones = []
        for j in range(len(stones)):
            if stones[j] == '0':
                new_stones.append('1')
            elif len(stones[j]) % 2 == 0:
                left_part = stones[j][:len(stones[j])//2]
                right_part = stones[j][len(stones[j])//2:]
                while right_part[0] == "0" and len(right_part) > 1:
                    right_part = right_part[1:]
                new_stones.append(left_part)
                new_stones.append(right_part)
            else:
                new_stones.append(str(int(stones[j]) * 2024))
        stones = new_stones
        print(" ".join(stones))
        print(len(stones))