
class Keyboard:
    def __init__(self, brand, color, type):
        self.brand = brand
        self.color = color
        self.type = type

k1 = Keyboard("Dell", "Black", "Wired")
k2 = Keyboard("Logitech", "White", "Wireless")
k3 = Keyboard("HP", "Grey", "Wired")
k4 = Keyboard("Corsair", "Black", "Wireless")
k5 = Keyboard("Redragon", "Red", "Wired")
k6 = Keyboard("Lenovo", "Black", "Wireless")
k7 = Keyboard("Asus", "White", "Wired")

Mylist = [k1, k2, k3, k4, k5, k6, k7]

for i in Mylist:
    if i.type == "Wired":
        print("Brand:", i.brand)
        print("Color:", i.color)
        print("Type:", i.type)
        print("====================")    
