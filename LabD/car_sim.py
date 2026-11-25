from car import Car

vehicle = Car(100, 30)
x = ""
while x != "exit":
    x = input("Drive, refuel, or type 'Exit'").lower()
    if x == "drive":
        vehicle.drive()
    elif x == "refuel":
        vehicle.refuel()
    elif x == "exit":
        break
    else:
        continue