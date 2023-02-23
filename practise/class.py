class House():
    def __init__(self, street, number):
        self.street = street
        self.number = number
    def build(self):
        print("Дом на улице" + self.street + " под номером" + self.number + "построен")

House1 = House("Московская", 20)
House2 = House("Московская", 21)
print(House2.street)

class ProspectHouse(House):
    def __init__(self, prospect,number):
        super().__init__(self, number)
        self.prospect = prospect

Prhouse = ProspectHouse("Ленина", 20)
print(Prhouse.prospect)