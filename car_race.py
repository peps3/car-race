from car import Car
import sys

cars=list()

with open(sys.argv[1]) as file:
    for line in file:
        line=line.strip()
        ls=line.split(",")
        car=Car(ls[0],ls[1],ls[2],0)
        for i in range(3,len(ls)):
            if int(ls[i]) > 0:
                car.accelerate(int(ls[i]))
            elif int(ls[i]) < 0:
                car.brake(abs(int(ls[i])))
            else:
                pass
        cars.append(car)
    winner=sorted(cars, key=lambda car: car.get_speed(),reverse=True)

    print("Winner: {}".format(winner[0]))
    print("Runner up: {}".format(winner[1]))
    print("3rd finisher: {}".format(winner[2]))
