#    Task


# 4.Design a program for a 'Student Resource Portal.' The program should
# ask for a username and a password.
#  If the username is admin and password is ad123, print
# Access Granted: Faculty Dashboard.
#  If the username is student and password is st2026, print
# Access Granted: Notes and Practice Questions.
#  For any other combination, print Invalid Credentials. 
# Please try again.


username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard")
elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions")
else:
    print("Invalid Credentials. Please try again.")

# ------------------------------------------------------------------------

# 5. Design a Traffic Light System. Given a variable light that can be red,
# yellow, or green, print the correct instruction. Also handle an invalid
# color with an error message.


light = input("Enter light color: ")
if light == "red":
    print("Stop!")
elif light == "yellow":
    print("Get Ready.")
elif light == "green":
    print("Go!")
else:
    print("Error: Invalid light color.")


# --------------------------------------------------------------------------

# 6. Write a match statement that takes a number 1–4 and prints the
# corresponding season: 1=spring, 2=summer, 3=autumn, 4=winter.
# Default: unknown


season_number=int(input('enter season number:'))
match season_number:
    case 1 |2:
        print('spring')
    case 3:
        print('autumn')
    case 4:
        print('winter')
    case 5:
        print('summer')
    case _:
        print('unknown')

# --------------------------------------------------------------------------

# 7. Design a Bank Loan Approval System. Approve a loan only if ALL three conditions are met:
#  Age is between 21 and 60 (inclusive)
#  Monthly income is at least 30,000
#  Credit score is at least 700
# If not approved, print which condition failed. 


age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))

if age >= 21 and age <= 60 and income >= 30000 and credit_score >= 700:
    print("Loan Approved!")
else:
    if not (age >= 21 and age <= 60):
        print("Failed: Age must be between 21 and 60.")
    if income < 30000:
        print("Failed: Monthly income must be at least 30,000.")
    if credit_score < 700:
        print("Failed: Credit score must be at least 700.")


# --------------------------------------------------------------------------

# 8. You are developing a simple ticket booking system for a movie theatre.
# The ticket price depends on the age of the person and whether they
# have a membership card. If the person is under 12, the ticket is free. If
# the person is between 12 and 60: If they have a membership card, the
# ticket costs Rs. 150. If not, the ticket costs Rs. 200. If the person is
# above 60, they get a senior citizen discount, and the ticket costs Rs.
# 100. Write a Python program using nested if-else to calculate and print
# the ticket price based on the user's age and membership status.

age = int(input("Enter age: "))

if age < 12:
    print("Ticket Price: Free")
elif age <= 60:
    membership = input("Do you have a membership card? (yes/no): ")
    if membership == "yes":
        print("Ticket Price: Rs. 150")
    else:
        print("Ticket Price: Rs. 200")
else:
    print("Ticket Price: Rs. 100 (Senior Citizen Discount)")


# --------------------------------------------------------------------------       

# 9. A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. Ask user for 
# their salary and year of service and print the net bonus amount.

salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.05
    print(f"Net Bonus Amount: Rs. {bonus}")
else:
    print("Not eligible for bonus.")


# --------------------------------------------------------------------------

# 10. Write a python program which accepts the radius of circle from user and compute the area.


import math
radius = float(input("Enter radius: "))
area = math.pi * radius ** 2
print(f"Area of Circle: {area:.2f}")


#--------------------------------------------------------------------------


# 12. Accept input from user
# If given number is a multiple of both 3 and 5 prints Fizz Buzz instead of number
# If given number is a multiple of 3 but not 5 prints Fizz instead of number
# If given number is a multiple of 5 but not 3 prints Buzz instead of number
# If given number is not multiple of 3 or 5 prints value as usual.


num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)


#--------------------------------------------------------------------------

# 13. A utility company charges different rates based on electricity usage:
# If usage < 100 units then cost Rs 5 per unit
# If usage is between 100 to 300 units:
# First 100 units: Rs 5
# Next units: Rs 8
# If usage is > 300 units: First 100: Rs 5 Next 200: Rs 8 Remaining: Rs 10

units = int(input("Enter electricity usage (units): "))
if units < 100:
    cost = units * 5
elif units <= 300:
    cost = (100 * 5) + ((units - 100) * 8)
else:
    cost = (100 * 5) + (200 * 8) + ((units - 300) * 10)
print(f"Total Bill: Rs. {cost}")


#--------------------------------------------------------------------------

#14 Rock Paper Scissors
p1 = input("\nPlayer 1 - Enter move (rock/paper/scissors): ")
p2 = input("Player 2 - Enter move (rock/paper/scissors): ")

if p1 == p2:
    print("It's a Tie!")
elif (p1 == "rock" and p2 == "scissors") or \
     (p1 == "scissors" and p2 == "paper") or \
     (p1 == "paper" and p2 == "rock"):
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")



#--------------------------------------------------------------------------

# 15. Write a Python program that takes a number as input, first
# checks if it is positive if yes then check whether it is even or odd

num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("The number is Positive and Even.")
    else:
        print("The number is Positive and Odd.")
else:
    print("The number is not positive.")

#--------------------------------------------------------------------------

#  16. A store gives a 20% discount if the total purchase is above RS
#  1000 AND the customer is a member, or a 10% discount if the
# purchase is above RS 1000 but the customer is not a member. Write a
# program that takes total_amount and is_member (True/False) as
# input and prints the final amount after applying the correct discount or no discount.

total_amount = float(input("Enter total purchase amount: Rs. "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

if total_amount > 1000 and is_member:
    discount = total_amount * 0.20
    final = total_amount - discount
    print(f"20% Discount Applied! Final Amount: Rs. {final}")
elif total_amount > 1000:
    discount = total_amount * 0.10
    final = total_amount - discount
    print(f"10% Discount Applied! Final Amount: Rs. {final}")
else:
    print(f"No Discount. Final Amount: Rs. {total_amount}")

#--------------------------------------------------------------------------    


# 18. WAP which accepts marks of four subjects and display total
# marks, percentage and grade. Hint: more than 70 –> distinction, more
# than 60 –> first, more than 40 –> pass, less than 40 –> fail



s1 = float(input("Enter marks of Subject 1: "))
s2 = float(input("Enter marks of Subject 2: "))
s3 = float(input("Enter marks of Subject 3: "))
s4 = float(input("Enter marks of Subject 4: "))

total = s1 + s2 + s3 + s4
percentage = total / 4

if percentage >= 70:
    grade = "Distinction"
elif percentage >= 60:
    grade = "First"
elif percentage >= 40:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Total Marks  : {total}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")


#--------------------------------------------------------------------------

# 19. Write a Python program to simulate a simple ATM with the
# following specifications: Assume the card is valid (is_valid = True)
#  Initial account balance is RS 5000
#  Correct PIN is 123
#  After entering correct PIN, display the menu:
# 1. Withdraw
# 2. Check Balance
# 3. Exit
# If user selects 1 then ask amount and deduct from balance
# If user selects 2 then show current balance
# If user selects 3 then print Thank you for visiting
# Show proper messages for wrong PIN and invalid option


is_valid = True
balance = 5000
correct_pin = 123

if not is_valid:
    print("Invalid Card.")
else:
    pin = int(input("Enter PIN: "))

    if pin != correct_pin:
        print("Wrong PIN. Access Denied.")
    else:
        print("\n1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")

        choice = int(input("\nSelect option: "))

        if choice == 1:
            amount = float(input("Enter amount to withdraw: Rs. "))
            if amount > balance:
                print("Insufficient Balance.")
            else:
                balance -= amount
                print(f"Rs. {amount:.2f} withdrawn. Remaining Balance: Rs. {balance:.2f}")
        elif choice == 2:
            print(f"Current Balance: Rs. {balance:.2f}")
        elif choice == 3:
            print("Thank you for visiting.")
        else:
            print("Invalid option.")

#--------------------------------------------------------------------------   



# first = input("First Name: ")
# last = input("Last Name: ")
# email = input("Email: ")
# re_email = input("Re-enter Email: ")
# password = input("Password: ")

if not first.isalpha():
    print("Invalid first name.")
elif not last.isalpha():
    print("Invalid last name.")
elif "@" not in email or "." not in email:
    print("Invalid email.")
elif email != re_email:
    print("Emails do not match.")
elif len(password) < 6:
    print("Password must be at least 6 characters.")
else:
    print("Registration Successful!")

#--------------------------------------------------------------------------

#11,17,20,21 Qno 


# Q.no 11 Accept the age, gender ('M', 'F'), number of days and display the wages accordingly.
# >=18 and <30 M 700
# F 750
# >=30 and <=40 M 800
# F 850

def wage():
    age=int(input("Enter the age: "))
    gender=input("Enter your gender (M= Male, F= Female): ").lower()
    days=int(input("Number of working days: "))
    if age >=18 and age<30:
        if gender == "m":
            print(f"\nYour total wage of {days} days is: ",700*days)
        elif gender == "f":
            print(f"\nYour total wage of {days} days is: ",750*days)
        else:
            print("Invalid option!!")
    elif age >=30 and age<40:
        if gender == "m":
            print(f"\nYour total wage of {days} days is: ",800*days)
        elif gender == "f":
            print(f"\nYour total wage of {days} days is: ",850*days)
        else:
            print("Invalid option!!")

    else:
        print("Invalid option!!!")

# Q no 17
# Create a weight conversion program that:
# Asks the user what their Earth weight is (as a float).
# Asks the user for a planet number (as an int).
# Then, use an if/elif/else statement to calculate the user's weight on
# the destination planet.
# To calculate the user's weight: destination weight=Earth weight ×
# relative gravity
# If the user enters a planet number outside of 1 - 7, print a message
# that says 'Invalid planet number'

def weightConv():
    earthWeight=float(input("Enter your normal weight: "))
    planet=int(input("""
                     
                     Enter you planet in number: 
                     1. Mercury
                     2. Venus
                     3. Mars
                     4. Jupiter
                     5. Saturn
                     6. Uranus
                     7. Neptune

                     """))
    print(f"Your weight in earth is {earthWeight}kg in other planet it'll be: \n")
    if planet==1:
       print("Your weight in Mercury will be:",float(earthWeight*0.38,"kg"))
    elif planet ==2:
       print("Your weight in Venus will be:",float(earthWeight*0.91),"kg")
    elif planet ==3:
       print("Your weight in Mars will be:",float(earthWeight*0.38),"kg")
    elif planet ==4:
       print("Your weight in Jupiter will be:",float(earthWeight*2.53),"kg")
    elif planet ==5:
       print("Your weight in Saturn will be:",float(earthWeight*1.07),"kg")
    elif planet ==6:
       print("Your weight in Uranus will be:",float(earthWeight*0.89),"kg")
    elif planet ==7:
       print("Your weight in Neptune will be:",float(earthWeight*1.14),"kg")
    else:
        print("Invalid planet number!!")



#     Q.no 20
# Create a Python program for a text-based adventure game called
# Magic Forest based on the given flowchart. The program should follow
# the exact logic shown in the flowchart.
def game():
    print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ------------------ The Magic Forest Game ------------------
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        About the game: This game has 3 stages- Stage 1, Stage 2 and Stage 3,
                        Choosing wrong option will lead the Game Over and if the option is
                        right you will move on the next level
        
    """)

    print(" Welcome to the Magic Forest Game ")
    name=input("Enter your game name: ")
    print(f"Hello {name} you are now in Stage 1: Start and Inital Direction")
    print("\n Do you want to go north or south?")
    direction=input(" Enter South, North or No?: ").lower()
    if direction=="north":
        print("Congratulation stage 1 ended! \n")
        print(f"Hey {name} now you are in stage 2: Route  Choice & obstacle  ")
        cross=input("\n Do you want to cross \nthe river or follow the path? \n Enter Yes to cross the river and No to follow the path \n").lower()
        if cross=="no":
            print("Congratulation stage 2 ended! \n")
            print(f"Hey {name} now you are in stage 3: creature interaction & final resolution ")  
            choose=input("\n what do you want to choose? \n Fairy, Ogre or Elf?").lower()
            if choose=="elf":
                print(f"Congratulations {name}, you completed the game! \n \t !!! Game ended !!!")
            elif choose=="ogre" or choose=="fairy":
                print("You choose wrong option game over!!")
            else:
                print("Invalid choice, game ended")
        elif cross=="yes":
            print(f" {name} Crossed the river -- the bridge broke, Game over!!")
        else:
            print("invalid route. Game over!!")
    elif direction=="south":
        print("Wrong direction, game over!!")
    else:
        print("No such direction, Game over !!")



#21
    

def elevator():

    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------- Smart Elevator System ----------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

    print("Welcome to the Smart Elevator System")

    floor=int(input("Enter floor number (0-10): "))

    if floor>=0 and floor<=10:

        weight=int(input("Enter total weight in KG (Max 500KG): "))

        if weight<=500:

            door=input("Is the door fully closed? Enter Yes or No: ").lower()

            if door=="yes":
                print("Activate elevator motion.")
                print("Elevator is moving.")

            elif door=="no":
                print("DISPLAY WARNING: CLOSE THE DOOR.")

            else:
                print("Invalid door status.")

        else:
            print("DISPLAY: OVERWEIGHT! LIFT CANNOT MOVE.")
            print("Maximum allowed weight is 500KG.")

    else:
        print("DISPLAY: INVALID FLOOR.")


wage()
weightConv()
game()
elevator()
