import random

lowest_num = 0 
greatest_num = 10

answer = random.randint(lowest_num,greatest_num+1)

guesses = 0
is_running = True

while is_running:
    guess = input(f"Enter your guess between:({lowest_num},{greatest_num}): ")
    if guess.isdigit():
        guess = int(guess)  
        guesses += 1

        if guess < lowest_num or guess > greatest_num:
            print(f"Enter the numbers between {lowest_num}-{greatest_num}")

        elif guess < answer:
            print("Too! Low")

        elif guess > answer:
            print("Too! High")

        else:
            print("Hey you win!")
            print(f"Guesses : {guesses} ")

            is_running = False


        
