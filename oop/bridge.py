class Bridge:
    def __init__(self, name, location, length):
        self.name = name
        self.location = location
        self.length = length

b1 = Bridge("Karve Nagar Bridge", "Pune", 500)
b2 = Bridge("Warje Bridge", "Pune", 705)
b3 = Bridge("Mhatre Bridge", "Pune", 600)
b4 = Bridge("Holkar Bridge", "Pune", 450)
b5 = Bridge("Sangam Bridge", "Pune", 800)
b6 = Bridge("Bund Garden Bridge", "Pune", 550)
b7 = Bridge("Bhide Bridge", "Pune", 400)

Mylist = [b1, b2, b3, b4, b5, b6, b7]

for i in Mylist:
    print("Bridge Name:", i.name)
    print("City:", i.location)
    print("Length:", i.length)
    print("========================")