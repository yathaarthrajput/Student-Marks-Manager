Subjects = ["Physics", "Chemistry", "Math", "English", "Computer Science"]

students = [
    {"roll_no": 1, "name": "Ashish", "class": 10, "marks": {"Physics": 85, "Chemistry": 90, "Math": 95, "English": 88, "Computer Science": 92}},
    {"roll_no": 2, "name": "Ram", "class": 12, "marks": {"Math": 70}},
    {"roll_no": 3, "name": "Shyam", "class": 12, "marks": {"Physics": 60, "English": 75}},
    {"roll_no": 4, "name": "Sita", "class": 12, "marks": {"Chemistry": 55, "Computer Science": 65}},
    {"roll_no": 5, "name": "Gita", "class": 12, "marks": {"Physics": 95, "Chemistry": 85, "Math": 80, "English": 90, "Computer Science": 88}}
]


def getClass(allowAll = False):
    """Prompts for a class number (1-12) or 'ALL' and validates input."""
    while True:
        inp = input("Enter class (1-12" + (", or ALL" if allowAll else "") + "): ")
        if allowAll and inp.upper() == "ALL":
            return "ALL"
        if inp.isdigit():
            num = int(inp)
            if 1 <= num <= 12:
                return num
        print("Oops, wrong input. Please try again.")

def getMarks():
    """Prompts for marks (0-100) or 'NO' and validates input."""
    while True:
        mark = input("Enter marks (0-100 or NO): ")
        if mark.upper() == "NO":
            return None
        if mark.isdigit():
            m2 = int(mark)
            if 0 <= m2 <= 100:
                return m2
        print("Invalid marks! Must be between 0 and 100.")

def findStudent(cls, r):
    """Finds a student by class and roll number."""
    for st in students:
        if st["class"] == cls and st["roll_no"] == r:
            return st
    return None

def rollExists(cls, roll):
    """Checks if a roll number exists in a given class."""
    for x in students:
        if x["class"] == cls and x["roll_no"] == roll:
            return True
    return False

def addStudent():
    """Adds a new student to the system."""
    cls = getClass()
    while True:
        try:
            rn = int(input("Enter roll number: "))
            if rollExists(cls, rn):
                print("This roll number already exists. Please choose another.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    nm = input("Enter name of student: ")
    marks = {}
    print("Now enter marks (or type NO):")
    for sb in Subjects:
        mk = getMarks()
        if mk is not None:
            marks[sb] = mk

    if not marks:
        print("You must enter at least one subject. Student not added.")
        return

    newStu = {"roll_no": rn, "name": nm, "class": cls, "marks": marks}
    students.append(newStu)
    print("Student added successfully!")

def deleteStudent():
    """Deletes a student from the system."""
    c = getClass()
    try:
        rr = int(input("Enter roll number to delete: "))
    except ValueError:
        print("Invalid input.")
        return
    stu = findStudent(c, rr)
    if stu:
        students.remove(stu)
        print("Student deleted, Request Successful!")
    else:
        print("Student not found!")

def editStudent():
    """Edits student details based on user choice."""
    print("What do you want to edit?")
    print("1-Class")
    print("2-Roll No")
    print("3-Name")
    print("4-Marks")
    choice = input("Enter choice: ")

    cls = getClass()
    try:
        rn = int(input("Enter roll number: "))
    except ValueError:
        print("Invalid roll number input.")
        return
    stu = findStudent(cls, rn)
    if not stu:
        print("Student does not exist.")
        return

    if choice == "1":
        nc = getClass()
        if rollExists(nc, rn):
            print("A student with this roll number already exists in the new class.")
        else:
            stu["class"] = nc
            print("Class changed successfully.")
    elif choice == "2":
        try:
            nr = int(input("Enter new roll number: "))
            if rollExists(cls, nr):
                print("This roll number is already used in the current class.")
            else:
                stu["roll_no"] = nr
                print("Roll number updated.")
        except ValueError:
            print("Invalid input.")
    elif choice == "3":
        newName = input("Enter new name: ")
        stu["name"] = newName
        print("Name updated.")
    elif choice == "4":
        print("Subjects list:")
        for i, subj_name in enumerate(Subjects, 1):
            print(f"{i}. {subj_name}")
        try:
            sc = int(input("Pick subject number: "))
            if 1 <= sc <= len(Subjects):
                subj = Subjects[sc - 1]
                val = getMarks()
                if val is not None:
                    stu["marks"][subj] = val
                    print(f"Marks updated for {subj}.")
                else:
                    if subj in stu["marks"]:
                        del stu["marks"][subj]
                        print(f"Marks for {subj} deleted.")
            else:
                print("Invalid subject number.")
        except ValueError:
            print("Invalid input.")
    else:
        print("Invalid option.")

def showAll():
    """Displays all students in a formatted table."""
    print("\n" + "="*80)
    print(f"{'Class':<8} {'Roll':<8} {'Name':<20} {'Marks'}")
    print("="*80)
    for s in students:
        marks_str = ", ".join([f"{subj}: {mark}" for subj, mark in s["marks"].items()])
        print(f"{s['class']:<8} {s['roll_no']:<8} {s['name']:<20} {marks_str}")
    print("="*80)

def subjectStats():
    """Calculates and displays statistics for a chosen subject."""
    for i, subj_name in enumerate(Subjects, 1):
        print(f"{i}. {subj_name}")
    try:
        ch = int(input("Enter subject number: "))
    except ValueError:
        print("Invalid input.")
        return

    if not (1 <= ch <= len(Subjects)):
        print("Invalid subject number.")
        return
    
    sub = Subjects[ch - 1]
    c = getClass(True)
    
    marks_list = [
        s["marks"][sub] for s in students
        if sub in s["marks"] and (c == "ALL" or s["class"] == c)
    ]
    
    if not marks_list:
        print("No data found for this subject and class.")
    else:
        avg = sum(marks_list) / len(marks_list)
        print(f"Maximum mark: {max(marks_list)}")
        print(f"Average mark: {avg:.2f}")

def classStats():
    """Calculates and displays statistics for a chosen class."""
    c = getClass()
    student_stats = []
    
    for s in students:
        if s["class"] == c:
            num_subjects = len(s["marks"])
            if num_subjects > 0:
                total_marks = sum(s["marks"].values())
                avg_marks = total_marks / num_subjects
                student_stats.append(avg_marks)
    
    if not student_stats:
        print(f"No students found in class {c}.")
    else:
        print(f"Class {c} statistics:")
        print(f"Highest student average: {max(student_stats):.2f}")
        print(f"Class average: {sum(student_stats) / len(student_stats):.2f}")



def menu():
    """The main menu loop for the student management system."""
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add or Delete Student")
        print("2. Edit Student Details")
        print("3. Show All Students")
        print("4. Subject Statistics")
        print("5. Class Statistics")
        print("6. Exit")

        c = input("Enter option: ")
        if c == "1":
            xx = input("1-Add  2-Delete: ")
            if xx == "1":
                addStudent()
            elif xx == "2":
                deleteStudent()
            else:
                print("Invalid option.")
        elif c == "2":
            editStudent()
        elif c == "3":
            showAll()
        elif c == "4":
            subjectStats()
        elif c == "5":
            classStats()
        elif c == "6":
            print("THANKS FOR COMING, CREATED BY YATHAARTH RAJPUT!")
            break
        else:
            print("Invalid menu choice!")

if __name__ == "__main__":
    menu()
