
class Table:
    def __init__(self, material, color, height, price):
        self.material = material
        self.color = color
        self.height = height
        self.price = price

t1 = Table("Wood", "Brown", 3, 2500)
t2 = Table("Plastic", "White", 2, 1000)
t3 = Table("Glass", "Black", 4, 5000)
t4 = Table("Steel", "Silver", 3, 3500)
t5 = Table("Wood", "White", 5, 4500)
t6 = Table("Plastic", "Blue", 2, 1500)
t7 = Table("Wood", "Black", 4, 3000)

Mylist = [t1, t2, t3, t4, t5, t6, t7]

for i in Mylist:
    print("Material:", i.material)
    print("Color:", i.color)
    print("Height:", i.height)
    print("Price:", i.price)
    print("====================")
