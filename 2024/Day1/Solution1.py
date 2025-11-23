
def readInput():
    with open("input.txt","r") as file:
        return file.read()

if __name__ == "__main__":
    content = readInput().split("\n")
    content = [numbers.split() for numbers in content if numbers != ""]

    left_list = [int(nums[0]) for nums in content]
    right_list = [int(nums[1]) for nums in content]

    sum = 0

    while len(left_list) > 0:
        l_min = min(left_list)
        r_min = min(right_list)

        left_list.remove(l_min)
        right_list.remove(r_min)

        dis = abs(l_min - r_min)
        sum += dis

