#Classes are used for data types beyond the scope of python- boolean, Strings, Numbers - An object on the other hand is what is using the data type
#To import a class use - from fileName import className

from student import classStudent

student1 = classStudent("Pam", 20, "Arts", True)


print(student1.name)