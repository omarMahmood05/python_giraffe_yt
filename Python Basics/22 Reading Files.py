

employee_file = open("0employees.txt", "r") # r stands for read, w stands for write, a will let you read and write but wont let you modify the existing data
for employee in employee_file.readlines():
    print(employee)
employee_file.close() #  ALWAYS CLOSE A FILE AFTER OPENING