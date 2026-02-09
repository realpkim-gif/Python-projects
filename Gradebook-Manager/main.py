import pandas as pd
import numpy as np


# DataFrame: Name, Grades (list), Average
students = pd.DataFrame(columns=["Name", "Grades", "Average"])

def save():
    if students.empty:
        print("No students to save.")
        return

    filename = input("Enter filename (without .csv): ").strip()
    students.to_csv(filename + ".csv", index=False)
    print("Saved students to "+ filename+".csv")

# Update averages
def update_average():
    if len(students) == 0:
        print("No students, no average calculated:\n")
        return

    # Calculate average from the list of grades for each student
    for i in students.index:
        grades = students.loc[i, "Grades"]
        if grades:
            students.loc[i, "Average"] = np.mean(grades)
        else:
            students.loc[i, "Average"] = np.nan

    print(students)
    print("\n")

# Add a new student with a first grade
def add():
    name = input("Student Name: ")
    grade = float(input("Student First Grade: "))

    print("\n" * 100)

    students.loc[len(students)] = [name, [grade], np.nan]
    update_average()


# Edit an existing student: add new grade or change name
def edit_student():
    ask = input("Student's name: ")
    found = students.loc[students["Name"] == ask]

    if found.empty:
        print("Student not found.")
        return


    print(found)
    change = input(
        "What would you like to do?\n"
        "1 - Change name\n"
        "2 - Add a new grade\n"
        "3 - Edit an existing grade\n"
        "4 - Delete existing grade\n"
        "5 - Delete student\n"
        "6 - Return\n"
    )

    print("\n" * 100)

    if change == "1":
        new_name = input("New name: ")
        locate= students[students["Name"] == ask].index[0]
        students.loc[locate, "Name"] = new_name
        print("Name updated.")

    elif change == "2":
        new_grade = float(input("New grade: "))
        locate = students[students["Name"] == ask].index[0]
        students.loc[locate, "Grades"].append(new_grade)
        update_average()
        print("Grade added.")

    elif change == "3":  # Edit an existing grade
        student_index = students.index[students["Name"] == ask]

        if len(student_index) == 0:
            print("Student not found.")
            return

        # first (and only) matching row
        grades = students.loc[student_index[0], "Grades"]

        if not grades:
            print("No grades to edit.")
            return


        print("Current existing grades:", grades)
        edit = int(input("Enter the position (1-" + str(len(grades)) + ") of the grade to change: ")) - 1

        if 0 <= edit < len(grades):
            new_grade = float(input("Enter the new grade: "))
            grades[edit] = new_grade
            update_average()
            print("Grade updated.")
        else:
            print("Invalid position.")

    elif change == "4":  # Delete an existing grade
        student_index = students.index[students["Name"] == ask]

        if len(student_index) == 0:
            print("Student not found.")
            return

        i = student_index[0]
        grades = students.loc[i, "Grades"]

        if not grades:
            print("No grades to delete.")
            return

        print("Current grades:", grades)
        deleted = int(input("Enter the position (1-" + str(len(grades)) + ") of the grade to delete: ")) - 1

        if 0 <= deleted < len(grades):
            removed = grades.pop(deleted)
            print("Removed grade:", removed)
            update_average()
        else:
            print("Invalid position.")
    elif change == "5":
        students.drop(students[students["Name"] == ask].index[0], inplace=True)
        students.reset_index(drop=True, inplace=True)

        print("Student deleted.")

    elif change == "6":
        list_show()

    else:
        print("Invalid choice.")

# Show all students
def list_show():
    if students.empty:
        print("No students available.")
        return
    print(students)

# Main menu
def main():

    print(students)

    while True:
        print("\n1. Add a New Student")
        print("2. Edit an Existing Student (including grade)")
        print("3. Show name list")
        print("4. Exit")
        print("5. Save gradebook to file")


        choice = input("Choose an option: ")
        print("\n"*100)

        if choice == "1":
            add()
        elif choice == "2":
            edit_student()
        elif choice == "3":
            list_show()
        elif choice == "4":
            break
        elif choice == "5":
            save()

        else:
            print("Invalid choice")
main()
