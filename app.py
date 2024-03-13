import random 

game_over = True

count = 0

while game_over:

    try:
        user_input = int(input("""

        Choose From The Following 

        1. Rock 
        2. Paper 
        3. Scissor

        """))
    except:
        print("/nPlease Enter Valid")

    random_number = random.randint(1,3)

    mapping = {'1' : "Rock",'2' : "Paper", '3' : "Scissor"}

    print(f"\nYou Choose : {mapping[str(user_input)]}")

    if random_number == 1:
        print(f"\nCPU Choose : Rock")
    elif random_number == 2:
        print(f"\nCPU Choose : Paper")
    else:
        print(f"\nCPU Choose : Scissor")

    if user_input == random_number:
        print("\nDraw")
    elif user_input == 1 :
        if random_number == 3:
            print("\nYou Won!!")
            count += 1
        else:
            print("\nYou Lose")
    elif user_input == 2:
        if random_number == 1:
            print("\nYou Won!!")
            count += 1
        else:
            print("\nYou Lose")
    else:
        if random_number == 2:
            print("\nYou Won!!")
            count += 1
        else:
            print("\nYou Lose")

    end_game = input("\nDo you want to play again?(Y/N): ").lower()

    if end_game == 'n':
        print(f"/nYour Score is: {count}")
        break




