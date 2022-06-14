import random

print("Let's Play A Number Guessing Game, Take any number from 1 to 9")

num = random.randint(1,9);

chances = 0

while chances < 5:
    guess = int(input("Write the number you took... "))


    

if guess == num:
    print("Congrats, You choosed right.")
    break

elif guess < num:
    print("Your guess was too low", guess)

else:
    print("Your guess was too high", guess)


chances += 1

if not chances < 5:
    print("You lose! The number is ", num)