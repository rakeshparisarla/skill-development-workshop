students = {} 
sections = set()
students['101'] = {'name': 'Alice Johnson', 'age': 16, 'marks': (85, 90, 88), 'section': 'A'}
students['102'] = {'name': 'Bob Smith', 'age': 17, 'marks': (78, 82, 80), 'section': 'B'}
students['103'] = {'name': 'Charlie Brown', 'age': 15, 'marks': (92, 89, 91), 'section': 'A'}
sections.update(['A', 'B'])
def add_student():
    try:
        roll = input("Enter Roll Number: ").strip()
        if roll in students:
            print("Roll Number already exists!")
            return
        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        marks1 = int(input("Enter Marks for Subject 1: "))
        marks2 = int(input("Enter Marks for Subject 2: "))
        marks3 = int(input("Enter Marks for Subject 3: "))
        marks = (marks1, marks2, marks3)
        section = input("Enter Section: ").strip()
        students[roll] = {'name': name, 'age': age, 'marks': marks, 'section': section}
        sections.add(section)
        print("Student added successfully!")
    except ValueError:
        print("Invalid input! Please enter correct data types.")
def display_all_students():
    if not students:
        print("No students to display.")
        return
    for roll, details in students.items():
        total_marks = sum(details['marks'])
        print(f"Roll: {roll}, Name: {details['name']}, Age: {details['age']}, Marks: {details['marks']}, Total: {total_marks}, Section: {details['section']}")
def search_student():
    roll = input("Enter Roll Number to search: ").strip()
    if roll in students:
        details = students[roll]
        total_marks = sum(details['marks'])
        print(f"Roll: {roll}, Name: {details['name']}, Age: {details['age']}, Marks: {details['marks']}, Total: {total_marks}, Section: {details['section']}")
    else:
        print("Student not found!")
def remove_student():
    roll = input("Enter Roll Number to remove: ").strip()
    if roll in students:
        section = students[roll]['section']
        del students[roll]
        if not any(s['section'] == section for s in students.values()):
            sections.discard(section)
        print("Student removed successfully!")
    else:
        print("Student not found!")
def show_class_topper():
    if not students:
        print("No students to find topper.")
        return
    topper = max(students.items(), key=lambda x: sum(x[1]['marks']))
    roll, details = topper
    total_marks = sum(details['marks'])
    print(f"Class Topper: Roll: {roll}, Name: {details['name']}, Total Marks: {total_marks}")
def display_unique_sections():
    if not sections:
        print("No sections to display.")
        return
    print("Unique Sections:", ', '.join(sections))
def main():
    while True:
        print("\nSchool Data Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Roll Number")
        print("4. Remove Student by Roll Number")
        print("5. Show Class Topper")
        print("6. Display Unique Sections")
        print("7. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_student()
            elif choice == 2:
                display_all_students()
            elif choice == 3:
                search_student()
            elif choice == 4:
                remove_student()
            elif choice == 5:
                show_class_topper()
            elif choice == 6:
                display_unique_sections()
            elif choice == 7:
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    main()
