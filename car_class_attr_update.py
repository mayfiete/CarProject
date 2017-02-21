
class Car():
    """A simple attempt to represent a car. """

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model =  model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a neatly formatted descriptive name. """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    # add everything below to notes
    def update_odometer(self, mileage):
        """
        Set the odometer reading to a given value.
        Reject teh change if it attempts to roll the odometer back.
        """
        # self.odometer_reading = mileage

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer! ")

    def read_odometer(self):
        """Print a statement showing the car's mileage """
        print("This car has " + str(self.odometer_reading) + " miles on it. ")




my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(15)
my_new_car.read_odometer()