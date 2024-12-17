# Task 1: List - Student Grades
# Write a Python program that stores student grades 
# in a list and calculates the average grade. If the 
# average is above 50, print "Pass"; otherwise, print "Fail.


class studentGrade:
    def __init__(self):
        self.list_marks = []
        self.total = 0

    def marks_input(self):
        for i in range(5):
            marks = int(input("enter marks: "))
            if marks < 0 or marks > 100:
                print("invalid")
                break
            self.list_marks.append(marks)
            self.total += marks
        # print(self.list_marks, self.total)
    
    def pass_fail(self):
        average = self.total/5
        if average >= 50:
            print("PASS")
        else:
            print("FAIL")



student = studentGrade()
student.marks_input()
student.pass_fail()

