

# 1. Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance. 
# Add a class initializer that sets the first two of the properties based on parameter values. 
# The current speed and travelled distance of a new car must be automatically set to zero. 
# Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h). 
# Finally, print out all the properties of the new car.
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142)
print(f"Registration Number: {car.registration_number}")
print(f"Maximum Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Travelled Distance: {car.travelled_distance} km")

# 2. Extend the program by adding an accelerate method into the new class. 
# The method should receive the change of speed (km/h) as a parameter. 
# If the change is negative, the car reduces speed. 
# The method must change the value of the speed property of the object. 
# The speed of the car must stay below the set maximum and cannot be less than zero. 
# Extend the main program so that the speed of the car is first increased by +30 km/h, 
# then +70 km/h and finally +50 km/h. Then print out the current speed of the car. 
# Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed. 
# The travelled distance does not have to be updated yet.
def accelerate(self, change):
    new_speed = self.current_speed + change
    if new_speed > self.max_speed:
        self.current_speed = self.max_speed
    elif new_speed < 0:
        self.current_speed = 0
    else:
        self.current_speed = new_speed

Car.accelerate = accelerate

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current Speed after acceleration: {car.current_speed} km/h")

car.accelerate(-200)
print(f"Final Speed after emergency brake: {car.current_speed} km/h")

# 3. Again, extend the program by adding a new drive method that receives the number of hours as a parameter. 
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time. 
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. 
# Method call car.drive(1.5) increases the travelled distance to 2090 km.
def drive(self, hours):
    self.travelled_distance += self.current_speed * hours

Car.drive = drive

car.drive(1.5)
print(f"Travelled Distance after driving: {car.travelled_distance} km")

# 4. Now we will program a car race. 
# The travelled distance of a new car is initialized as zero. 
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop. 
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h. 
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. 
# Now the race begins. One per every hour of the race, the following operations are performed:
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. 
# This is done using the accelerate method. Each car is made to drive for one hour. 
# This is done with the drive method. 
# The race continues until one of the cars has advanced at least 10,000 kilometers. 
# Finally, the properties of each car are printed out formatted into a clear table.
import random
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Registration':<15}{'Speed (km/h)':<15}{'Distance (km)':<15}")
        for car in self.cars:
            print(f"{car.registration_number:<15}{car.current_speed:<15}{car.travelled_distance:<15}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

def main():
    cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
    race = Race("Grand Demolition Derby", 10000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()

    race.print_status()

if __name__ == "__main__":
    main()