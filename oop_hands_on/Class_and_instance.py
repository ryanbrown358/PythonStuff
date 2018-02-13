'''
Created on Feb 11, 2018

@author: ryanb
'''


"""
OOP hands on 

"""

"""Step 1 create the class"""
class Student:
    """this models a student that will contain a name and a grade along with a student count"""
    student_count = 0
    
    def __init__(self, name, grade):
        """initalize attributes to discribe a student"""
        self.name = name
        self.grade = grade
        Student.student_count += 1
    
    """create the displayStudents() method that will print the name and grade of the Student"""
    def displayStudent(self):
        print("Name:", self.name, "\nGrade:", self.grade)
    
    """Now that the class is build we can create instances of the class student"""
    

student1 = Student("Ryan", "Freshman")
student2 = Student("Mike", "Freshman")
student3 = Student("Candace", "Senior") 
student4 = Student("Layla", "Junior")

student1.displayStudent()
student2.displayStudent()
student3.displayStudent()
student4.displayStudent()

print("The total number of students is: ", Student.student_count)
