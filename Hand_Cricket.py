import random
print("Let's play a game\nNote: You cannot write any other number than the one given to you\nWhat do you choose (Batting or Bowling)?")
option = int(input("Enter your option (1 for Batting / 2 for Bowling): "))
num, a = 7, 81 
your_score = 0
computer_score = 0

if option == 1:
    print("It's your batting first")
    while a != num:
        a = int(input("Enter any number between (1-6): "))
        num = random.randint(1, 6)
        if a == num:
            print("You're out! Now it's the computer's turn.")
            break
        print("GOOD JOB!")
        your_score += a
        print(f"Your option: {a}")
        print(f"Computer's option: {num}")
        print(f"Your score is {your_score}")
    
    num, a = 7, 81 
    print("Now it's your bowling")
    while a != num:
        a = int(input("Enter any number between (1-6): "))
        num = random.randint(1, 6)
        if a == num:
            print("GOOD JOB! Computer is out.")
            print(f"Computer's score: {computer_score}")
            break
        computer_score += num
        print(f"Your option: {a}")
        print(f"Computer's option: {num}")
        print(f"Computer's score: {computer_score}")
    
    if your_score > computer_score:
        print("Congratulations! You win.")
    elif your_score < computer_score:
        print("You lose. Try next time.")
    else:
        print("It's a draw.")

if option == 2:
    print("It's your bowling first")
    while a != num:
        a = int(input("Enter any number between (1-6): "))
        num = random.randint(1, 6)
        if a == num:
            print("Good job! Computer is out.")
            print(f"Computer's score: {computer_score}")
            break
        computer_score += num
        print(f"Your option: {a}")
        print(f"Computer's option: {num}")
        print(f"Computer's score: {computer_score}")
    
    num, a = 7, 81 
    print("Now it's your batting")
    while a != num:
        a = int(input("Enter any number between (1-6): "))
        num = random.randint(1, 6)
        if a == num:
            print("You're out! Now it's the computer's turn.")
            break
        print("Good job!")
        your_score += a
        print(f"Your option: {a}")
        print(f"Computer's option: {num}")
        print(f"Your score is {your_score}")
    
    if your_score > computer_score:
        print("Congratulations! You win.")
    elif your_score < computer_score:
        print("You lose. Try next time.")
    else:
        print("It's a draw.")