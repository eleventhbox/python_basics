# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Direction:
    LEFT = 'left'
    RIGHT = 'right'


class Color:
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._is_moving = False

    def go(self):
        self._is_moving = True
        print("The car has started moving.")

    def stop(self):
        self._is_moving = False
        print("The car has stopped")

    def turn(self, direction):
        if self._is_moving:
            print(f"The car has turned to the {direction}.")
        else:
            print("The car is not moving.")

    def show_speed(self):
        if self._is_moving:
            print(f"The cars's speed is: {self.speed} km/hr.")
        else:
            print( "The car is not moving.")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        self.__speed_limit = 60

    def show_speed(self):
        super().show_speed()
        if  self._is_moving:
            if self.speed > self.__speed_limit:
                print(f" The car exceeded the speed limit of {self.__speed_limit} km/hr !")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        self.__speed_limit = 40

    def show_speed(self):
        super().show_speed()
        if self._is_moving:
            if self.speed > self.__speed_limit:
                print(f" The car exceeded the speed limit of {self.__speed_limit} km/hr !")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(speed=70, color=Color.GREEN, name='Ford')
work_car = WorkCar(speed=30, color=Color.YELLOW, name='GAZ')
sport_car = SportCar(speed=300, color=Color.RED, name='Ferrari')
police_car = PoliceCar(speed=190, color=Color.BLUE, name='Toyota')

print("Town car:")
town_car.show_speed()
town_car.go()
town_car.show_speed()
town_car.turn(Direction.LEFT)
town_car.stop()
print("====")
print("Sport car:")
sport_car.show_speed()
sport_car.go()
print(f"Sport car's color: {sport_car.color}")
print(f"Sport car's name: {sport_car.name}")
sport_car.show_speed()
print(f"Is this car police? {'Yes' if sport_car.is_police else 'No'}")
print("====")
print("Police car:")
police_car.go()
print(f"Police car's name: {police_car.name}")
print(f"Police car's color: {police_car.color}")
print(f"Is this car police? {'Yes' if police_car.is_police else 'No'}")
print("====")
print("Work car:")
work_car.go()
work_car.speed = 80
work_car.show_speed()
work_car.stop()
