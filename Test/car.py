class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description_name(self):
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        print('Пробег ' + str(self.odometer_reading) + ' км')

    def update_odometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('Не трожь!')
    
    def increment_odometer(self, km):
        self.odometer_reading += km

class Battery():
     
    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        print(self.battery)

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def description_name(self):
        desc = str(self.year) + ' ' + self.model
        return desc.title()

car = ElectricCar('make', 'model', 2020)
car.battery.description_battery()