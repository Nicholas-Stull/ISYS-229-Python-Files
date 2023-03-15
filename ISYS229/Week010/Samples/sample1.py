Sample-1 for Lesson 7.2

class Vehicle: #declaring the Vehicle class
    def __init__(self, year, color, make, model, trim): #listing the objects of the Vehicle class
        self.year = year
        self.color = color
        self.make = make
        self.model = model
        self.trim = trim
	    
car_1 = Vehicle(2022, "Grey", "Jeep", "Cherokee", "Trailhawk" ) #instntiating the object attributes of car_1
car_2 = Vehicle(2023, "White", "Subaru", "Crosstrek", "Limited") #instntiating the object attributes of car_2

#printing the various object attributes
print(f"The new {car_2.make} {car_2.model}, is a great vehicle. However, the {car_1.make} {car_1.model} {car_1.trim} is a better off-road vehicle.") 