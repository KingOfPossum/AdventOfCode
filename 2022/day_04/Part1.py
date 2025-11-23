sum = 0

with open("../../../Python/Discord/Discord_Listbot_3.0/src/Input.txt", "r") as file:
    data = file.read()
    lines = data.split()

    for line in lines:
        ranges = line.split(",")
        range1 = ranges[0].split("-")
        range2 = ranges[1].split("-")

        range1Begin = int(range1[0])
        range1End = int(range1[1])
        range2Begin = int(range2[0])
        range2End = int(range2[1])

        if (range1Begin - range2Begin <= 0 <= range1End - range2End) or (
                range2Begin - range1Begin <= 0 <= range2End - range1End):
            sum += 1

print(sum)