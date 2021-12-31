import random
choices = ["가위", "바위", "보"]

draw = 0
computer_win = 0
you_win = 0

# player = input("가위, 바위, 보 중에서 하나를 선택해주세요.(중단은 quit)")
for i in range(300):
    computer = random.choice(choices)
    player = random.choice(choices)
    # print("당신의 선택은 "+ player + " 컴퓨터의 선택은 "+ computer)
    if player == computer:
        # print("비겼습니다.")
        draw += 1
    elif player == "가위":
        if computer == "바위":
            # print("computer win !!")
            computer_win += 1
        else:
            # print("you win !!")
            you_win += 1
        
    elif player == "바위":
        if computer == "보":
            # print("computer win !!")
            computer_win += 1
        else:
            # print("you win !!") 
            you_win += 1

    elif player == "보":
        if computer == "가위":
            # print("computer win !!")
            computer_win += 1
        else:
            # print("you win !!")
            you_win += 1
    else: 
        print("에러가 발생했습니다.")

print("draw = ", draw, "computer win", computer_win, "you win", you_win)





