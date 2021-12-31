import random
suits = ["club", "diamond", "heart", "spade"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

keep_going = True
while keep_going:
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    computer_face = random.choice(faces)
    computer_suit = random.choice(suits)
    print("my card is", my_suit + my_face)
    print("computer's card is", computer_suit + computer_face)

    if faces.index(my_face) > faces.index(computer_face):
        print("I won!!")
    elif faces.index(my_face) < faces.index(computer_face):
        print("I lost!!")
    else:
        if suits.index(my_suit) > suits.index(computer_suit):
            print("I won!!")
        elif suits.index(my_suit) < suits.index(computer_suit):
            print("I lost!!")
        else:
            print("비겼습니다.")

    answer = input("[Enter]키를 누르면 한번 더, 다른 키를 누르면 종료 : ")
    keep_going = (answer == "")



