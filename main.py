class Human:
    def __init__(self,name,age,iin):
        self.name = name
        self.age = age
        self.iin = iin 

    def introduce(self):
        print(f"ПРИВЕТ! Меня зовут {self.name},мне{self.age}Лет")

class Student(Human):
    def __init__(self,name,age,iin,group,gpa):
        super().__init__(name,age,iin)
        self.group = group
        self.gpa = gpa

    def introduce(self):
        super().introduce()
        print(f"Я учусь в группе {self.group}и мой gpa- {self.gpa}")

class Teach(Human):
    def __init__(self, name, age, iin,subject):
        super().__init__(name, age, iin)
        self.subject= subject
        self.grouplist= []

    def addgroup(self,group):
        grouplist.append(group)
        print(f"Группа добавлена в список")
        
    def introduce(self):
         super().introduce()
         print(f"Я веду предмет {self.subject},я веду группы:")
         for items in grouplist:
             print(items)

Bob = Student("Bob",21,123456789,"1241",4.0)
Bob.introduce()

Kate=Teach("Kate",40,432141414,"Math")
Kate.addgroup("4321")
Kate.addgroup("4121")
Kate.addgroup("4421")
Kate.addgroup("4621")
Kate.introduce()