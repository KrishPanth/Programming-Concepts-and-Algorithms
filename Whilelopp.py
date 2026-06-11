

# 1. Create a Python program that prompts the user to enter their age. If the age is less
# than 18, print you are a minor. If the age is between 18 and 60, print you are an
# adult. For ages over 60, print you are a senior citizen. The program should continue
# until the user inputs stop.


while True:
    age = int(input("Please enter your age: "))

    if age < 18:
        print("You are a minor")
    elif age < 60:
        print("You are an adult")
    else:
        print("You are a senior citizen")

    user_input = input("Do you want to continue? (yes/no): ").lower()

    if user_input == "no":
        break      

# 2. Write a Python program that simulates waiting for a specific vehicle, such as a bus.
# The program should repeatedly prompt the user to input the name of a vehicle. If the
# input is not bus, the program should print waiting and continue. Once the user inputs
# bus, the program should print finally the wait is over and terminate the loop


while True:
    vehicle = input("Enter a vehicle name: ")
    if vehicle == "Aeroplane":
        print("Finally the wait is over")
        break
    else:
        print("Wait is over")



# 3. Generate a frequency table for the ratings list which is initialized below. Ratings =
# ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
#  a. Start by creating an empty dictionary named content_ratings
#  b. Loop through the ratings list. For each iteration, complete the following:
#  If the rating is already in content_ratings then increment the frequency of that rating by 1.
#  Else, initialize the rating with a value of 1 inside the content_ratings dictionary.


ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
content_ratings = {}
for i in ratings:
    if i in content_ratings:
        content_ratings[i] = content_ratings[i] + 1
    else:
        content_ratings[i] = 1
print(content_ratings)


# 4. Write a Python program that generates a random number between 1 and 10 and
# prompts the user to guess the number. The program should provide hints such as
# guess higher or guess lower based on the user's input. Once the user guesses the
# correct number, the program should display the number of attempts it took to guess
# the correct number.


import random
secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess == secret_number:
        print("Correct!")
        print("Total attempts taken:", attempts)
        break
    elif guess < secret_number:
        print("Your guess is lower")
    else:
        print("Your guess is higher")



# 5. Write a Python program that simulates a login system. The program should prompt
# the user to enter a username and password. If both are correct for example username
# is admin and password is 1234, print Login successful and exit. If either is incorrect,
# print Invalid credentials, try again. Allow the user up to 3 attempts before locking
# them out with the message too many failed attempts.


correct_username = "admin"
correct_password = "1234"
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Too many failed attempts. Account locked.")
        else:
            print("Invalid credentials, try again.")



#  6. Write a Python program that simulates a basic arithmetic quiz. Generate two random numbers between 1 and
#  30 and ask the user to provide the result of their multiplication. If the answer is correct, print correct and generate a new question. If
# the answer is wrong, print Incorrect, try again. Allow the user to stop the quiz when the user enters exit.

import random
while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    answer = input(f"What is {num1} x {num2}? (type 'exit' to stop): ")
    if answer.lower() == "exit":
        print("Quiz stopped. Bye!")
        break
    if int(answer) == num1 * num2:
        print("Correct!\n")
    else:
        print("Incorrect, try again.\n")




# 7. Write a Python program that prompts the user to repeatedly enter a name. If the user
# enters the phrase good luck, the program keeps track of how many times the phrase
# has been entered. When the phrase has been entered three times, the program should
# display a message stating you typed good luck three times. For each entry of good
# luck before the third occurrence, display the message you typed the same word
# [count] times. Continue this process until the phrase has been entered three times.        



count = 0
while count < 3:
    name = input("Enter a name: ")
    if name == "good luck":
        count += 1
        if count == 3:
            print("You typed good luck three times.")
        else:
            print(f"You typed the same word {count} times.")



# 8. Generate a random number (1–50). Give the user up to 7 attempts to guess it using a
# while loop. Track remaining attempts and stop early if they guess correctly or run out
# of tries


import random
num = random.randint(1, 50)
attempts = 7
while attempts > 0:
    guess = int(input(f"Guess (Attempts left {attempts}): "))
    if guess == num:
        print("Correct!")
        break
    elif guess < num:
        print("Too low")
    else:
        print("Too high")
    attempts -= 1
if attempts == 0:
    print("Game over. Number was", num)



# 9. Write a Python program that simulates a basic elevator system. The program should
# keep track of the elevator's current position and allow a user to travel to different
# floors until they choose to exit.
# Requirements:
# a) Starting State: The elevator should start on floor 1.
# b) Continuous Loop: Use a while loop to repeatedly ask the user for a destination floor.
# c) Input Handling: If the user enters 0, the program should print a goodbye
# message and terminate. If the user enters something that isn't a number,
# handle the error gracefully so the program doesn't crash.
# d) Logic: If the target floor is higher than the current floor, print a ‘Going up’
# message. If the target floor is lower than the current floor, print a ‘Going
# down’ message. If the user is already on the requested floor, inform them of that.
# e) State Update: After moving, update the current floor to the target floor so
# the next movement starts from the new location.



floor = 1
while True:
    f = int(input("Enter floor (0 to exit): "))
    if f == 0:
        print("Bye!")
        break
    if f > floor:
        print("Going up")
    elif f < floor:
        print("Going down")
    else:
        print("Already here")
    floor = f



# 10.


p1_score = 0
p2_score = 0

while p1_score < 5 and p2_score < 5:
    p1 = input("P1: ").lower()
    p2 = input("P2: ").lower()

    if p1 == p2:
        print("Tie")
    elif (p1 == "rock" and p2 == "scissor") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissor" and p2 == "paper"):
        p1_score += 1
        print("P1 +1")
    else:
        p2_score += 1
        print("P2 +1")

    print("Score:", p1_score, "-", p2_score)

if p1_score == 5:
    print("P1 wins!")
else:
    print("P2 wins!")



# 11. Write a python program to get the following output using while loop.
# 1 – 49
# 2 – 48
# 3 – 47
# 4 – 46
# .
# .
# .
# 48 – 2
# 49 –1


i = 1
j = 49
while i <= 49:
    print(i, "-", j)
    i += 1
    j -= 1


# 12. Write a program that accepts a number from the user and calculates the sum of all
# numbers from 1 up to that number.


n = int(input("Enter number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum =", total)



# 13. Print alphabet series A to Z.
# Output: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z


i = 65
while i <= 90:
    print(chr(i), end=" ")
    i += 1




# 14. Write a program to find the numbers which are below 20 in a list.
# number = [2, 40, 21, 31, 10, 7, 5]

number = [2, 40, 21, 31, 10, 7, 5]
i = 0
while i < len(number):
    if number[i] < 20:
        print(number[i])
    i += 1