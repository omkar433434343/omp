import random
print("Welcome to NUMBER GUESSING GAME")
number = random.randint(1,10)
chances = 0
print("Guess a number (between 1 and 10):")
while chances < 10:
    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulation !!! You Guessed Correctly :)  !!!")
        break
    elif guess < number:
        print("Guess higher than", guess)

    
    else:
        print("TOO HIGH guess lower", guess)
    chances += 1
if not chances < 10:
    print("You LOST :( try again next time", number)
    

print ("Made by OM ")