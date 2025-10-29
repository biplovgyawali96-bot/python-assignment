# 1. Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down.
# A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5),
# the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
# The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
class Elevator:
    def __init__(self, bottomFloor, topFloor):
        self.currentFloor = bottomFloor
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor

    def goToFloor(self, floor):
        while self.currentFloor < floor:
            self.floorUp()
        while self.currentFloor > floor:
            self.floorDown()

    def floorUp(self):
        if self.currentFloor < self.topFloor:
            self.currentFloor += 1
            print(f"Elevator is now at floor {self.currentFloor}")

    def floorDown(self):
        if self.currentFloor > self.bottomFloor:
            self.currentFloor -= 1
            print(f"Elevator is now at floor {self.currentFloor}")

elevator = Elevator(0, 10)
elevator.goToFloor(5)
elevator.goToFloor(0)

# 2. Extend the previous program by creating a Building class.
# The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
# When a building is created, the building creates the required number of elevators.
# The list of elevators is stored as a property of the building.
# Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
class Building:
    def __init__(self, bottomFloor, topFloor, numElevators):
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor
        self.elevators = [Elevator(bottomFloor, topFloor) for _ in range(numElevators)]

    def runElevator(self, elevatorNumber, destinationFloor):
        if 0 <= elevatorNumber < len(self.elevators):
            self.elevators[elevatorNumber].goToFloor(destinationFloor)

building = Building(0, 10, 3)
building.runElevator(0, 7)
building.runElevator(1, 3)

# 3. Extend the program again by adding a method fire_alarm that does not receive any parameters
# and moves all elevators to the bottom floor.
def fireAlarm(self):
    for elevator in self.elevators:
        elevator.goToFloor(self.bottomFloor)

Building.fireAlarm = fireAlarm
building.fireAlarm()

# 4. This exercise continues the previous car race exercise from the last exercise set.
# Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race.
# The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class.
class Car:
    def __init__(self, registrationNumber, maxSpeed):
        self.registrationNumber = registrationNumber
        self.maxSpeed = maxSpeed
        self.currentSpeed = 0
        self.travelledDistance = 0

    def accelerate(self, change):
        newSpeed = self.currentSpeed + change
        if newSpeed > self.maxSpeed:
            self.currentSpeed = self.maxSpeed
        elif newSpeed < 0:
            self.currentSpeed = 0
        else:
            self.currentSpeed = newSpeed

    def drive(self, hours):
        self.travelledDistance += self.currentSpeed * hours

import random

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hourPasses(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def printStatus(self):
        print(f"\nRace: {self.name}")
        print(f"{'Registration':<15}{'Speed (km/h)':<15}{'Distance (km)':<15}")
        for car in self.cars:
            print(f"{car.registrationNumber:<15}{car.currentSpeed:<15}{car.travelledDistance:<15}")

    def raceFinished(self):
        return any(car.travelledDistance >= self.distance for car in self.cars)

def main():
    cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.raceFinished():
        race.hourPasses()
        hours += 1
        if hours % 10 == 0:
            race.printStatus()

    race.printStatus()

if __name__ == "__main__":
    main()