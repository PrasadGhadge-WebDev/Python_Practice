class Laptop:
    def __init__(self, brand, color, ram, storage):
        self.brand = brand
        self.color = color
        self.ram = ram
        self.storage = storage

l1 = Laptop("Dell", "Black", "8GB", "512GB SSD")
l2 = Laptop("HP", "Silver", "16GB", "1TB SSD")

print(l1.brand, l1.color, l1.ram, l1.storage)
print(l2.brand, l2.color, l2.ram, l2.storage)