
#Note: Once you sort, the order cannot be reversed

#create cars list to support sort example
cars = ['bmw', 'audi', 'toyota', 'subaru'];
cars.sort();
print(cars);

#sort in reverse alphabetical order
cars.sort(reverse=True);
print(cars);

#Use the sorted() method to maintain the original order
cars = ['bmw', 'audi', 'toyota', 'subaru'];

print("Here is the original list");
print(cars);

print("\nHere is the sorted list");
print(sorted(cars));

print("\nHere is the original list again");
print(cars);

#using the reverse() method to reverse the original order of a list
cars = ['bmw', 'audi', 'toyota', 'subaru'];
print(cars);

cars.reverse();
print(cars);

#finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru'];
len(cars); #this is all that is needed on the command line
print(len(cars));

#access the last item in a list
cars = ['bmw', 'audi', 'toyota', 'subaru'];
print(cars[-1]);

########################################################################
#Starting here for Chapter 5

#Conditional IF statement
cars = ['audi', 'bmw', 'subaru', 'toyota'];
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title());

car = 'audi'
print(car=='bmw');

#Ignoring case when checking for equality
car = 'BMW'
print(car.lower()=='bmw');
#Note the value of the car value doesn't change bc we used  lower
print(car);