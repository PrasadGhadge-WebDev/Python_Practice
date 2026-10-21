
class Mouse:
    def __init__(self, brand, color, type):
        self.brand = brand
        self.color = color
        self.type = type

m1 = Mouse("Dell", "Black", "Wired")
m2 = Mouse("HP", "White", "Wireless")
m3 = Mouse("Logitech", "Grey", "Wireless")
m4 = Mouse("Lenovo", "Black", "Wired")
m5 = Mouse("Asus", "White", "Wireless")
m6 = Mouse("Zebronics", "Red", "Wired")
m7 = Mouse("Razer", "Green", "Wireless")

Mylist = [m1, m2, m3, m4, m5, m6, m7]

for i in Mylist:
    print("Brand:", i.brand)
    print("Color:", i.color)
    print("Type:", i.type)
    print("====================")
