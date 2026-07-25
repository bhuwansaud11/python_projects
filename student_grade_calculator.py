import json
import os
class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self):
        grade = int(input("Enter the grade: "))
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def highest(self):
        if not self.grades:
            return None
        return max(self.grades)

    def lowest(self):
        if not self.grades:
            return None
        return min(self.grades)

    def display(self):
        avg = self.average()
        high = self.highest()
        low = self.lowest()
        print("--------------------------")
        print("---Student Overview---")
        print(f"Name: {self.name}")
        print(f"Average: {avg}")
        print(f"Highest Grade: {high}")
        print(f"Lowest Grade: {low}")

    def to_dict(self):
        return {
            "Name":self.name,
            "Grades":self.grades
        }
    
    @classmethod
    def from_dict(cls,data):
        Student = cls(data['Name'])
        Student.grades = data['Grades']
        return Student
students = []
filename = "Projects\student_grade_calculator.json"
def main():
    load_students()
    is_running = True
    while is_running:

        print("----------------------------")
        print("---STUDENT GRADE CALCULATOR---")
        print("1. Add a student")
        print("2. Add a grade to the existing student.")
        print("3. View student details")
        print("4. Exit")

        choice = int(input("Choose(1-4): "))
        match choice:
            case 1:
                name = input("Enter the name of the student: ")
                students.append(Student(name))
                save_details()
                
            case 2:
                for i,student in enumerate(students,1):
                    print(f"{i}. {student.name}")
                ask = int(input("Enter the student's sno: "))
                
                if ask>len(students):
                    print("Invalid choice. Try again.")
                    continue
                no_of_grades = int(input("Enter the # of Grades: "))
                for i in range(no_of_grades):
                    students[ask-1].add_grade()
                save_details()
                
            case 3:
                for i,student in enumerate(students,1):
                    print(f"{i} {student.name}")
                ask = int(input("Enter the student's num to view details: "))   
                if ask>len(students):
                    print("Invalid choice. Try again.")
                    continue
                students[ask-1].display()


            case 4:
                
                print("Thanks for visiting me...")
                print("Exiting...")
                is_running = False
            

            case _:
                print("Invalid choice. Please try again.")

def save_details():
    
    with open(filename,'w') as file:
        json.dump([student.to_dict() for student in students],file,indent=4)

def load_students():
    global students
    if os.path.exists(filename):
        with open(filename,'r') as file:
            data = json.load(file)
            students = [Student.from_dict(s) for s in data]
    

main()



