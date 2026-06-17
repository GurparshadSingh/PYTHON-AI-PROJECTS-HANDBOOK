class Student:

    students=[]
    def __init__(self,name,id,marks):
        self.name=name
        self.id=id
        self.marks=marks
        Student.students.append(self)
    def __str__(self):
        return f"Name:{self.name},ID:{self.id},Marks:{self.marks}"   
    #! display all students
    @classmethod
    def view_all(cls):
        for student in cls.students:
            print(student)
            
    #! display student with any parameter be it id or be it name
    @classmethod
    def search_student(cls):
        search = input("Enter name or id of student: ")

        found = False
        for student in cls.students:
            if student.name.lower() == search.lower() or str(student.id) == search:
                print(student)
                found = True

        if not found:
            print("Student not found")
            
            
        
    #! enter a new student in students
    @classmethod
    def enter_new(cls):
        name = input("Enter student name: ")
        student_id = int(input("Enter student id: "))
        marks = int(input("Enter marks of student: "))
        if marks<0:
            raise ValueError("Marks cannot be negative")
        for student in cls.students:
            if student.id == student_id:
                print("Student ID already exists!")
                return

        Student(name, student_id, marks)

        print("Student added successfully")
        
    #! update marks of any student
    @classmethod
    def update_marks(cls):
            student_id = int(input("Enter student id: "))
            updated = False
            for student in cls.students:
                if student.id == student_id:
                    student.marks = int(input("Enter new marks: "))
                    updated =True

            if updated:
                print("Marks updated successfully")
            else:
                print("No student found with those marks")
                
    #!delete a student with any parameter
    @classmethod
    def delete_with(cls):
                search_key = input("Enter key (name/id/marks): ").strip()
                search_value = input("Enter value to delete: ").strip()

                deleted = False

                for student in cls.students[:]:  # shallow copy of list
                    if hasattr(student, search_key):
                        if str(getattr(student, search_key)).lower() == search_value.lower():
                            cls.students.remove(student)
                            deleted = True

                if deleted:
                    print("Success! Updated list:")
                    print(cls.view_all())
                else:
                    print("No matching student found.")
                    
    #! find student with max marks
    @classmethod
    def find_max_marks(cls):
        if not cls.students:
            print("No students found")
            return

        topper = cls.students[0]

        for student in cls.students:
            if student.marks > topper.marks:
                topper = student

        print("Topper:")
        print(topper)
        
Student("Alice", 1, 10)
Student("Bob", 2, 20)
Student("Charlie", 3, 30)

while True:
    print("""
1. View All Students
2. Search Student
3. Add Student
4. Update Marks
5. Delete Student
6. Find Topper
7. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        Student.view_all()

    elif choice == "2":
        Student.search_student()

    elif choice == "3":
        Student.enter_new()

    elif choice == "4":
        Student.update_marks()

    elif choice == "5":
        Student.delete_with()

    elif choice == "6":
        Student.find_max_marks()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")