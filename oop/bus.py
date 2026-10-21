
class Bus:
    def __init__(self, brand, color, number):
        self.brand = brand
        self.color = color
        self.number = number

b1 = Bus("Tata", "Red", "MH11")
b2 = Bus("Ashok Leyland", "Blue", "MH12")
b3 = Bus("Eicher", "White", "MH14")
b4 = Bus("Bharat Benz", "Yellow", "MH09")
b5 = Bus("Volvo", "Blue", "MH10")
b6 = Bus("Mahindra", "Green", "MH12")
b7 = Bus("Scania", "Red", "MH11")

Mylist = [b1, b2, b3, b4, b5, b6, b7]

for i in Mylist:
    if i.number == "MH11":
        print("Brand:", i.brand)
        print("Number:", i.number)
        print("Color:", i.color)
        print("====================")
