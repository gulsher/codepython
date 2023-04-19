employee_file = open('emp.txt', "r")

print(employee_file.readable())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()


#write file
employee_files = open('NewEmp.txt', "w")

employee_files.write("\nToby - Intern")

employee_files.close()