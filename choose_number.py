import random


def choose_seq(grid, num):
    start_num = [random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1)]
    print("Index", start_num)
    print("Starting number: ", grid[start_num[0]][start_num[1]])
    num.append(grid[start_num[0]][start_num[1]])

    isAble = False
    while not isAble:
        direction = random.randint(0, 7)
        if direction == 0 and start_num[0] >= 4 and start_num[1] >= 4:
            print("Left-Up")
            for j in range(4):
                print(grid[start_num[0] - j - 1][start_num[1] - j - 1])
                num.append(grid[start_num[0] - j - 1][start_num[1] - j - 1])
            isAble = True
        elif direction == 1 and start_num[0] >= 4:
            print("Up")
            for j in range(4):
                print(grid[start_num[0] - j - 1][start_num[1]])
                num.append(grid[start_num[0] - j - 1][start_num[1]])
            isAble = True
        elif direction == 2 and start_num[0] >= 4 and start_num[1] <= len(grid[0]) - 5:
            print("Right-Up")
            for j in range(4):
                print(grid[start_num[0] - j - 1][start_num[1] + j + 1])
                num.append(grid[start_num[0] - j - 1][start_num[1] + j + 1])
            isAble = True
        elif direction == 3 and start_num[1] <= len(grid[0]) - 5:
            print("Right")
            for j in range(4):
                print(grid[start_num[0]][start_num[1] + j + 1])
                num.append(grid[start_num[0]][start_num[1] + j + 1])
            isAble = True
        elif direction == 4 and start_num[0] <= len(grid) - 5 and start_num[1] <= len(grid[0]) - 5:
            print("Right-Down")
            for j in range(4):
                print(grid[start_num[0] + j + 1][start_num[1] + j + 1])
                num.append(grid[start_num[0] + j + 1][start_num[1] + j + 1])
            isAble = True
        elif direction == 5 and start_num[0] <= len(grid) - 5:
            print("Down")
            for j in range(4):
                print(grid[start_num[0] + j + 1][start_num[1]])
                num.append(grid[start_num[0] + j + 1][start_num[1]])
            isAble = True
        elif direction == 6 and start_num[0] <= len(grid) - 5 and start_num[1] >= 4:
            print("Left-Down")
            for j in range(4):
                print(grid[start_num[0] + j + 1][start_num[1] - j - 1])
                num.append(grid[start_num[0] + j + 1][start_num[1] - j - 1])
            isAble = True
        elif direction == 7 and start_num[1] >= 4:
            print("Left")
            for j in range(4):
                print(grid[start_num[0]][start_num[1] - j - 1])
                num.append(grid[start_num[0]][start_num[1] - j - 1])
            isAble = True

    print(num)
    print("-----------------------------------------------------------")
