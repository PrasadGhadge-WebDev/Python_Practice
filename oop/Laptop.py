class Laptop:
    def __init__(self, brand, color, ram, storage, price):
        self.brand = brand
        self.color = color
        self.ram = ram
        self.storage = storage
        self.price = price

l1 = Laptop("Dell", "Black", "8GB", "512GB SSD", 45000)
l2 = Laptop("HP", "Silver", "16GB", "1TB SSD", 60000)
l3 = Laptop("Lenovo", "Grey", "8GB", "256GB SSD", 38000)
l4 = Laptop("Asus", "Black", "16GB", "512GB SSD", 55000)
l5 = Laptop("Acer", "Silver", "8GB", "1TB SSD", 42000)
l6 = Laptop("Apple", "Space Grey", "16GB", "512GB SSD", 120000)
l7 = Laptop("Dell", "White", "32GB", "1TB SSD", 85000)

Mylist = [l1, l2, l3, l4, l5, l6, l7]

print("\nAbove 50k Laptop List")
print("**********************************")

above_50k = []

for i in Mylist:
    if i.price > 50000:
        above_50k.append(i)

for n in above_50k:
    print("Brand Name:", n.brand)
    print("Brand Color:", n.color)
    print("Brand Ram:", n.ram)
    print("Brand Storage:", n.storage)
    print("Brand Price:", n.price)
    print("==============================\n")
