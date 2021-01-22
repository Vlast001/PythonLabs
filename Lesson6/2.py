"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной
в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    def __init__(self, length, width, weight, thickness):
        self._weight = weight
        self._thickness = thickness
        self._length = length
        self._width = width
        # print('Creat road_to_village object')

    def intake(self):
        intake = self._length * self._width * self._weight * self._thickness / 1000
        print(f'Need {intake} ton for the building')


road = Road(5000, 20, 25, 0.05)
road.intake()
