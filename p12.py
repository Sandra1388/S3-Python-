'''
Create class Student with attributes name, roll_number, and course.
Define an __init__ method to initialize these attributes and a method display() to print them.
'''

class student:
    def __init__(self, name, course, roll):
        self.name = name
        self.course = course
        self.roll = roll
    def disp(self):
        print("Name: ",self.name)
        print("Course: ",self.course)
        print("ROll.Number: ",self.roll)

name = input("Enter name:")
course = input("Enter course:")
roll = int(input("Enter roll number:"))
std = student(name,course,roll) 
std.disp()
