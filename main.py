#Класна робота
#1
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + ' кушає')

class Dog(Animal):
    def __init__(self, name, age, breed ):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(self.name,"гавкає")
hotdog = Dog("Bobik", 3,'Labrador')
print(hotdog.name)
print(hotdog.age,"роки")
print(hotdog.breed)
hotdog.eat()

#2

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name {self.name}, age {self.age}"
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
    def __str__(self):
        return super().__str__() + f"student_id {self.student_id}"

student1 = Student("Zahar", 45,"76345634535")

with open("info_student.txt",'w') as file:
    file.write(str(student1))