class Bike:
    def __init__(self, brand, color, mileage, price):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.price = price

b1 = Bike("Royal Enfield", "Black", 35, 180000)
b2 = Bike("Pulsar", "Red", 45, 120000)

print(b1.brand, b1.color, b1.mileage, b1.price)
print(b2.brand, b2.color, b2.mileage, b2.price)