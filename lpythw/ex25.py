def run():
    print("VROOM")


def stop():
    print("STOP")


def create_car(color, speed):
    corvette = {"color": color, "speed": speed, "run": run, "stop": stop}
    return corvette


car1 = create_car("RED", 50)
car2 = create_car("YELLOW", 20)
print(car1)
print(car2)
