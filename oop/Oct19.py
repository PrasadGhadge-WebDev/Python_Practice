class Student:

    def __init__(self, name, roll, city):
        self.Name = name
        self.Roll_no = roll
        self.City = city

obj1 = Student("Prasad", 101, "Pune")

print(obj1.Name)
print(obj1.Roll_no)
print(obj1.City)