total_number = 0
total_point = 0
count = 0
u = 1.00
v = 2.00
w = 3.00
x = 3.50
y = 4.00
z = 5.00
m = "GPA"
n = "CGPA"

input_point = 0
total_weighted_point = 0
input_first_year_gpa = 0
total_credit = 0
gpa = 0
cgpa = 0
year = 0
no_of_courses = 0
total_weighted_point_one_year = 0
total_credit_one_year = 0
weighted_point = 0
yearly_weighted_point = 0
yearly_total_credit = 0

def course_weighted_point():
    global weighted_point 
    global input_credit
    global input_point
    global yearly_total_credit
    global yearly_weighted_point
    weighted_point = input_credit * input_point
    yearly_weighted_point += weighted_point
    yearly_total_credit += input_credit

def repeat_function_3():
    count = 0
    global no_of_courses
    i = no_of_courses 
    while count < i:
        course_weighted_point()
        count += 1
        
def yearly_gpa():
    global weighted_point
    global input_point
    global input_credit
    global gpa
    global year
    global yearly_weighted_point
    global yearly_total_credit
    gpa_cg = 0
    repeat_function_3()
    gpa_cg = yearly_weighted_point / yearly_total_credit  
    print(f"Your {year} year GPA is: {gpa_cg}")

def repeat_function_1():
    count = 0
    global no_of_courses
    n = no_of_courses 
    while count < n:
        input_course()
        count += 1

def repeat_function_2():
    count = 0
    global no_of_year
    m = no_of_year 
    while count < m:
        input_year()
        count += 1
    
def input_course():
    global input_credit
    global total_credit
    global input_point
    global weighted_point
    global total_weighted_point

    input_name = str(input("Enter your course name in short code: "))
    input_credit = float(input(f"Enter your course credit of {input_name}: "))
    input_point = float(input(f"Enter the grade point you achieved in {input_name}: "))

    course_weighted_point()
    
    total_weighted_point += weighted_point
    total_credit += input_credit

def input_year():
    global your_name
    global total_credit
    global year
    global no_of_courses
    global yearly_weighted_point
    global yearly_total_credit

    year = str(input("Enter the year: "))
    no_of_courses = int(input(f"Enter the no of courses in {year} year: "))

    repeat_function_1()
    yearly_gpa()

def calculate_CGPA():
    global input_first_year_gpa
    global total_weighted_point
    global no_of_courses
    global total_credit
    global cgpa
    global gpa

    cgpa = total_weighted_point / total_credit
    print(f"your CGPA is: {cgpa}")  
    
def main_CGPA():
    global no_of_year

    print("Welcome to CGPA CALCULATOR")
    no_of_year = int(input("Enter how many years' result you want to calculate: "))
    
    repeat_function_2()
    calculate_CGPA()

def repeat_function():
    global no_of_subjects
    global count
    while count < no_of_subjects:
        count += 1
        grade_counter()

def grade_counter():
    global number
    global subject
    global total_number
    global total_point
    
    subject = str(input("Enter the subject name: "))
    number = float(input(f"Enter the marks you get in {subject}: "))

    if  0<= number <33:
        print(f"{subject}:  Failed")
        calculate_GPA()
    elif 33 <= number < 39:
        print(f"{subject}:  D   &  grade point:  {u}" )
        total_point += u
    elif 40 <= number < 49:
        print(f"{subject}:  C   &  grade point:  {v}" )
        total_point += v
    elif 50 <= number < 59:
        print(f"{subject}:  B   &  grade point:  {w}" )
        total_point += w
    elif 60 <= number < 69:
        print(f"{subject}:  A-  &  grade point:  {x}" )
        total_point += x
    elif 70 <= number < 79:
        print(f"{subject}:  A   &  grade point:  {y}" )
        total_point += y
    elif 80 <= number < 100:
        print(f"{subject}:  A+  &  grade point:  {z}" )
        total_point += z
    else:
        print("You have entered an irrelevant number.")

    total_number += number

def calculate_GPA():
    global gpa
    global avg_mark
    global exam_name 
    global total_number
    global total_point
    global no_of_subjects
    global your_name

    gpa = total_point / no_of_subjects
    avg_mark = total_number / no_of_subjects
    print(f"Hello {your_name}")
    print(f"Your GPA in {exam_name} Exam is: {gpa} ")
    print(f"Your average mark is: {avg_mark}")


def main_GPA():
    global exam_name
    global no_of_subjects
    print("Welcome to GPA CALCULATOR")
    print("Which exam result you want to calculate?")
    exam_name = str(input("SSC or HSC?  "))
    no_of_subjects = float(input("Enter the no of subjects: "))
    
    repeat_function()
    calculate_GPA()


def main():
    global GPA_CGPA
    global your_name
    your_name = str(input("Enter your name: "))
    print(f"Hello {your_name} ")
    print("What do you want to calculate?")
    GPA_CGPA = str(input("GPA or CGPA?  "))

    if GPA_CGPA == m:
        main_GPA()
    elif GPA_CGPA == n:
        main_CGPA()
    else:
        print("Please enter GPA or CGPA in block letters.")

main()