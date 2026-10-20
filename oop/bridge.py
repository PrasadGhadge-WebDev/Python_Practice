class Bridge:
    def __init__(self, name, location, length):
        self.name = name
        self.location = location
        self.length = length

b1 = Bridge("Karvengar Bridge", "Pune", 500)
b2 = Bridge("Warge Bridge", "Pune", 705)

print(b1.name, b1.location, b1.length)
print(b2.name, b2.location, b2.length)