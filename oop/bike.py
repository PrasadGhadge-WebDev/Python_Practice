
class Bike:
    def __init__(self, brand, color, mileage, price):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.price = price

b1 = Bike("Royal Enfield", "Black", 35, 180000)
b2 = Bike("Pulsar", "Red", 45, 120000)
b3 = Bike("KTM", "Orange", 30, 220000)
b4 = Bike("Honda", "Blue", 50, 95000)
b5 = Bike("Yamaha", "Black", 40, 150000)
b6 = Bike("TVS Apache", "White", 45, 140000)
b7 = Bike("Suzuki", "Grey", 55, 110000)

Mylist = [b1, b2, b3, b4, b5, b6, b7]

Mileage = []

for i in Mylist:
    if i.mileage <= 45:
        Mileage.append(i)

print("Bikes with Mileage <= 45")
print("************************")

for i in Mileage:
    print("Brand:", i.brand)
    print("Color:", i.color)
    print("Mileage:", i.mileage)
    print("Price:", i.price)
    print("========================")
