class Bus:
    def __init__(self, brand, color, number):
        self.brand = brand
        self.color = color
        self.number = number

b1 = Bus("Tata", "Red", "MH11")
b2 = Bus("Ashok Leyland", "Blue", "MH12")

print(b1.brand, b1.color, b1.number)
print(b2.brand, b2.color, b2.number)