import PersonClass
from PersonClass import Student
from PersonClass import Teacher
from PersonClass import Person

student1 = Student("Bob", 15, "170cm", "Male")
student1.student_profile()

teacher1 = Teacher("anemail@gmail.com", "physics", 45)
teacher1.teacher_introduction()

person1 = Person("John", 15)
person1.myfunc()