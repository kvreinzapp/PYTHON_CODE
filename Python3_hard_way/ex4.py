cars = 100
sapce_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_dirven = drivers
carpool_capacity = cars_dirven * sapce_in_a_car
everage_passengers_per_car = passengers / cars_dirven

print("There are cars", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "emtpy cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put out", everage_passengers_per_car, "in each car")
