class Car:
    def __init__(self, make, production_year):
        self.make = make
        self.production_year = production_year


car1 = Car("Syrenka", 1970)
car2 = Car("Wołga", 1976)

print(car1.make + " " + str(car1.production_year))
print(car2.make + " " + str(car2.production_year))

# Syrenka 1970
# Wołga 1976

car1 = car2

print(car1.make + " " + str(car1.production_year))
print(car2.make + " " + str(car2.production_year))

# Syrenka 1970
# Wołga 1976
# Wołga 1976
# Wołga 1976
