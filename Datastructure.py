# 1. 

contacts = {"krrish": "krrish@email.com"}
name = input("Enter name: ")
print(contacts.get(name, "contact not found"))


#2. 

shopping_list = {"Milk", "Bread", "Eggs"}
bought = {"Bread", "Eggs"}
remaining = shopping_list - bought
print(remaining if remaining else "Shopping complete")

# 3. 

class_list = ["ram", "sita", "laxman"]
new_student = input("Enter student name: ")
if new_student in class_list:
    print("Already present")
else:
    class_list.append(new_student)
    print("Student added:", class_list)



# 4. 

votes = ["Blue", "Red", "Blue", "Green", "Blue"]
count = votes.count("Blue")
print("Blue wins" if count >= 3 else "Blue did not win")



# 5. 

grades = {"Ram": 92, "Sita": 88}
name = input("Enter student name: ")
print(grades[name] if name in grades else "Grade is not available")



# 6. 

pythonapplicant = {"name": "Priya", "skills": ["Java", "SQL"], "experience_years": 1}
required_skills = {"Python", "Java"}
has_skill = any(s in required_skills for s in applicant["skills"])
if has_skill and applicant["experience_years"] >= 2:
    print("priya qualifies")
else:
    print("priya does not qualify")



# 7. 

banned_items = {"scissors", "knife", "lighter"}
weight = float(input("Enter baggage weight (kg): "))
item = input("Enter item name: ").lower()
if weight <= 7 and item not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")


#8.

ram_items = {"pen", "book", "ruler"}
laxman_items = {"pencil", "eraser", "bag"}
if ram_items.isdisjoint(laxman_items):
    print("they picked completely different items")
else:
    print("they have some common items")


# 9.

ram_items = {"pen", "book", "ruler"}
laxman_items = {"pencil", "eraser", "bag"}
if ram_items.isdisjoint(laxman_items):
    print("they picked completely different items")
else:
    print("they have some common items")


# 10.

data_list = [10, 20, 30]
data_tuple = (10, 20, 30)
data_set = {10, 20, 30}
data_dict = {'a': 1, 'b': 2}
val = 20

if val in data_list and val in data_tuple:
    if 'b' in data_dict and val not in data_set:
        print("Path A")
    else:
        print("Path B")
else:
    print("Path C")



# 11.

data = {'a': 10, 'b': 20, 'a': 30}
print(data)


# 12.

d = {}
d[10.5] = "float"      
d[(1,2,3)] = "tuple"    
d['key'] = "string"     
d[[1,2,3]] = "list"     

# 13.

d = {'val': 10}
if d.get('score'):
    print('Found')
else:
    print('Not Found')


# 14.

items = [10, 10, 20]
print(len(set(items)))

# 15.

my_set = {10, 20, 30}
my_set.add(40)
print(my_set)


# 16.

menu = {"Pizza": 15, "Burger": 10, "Salad": 8}
order = "Pizza"
if order in menu:
    print(menu[order])
else:
    print("item not found")


# 17. 

student_data = {"name": "Sam", "score": 85}
if student_data["score"] >= 80:
    student_data["status"] = "Pass"
else:
    student_data["status"] = "Review"
print(student_data)


# 18.


database = {"admin": "1234", "user": "abcd"}
user_input = 'admin'
user_pass = '1234'
if user_input in database and database[user_input] == user_pass:
    print("Login Successful")
else:
    print("Login Failed")


# 19.

emails = ['ram123@gmail.com', 'hari77@gmail.com']
blacklisted_emails = {'hari77@gmail.com'}
current_email = 'hari77@test.com'
if current_email in emails and current_email not in blacklisted_emails:
    print("Email Sent")
else:
    print("Blocked")


# 20.

inventory = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target = 'B2'
if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("dispatch item")
    else:
        print("stock error")
else:
    print("invalid zone")


# 21.


valid_courses = {"python", "robotics", "java"}
hs_grades = list(range(9, 13))

name = input("Enter name: ")
course = input("Enter course: ").lower()
grade = int(input("Enter grade: "))

student_records = {"name": name, "course": course, "grade": grade}

if course not in valid_courses:
    print(f"{name} selected an invalid course")
elif grade < 9:
    print("grade too low")
elif grade > 12:
    print("grade too high")
elif course == "robotics" and grade == 9:
    print(f"{name} is not eligible for {course} grade too low")
else:
    print(f"{name} is approved for {course}")