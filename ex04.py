#number of cars
cars = 100
#space in cars
space_in_a_car = 4
#number of drivers
drivers = 30
#number of passengers
passengers = 90
#car not used
cars_not_driven = cars - drivers
#number drivers needed
cars_driven = drivers
#capacity
carpool_capacity= cars_driven * space_in_a_car
#average passengers
average_passengers_per_car = passengers / cars_not_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
