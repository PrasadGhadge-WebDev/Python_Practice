class Table:
    def __init__(self, material, color, height, price):
        self.material = material
        self.color = color
        self.height = height
        self.price = price

t1 = Table("Wood", "Brown", 3, 2500)
t2 = Table("Plastic", "White", 2, 1000)

print(t1.material, t1.color, t1.height, t1.price)
print(t2.material, t2.color, t2.height, t2.price)