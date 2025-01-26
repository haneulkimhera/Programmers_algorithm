N = int(input())

balloons = list(enumerate(map(int,input().split())))

answers = ""
pointer = 0

while(balloons):
    # print("=====================")
    # print(balloons)
    idx,num = balloons.pop(pointer)
    answers = answers + str(idx+1) + " "

    # next = pointer + num
    # if not 0<=next<length:
    #     next = pointer + (length%num)
    # pointer = next-1

    if not balloons:
        break

    if num > 0:
        pointer = (pointer + (num - 1)) % len(balloons)
    else:
        pointer = (pointer + num) % len(balloons)

    # print(f"current:{idx}, move:{num}, next>>>{pointer}")

print(answers)
