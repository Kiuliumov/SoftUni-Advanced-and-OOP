from exam_practice.controller import Controller

def main():
    controller = Controller()
    print(controller.create_driver("Peter"))
    print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
    print(controller.add_car_to_driver("Peter", "SportsCar"))
    print(controller.create_car("SportsCar", "Porsche 911", 580))
    print(controller.add_car_to_driver("Peter", "SportsCar"))
    print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
    print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
    print(controller.create_driver("John"))
    print(controller.create_driver("Jack"))
    print(controller.create_driver("Kelly"))
    print(controller.add_car_to_driver("Kelly", "MuscleCar"))
    print(controller.add_car_to_driver("Jack", "MuscleCar"))
    print(controller.add_car_to_driver("Jack", "SportsCar"))
    print(controller.get_driver_by_name('Jack').car.model)
    print(controller.create_race("Christmas Top Racers"))
    print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
    print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
    print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
    print(controller.start_race("Christmas Top Racers"))
    [print(d.name, d.number_of_wins) for d in controller.drivers]

if __name__ == '__main__':
    main()