from Student import Student

student1 = Student("Jim","cse","8.2",True)
student2 = Student("Sai","ece","5.2",False)
student3 = Student("James","eee","3.2",False)

print(student1.name, student1.gpa)
print(student2.name, student2.gpa)
print(student3.graduate())