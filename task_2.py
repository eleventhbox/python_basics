# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self, asphalt_weight_per_sq_m, asphalt_thickness):
        print( self._length * self._width * asphalt_weight_per_sq_m * asphalt_thickness


road = Road(20, 5000)
wt = road.calc_weight(25, 5)
print(f'Asphalt weight, t: {int(wt/1000)}')
