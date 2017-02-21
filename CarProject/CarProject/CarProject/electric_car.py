
from car_class_attr_update import Car
from battery import Battery

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles. """
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super(). __init__(make, model, year)
# note: the super() function tells Python to call the __init__() method
    # from the parent class, which gives an ElectricCar instance all of
    # the attributes of the parent class. Pull the superclasses' attributes

    # note that batter size is specific to electric cars
    # pull battery details from the Battery class
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
