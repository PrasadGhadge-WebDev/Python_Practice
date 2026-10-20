class Keyboard:
    def __init__(self, brand, color, type):
        self.brand = brand
        self.color = color
        self.type = type

k1 = Keyboard("Dell", "Black" ,"Wired")
k2 = Keyboard("Logitech", "White" ,"Wireless")

print(k1.brand, k1.color, k1.type)
print(k2.brand, k2.color, k2.type)