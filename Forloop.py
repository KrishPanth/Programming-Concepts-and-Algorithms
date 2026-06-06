for r in range(7):
    for c in range(27):

        # K 
        if c == 0:
            print('*', end='')
        elif c == 1 and r == 3:
            print('*', end='')
        elif c == 2 and (r == 2 or r == 4):
            print('*', end='')
        elif c == 3 and (r == 1 or r == 5):
            print('*', end='')
        elif c == 4 and (r == 0 or r == 6):
            print('*', end='')

        # gap
        elif c == 5:
            print(' ', end='')

        # R 
        elif c == 6:
            print('*', end='')
        elif c == 7 and (r == 0 or r == 3):
            print('*', end='')
        elif c == 8 and (r == 0 or r == 3):
            print('*', end='')
        elif c == 9 and (r == 0 or r == 1 or r == 2 or r == 3 or r == 5 or r == 6):
            print('*', end='')
        elif c == 9 and r == 4:
            print('*', end='')

        # gap
        elif c == 10:
            print(' ', end='')

        # I 
        elif c == 11 and (r == 0 or r == 6):
            print('*', end='')
        elif c == 12:
            print('*', end='')
        elif c == 13 and (r == 0 or r == 6):
            print('*', end='')

        # gap
        elif c == 14:
            print(' ', end='')

        # S 
        elif c == 15 and (r == 1 or r == 2):
            print('*', end='')
        elif c == 16 and (r == 0 or r == 3 or r == 6):
            print('*', end='')
        elif c == 17 and (r == 0 or r == 3 or r == 6):
            print('*', end='')
        elif c == 18 and (r == 0 or r == 4 or r == 5):
            print('*', end='')

        # gap

        elif c == 19:
            print(' ', end='')

        # H 
        elif c == 20:
            print('*', end='')
        elif c == 21 and r == 3:
            print('*', end='')
        elif c == 22 and r == 3:
            print('*', end='')
        elif c == 23 and r == 3:
            print('*', end='')
        elif c == 24:
            print('*', end='')

        else:
            print(' ', end='')

    print()

    # Output- K R I S H



# Q1
for i in range(1, 6):
    if i % 2 == 0:
        print("Number", i, "is even.")
    else:
        print("Number", i, "is odd.")

# Q2
print("-" * 30)
lst = [10, 20, 30, 40]
total = 0
for num in lst:
    total = total + num
    print("Added", num, ". Running total is", total, ".")
print("-" * 30)
print("Total Sum:", total)

# Q3
print("--- Email Greetings Generated ---")
student_names = ["Ram", "Hari", "Sita"]
for name in student_names:
    print("Hi " + name + ", your course approval is ready!")

# Q4
print("--- Book Chapter Summary ---")
pages = [45, 30, 50, 40]
for i in range(len(pages)):
    print("Chapter", i + 1, "has", pages[i], "pages.")

# Q5
lst = [4, 5, 3, 2]
product = 1
for num in lst:
    product = product * num
print("Product:", product)

# Q6
number = 11
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# Q7
lst = [3, 2, 1, 4, 5]
reversed_lst = []
for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])
print("Original:", [3, 2, 1, 4, 5])
print("Reversed:", reversed_lst)

# Q8
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []
for num in list1:
    if num in list2:
        common.append(num)
print("List1:", list1)
print("List2:", list2)
print("Common:", common)

# Q9
lst = [1, 2, 3, 4]
for i in range(len(lst)):
    if i == 0 or i == len(lst) - 1:
        print(lst[i])

# Q10
text = "Hello World"
vowels = "aeiouAEIOU"
result = ""
for ch in text:
    if ch not in vowels:
        result = result + ch
print("Original:", text)
print("Without vowels:", result)

# Q11
sentence = 'Loops are Fun'
vowels_count = 0
consonants_count = 0
vowels = "aeiouAEIOU"
for ch in sentence:
    if ch.isalpha():
        if ch in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
print("Vowels:", vowels_count)
print("Consonants:", consonants_count)

# Q12
lst = [1, 2, 3, 4, 5]
odd = []
even = []
for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Odd:", odd)
print("Even:", even)

# Q13
number = 17
is_prime = True
if number < 2:
    is_prime = False
for i in range(2, number):
    if number % i == 0:
        is_prime = False
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

# Q14
lst = [1, 2, 3, 4, "a", "b"]
int_list = []
str_list = []
for item in lst:
    if type(item) == int:
        int_list.append(item)
    else:
        str_list.append(item)
print("Integers:", int_list)
print("Strings:", str_list)

# Q15
text = "Hello123"
digits = 0
letters = 0
for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
print("Letters:", letters)
print("Digits:", digits)

# Q16
username = "admin"
password = "pass123"
valid_username = "admin"
valid_password = "pass123"
if username == valid_username and password == valid_password:
    print("Login successful!")
else:
    print("Invalid username or password.")

# Q17
number = 7
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# Q18
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print("Factorial of", number, "is", factorial)

# Q19
for i in range(1, 9):
    print("--- Table of", i, "---")
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

# Q20
lst = [1, 2, 3, 4]
for i in range(len(lst)):
    if i == 0 or i == 1:
        print(lst[i])

# Q21
total = 0
for i in range(1, 21):
    if i % 2 != 0:
        total += i
print("Sum of odd numbers:", total)

# Q22
total = 0
for i in range(1, 21):
    if i % 2 == 0:
        total += i
print("Sum of even numbers:", total)

# Q23
text = "Loops are Fun in Python"
count = 0
for ch in text:
    if ch == ' ':
        count += 1
print("Number of spaces:", count)

# Q24
lst = [1, 2, 3, 4]
result = []
for num in lst:
    result.append(num ** 3)
print("Result:", result)

# Q25
a = "programming"
result = ""
for ch in a:
    result = ch + result
print("Original:", a)
print("Reversed:", result)

# Q26
for i in range(50):
    print(i)
    if i == 7:
        break

# Q27
text = "Python"
for ch in text:
    print(ch)

# Q28
a = ["ram", "shyam", 1, 2]
for item in a:
    if type(item) == str:
        print("Hello!" + item)

# Q29
a = ["ram", "shyam", 1, 2]
lst = []
for item in a:
    lst.append("Dr." + str(item))
print(lst)

# Q30
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print("Squares:", squares)

# Q31
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
new_list = []
for num in lst1:
    if num > 0:
        new_list.append(num)
print("Positive numbers:", new_list)

# Q32
lst = [0, 1, 2, 3, 4, 5, 6]
for num in lst:
    if num == 3 or num == 6:
        continue
    print(num)

# Q33
lst1 = [1, "hello", 3.5, True]
lst2 = []
for item in lst1:
    lst2.append(type(item))
print("Types:", lst2)

# Q34
for i in range(1, 4):
    print(i)
else:
    print("Done")

# Q35
for i in range(105, 6, -7):
    print(i, end=' ')
print()

# Q36
bad_chars = [';', ':', '!', '*', ' ']
string = "py;th* o:n ! ;py * t*h:o !n"
result = ""
for ch in string:
    if ch not in bad_chars:
        result += ch
print("Result:", result)

# Q37
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even count:", even_count)
print("Odd count:", odd_count)

# Q38
total = 0
for i in range(3, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("Sum:", total)

# Q39
even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)

# Q40
numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2
count = 0
for num in numbers:
    if num == target:
        count += 1
print("Number", target, "appears", count, "times.")