# Week 3 / Lesson 4: Task

# 1. Write a program to check whether the given number is in between 1 and 100 or not.


# user_input=int(input('Enter a number: '))
# if 1 <= user_input <= 100:
#     print("Number is between 1 and 100")
# else:
#     print("Number is not between 1 and 100")


# 2 Check whether the user input number is even or odd and display it to user.   

# num= int(input("Enter the number"))
# if num %2 ==0: 
#     print(num, "Is Even")
# else:
#     print(num, "is odd")

#  3. Write a program that asks the user for a number in the range of 1 to 12. 
#        The program should display the corresponding month, where 
#        1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 
#        8=august,9=september,10=october,11=november,12=december. The program should display an error 
#        message if the user enters a number that is outside the range of 1 to 12.   


# month = ("January","February","March","April","May","June",
#          "July","August","September","October","November","December")
# num = int(input("Enter a number (1-12): "))
# if 1 <= num <= 12:
#     print(f"Month: {month[num - 1]}")
# else:
#     print("Error: Number must be between 1 and 12.")

# 4. A school has following rules for grading system:
#         a. Below 25 - F
#         b. 25 to 45 - E
#         c. 45 to 50 - D
#         d. 50 to 60 - C
#         e. 60 to 80 - B
#         f. Above 80 - A
#         Ask user to enter marks and print the corresponding grade.


# print("\n=== Exercise 4 ===")
# marks = float(input("Enter marks: "))
# if marks < 25:
#     grade = "F"
# elif marks < 45:
#     grade = "E"
# elif marks < 50:
#     grade = "D"
# elif marks < 60:
#     grade = "C"
# elif marks <= 80:
#     grade = "B"
# else:
#     grade = "A"
# print(f"Grade: {grade}")


# 5. Write a program to check whether a number is divisible by 7 or not.

# print("\n--- 5. Divisible by 7 ---")
# num = int(input("Enter a number: "))
# if num % 7 == 0:
#     print(f"{num} is divisible by 7.")
# else:
#     print(f"{num} is NOT divisible by 7.")
 

# 6. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
#             Like:
#             Enter First Number: 7
#             Enter Second Number : 9
#             Enter operator : +
#             Your Answer is : 16


# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print("""
# _______________________________________
#       Operators List:
#       1. Addition       (+)
#       2. Subtraction    (-) 
#       3. Division       (/)
#       4. Multiplication (*)
# """)
# op=int(input(" Choose any one option: "))
# if op==1:
#     print(a+b)
# elif op==2:
#     print(a-b)
# elif op==3:
#     if a==0 or b==0:
#         print("Number Cannot Be divided by 0")
#     else:
#         print(float(a/b))
# elif op==4:
#     print(a*b)
# else:
#     print("Invalid Option!!!!")




# 7. Write a Python program to check car loan eligibility:
# Salary >= 50,000 and Credit Score >= 700: "Eligible"
# Otherwise: "Not Eligible"

# print("\n--- 7. Car Loan Eligibility ---")
# salary = int(input("Enter your salary: "))
# credit_score = int(input("Enter your credit score: "))
# if salary >= 50000 and credit_score >= 700:
#     print("Eligible")
# else:
#     print("Not Eligible")




# 8. Write a Python program that takes an integer input n n. 
#         From given number, 
#         check if it is divisible by both 3 and 5, and print "FizzBuzz" 
#         if true. 
#         If the number is divisible only by 5, print "Buzz." If it is 
#         divisible only by 3, print "Fizz." 
#        Finally, if the number is not divisible by either 3 or 5, 
#          print the number itself.

# print("\n--- 8. FizzBuzz ---")
# n = int(input("Enter a number: "))
# if n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
# elif n % 5 == 0:
#     print("Buzz")
# elif n % 3 == 0:
#     print("Fizz")
# else:
#     print(n)



# 9. Write a Python program that takes a character input and checks whether it is a vowel or consonant.

# print("\n--- 9. Vowel or Consonant ---")
# char = input("Enter a character: ").lower()
# if char in "aeiou":
#     print(f"'{char}' is a Vowel.")
# elif char.isalpha():
#     print(f"'{char}' is a Consonant.")
# else:
#     print("Invalid input. Please enter a letter.")



# 10. Write a Python program to input marks and determine the grade based on the following conditions:
# 90-100: A
# 80-89: B
# 70-79: C
# Below 70: Fail



# print("\n--- 10. Grade (100-scale) ---")
# marks = int(input("Enter marks (0-100): "))
# if 90 <= marks <= 100:
#     print("Grade: A")
# elif 80 <= marks <= 89:
#     print("Grade: B")
# elif 70 <= marks <= 79:
#     print("Grade: C")
# else:
#     print("Grade: Fail")



# 11. Write a Python program to categorize a person’s age:
# Age < 13: Child
# 13 <= Age <= 19: Teenager
# Age > 19: Adult


# print("\n--- 11. Age Category ---")
# age = int(input("Enter age: "))
# if age < 13:
#     print("Child")
# elif 13 <= age <= 19:
#     print("Teenager")
# else:
#     print("Adult")



# 12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.

# print("\n--- 12. Character Type ---")
# char = input("Enter a character: ")
# if char.isupper():
#     print(f"'{char}' is Uppercase.")
# elif char.islower():
#     print(f"'{char}' is Lowercase.")
# elif char.isdigit():
#     print(f"'{char}' is a Digit.")
# else:
#     print("Invalid input.")


# 13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and outputs the corresponding action ("Stop", "Get Ready", "Go").

# print("\n--- 13. Traffic Light ---")
# color = input("Enter color (Red/Yellow/Green): ").capitalize()
# if color == "Red":
#     print("Stop")
# elif color == "Yellow":
#     print("Get Ready")
# elif color == "Green":
#     print("Go")
# else:
#     print("Invalid color.")

# 14. Write a Python program to check eligibility for a job based on age and experience:
# Age > 18 and Experience >= 2 years: Eligible
# Otherwise: Not Eligible

# print("\n--- 14. Job Eligibility ---")
# age = int(input("Enter your age: "))
# experience = int(input("Enter years of experience: "))
# if age > 18 and experience >= 2:
#     print("Eligible")
# else:
#     print("Not Eligible")


# 15. Write a Python program to give advice based on the temperature:
# Temperature > 30°C: "It's hot, stay hydrated!"
# Temperature between 15-30°C: "Enjoy the weather!"
# Temperature < 15°C: "It's cold, wear warm clothes!"

# print("\n--- 15. Temperature Advice ---")
# temp = float(input("Enter temperature (°C): "))
# if temp > 30:
#     print("It's hot, stay hydrated!")
# elif 15 <= temp <= 30:
#     print("Enjoy the weather!")
# else:
#     print("It's cold, wear warm clothes!")

# 16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
# Pizza: $10
# Burger: $7
# Pasta: $8

# item = input("Enter item (Pizza/Burger/Pasta): ").capitalize()
# if item == "Pizza":
#     print("Price: $10")
# elif item == "Burger":
#     print("Price: $7")
# elif item == "Pasta":
#     print("Price: $8")
# else:
#     print("Item not found in menu.")

# 17. Write a Python program to select players based on height:
# Height >= 6 feet: Selected
# Height < 6 feet: Not Selected

# print("\n--- 17. Player Selection ---")
# height = float(input("Enter height (in feet): "))
# if height >= 6:
#     print("Selected")
# else:
#     print("Not Selected")


# 18. Write a Python program to check if a person is eligible to watch a movie based on their age:
# Age >= 18: Allowed
# Age < 18: Not Allowed

# print("\n--- 18. Movie Eligibility ---")
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Allowed")
# else:
#     print("Not Allowed")

# 19. Write a Python program to check login credentials:
# Username: "admin", Password: "password123"
# If correct, print "Access Granted"; otherwise, print "Access Denied."

# print("\n--- 19. Login Check ---")
# username = input("Enter username: ")
# password = input("Enter password: ")
# if username == "admin" and password == "password123":
#     print("Access Granted")
# else:
#     print("Access Denied")

# 20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:
# 12, 1, 2: "Winter"
# 3, 4, 5: "Spring"
# 6, 7, 8: "Summer"
# 9, 10, 11: "Autumn"


# print("\n--- 20. Season ---")
# month = int(input("Enter month number (1-12): "))
# if month in [12, 1, 2]:
#     print("Winter")
# elif month in [3, 4, 5]:
#     print("Spring")
# elif month in [6, 7, 8]:
#     print("Summer")
# elif month in [9, 10, 11]:
#     print("Autumn")
# else:
#     print("Invalid month number.")
  























