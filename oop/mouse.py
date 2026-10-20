class Mouse:
    def __init__(self, brand, color, type):
        self.brand = brand
        self.color = color
        self.type = type

m1 = Mouse("Dell", "Black", "Wired")
m2 = Mouse("HP", "White", "Wireless")

print(m1.brand, m1.color, m1.type)
print(m2.brand, m2.color,  m2.type)