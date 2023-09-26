class Mercedes():
    def __init__(self, power, speed, color, design):
        self.power = power
        self.speed = speed
        self.color = color
        self.design = design

    def car(self):
        print(f'{self.color} {self.design} улгусундогу унаанын кучу {self.power} ылдамдуулугу {self.speed}')


class BMW(Mercedes):
    def __init__(self, salon, color, complex):
        super().__init__(color)
        self.salon = salon
        self.complex = complex


a = Mercedes('5.5', '1450 km/h', 'Ak', 'S class')
print(a.power, a.speed, a.color, a.design)

b = BMW('busness class', 'millenium', 'black')
print(b.salon, b.complex, b.color)



class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age


per = Person('Nurik', 17)
print(per.name)
per.name = 'Ayaz'
print(per.name)




class MBank:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.__cash = 0
        self.__gold = False

    def __verification(self):
        self.__gold = True

    def get__cash(self):
        return f'Balance {self.__cash} som'

    def set__cash(self, x):
        self.__cash = self.__cash + x

    def info(self):
        return f'Name:{self.name}\nSurname:{self.surname}'

    def shopping(self, x):
        if self.__cash >= x:
            if x <= 100_000:
                self.__cash = self.__cash - x
                return 'Udacha'
            else:
                if self.__gold:
                    self.__cash = self.__cash - x
                    return f'баланс жетti'
                else:
                    return 'Ваш статус низок'
        else:
            return f"jetpey atat {self.get__cash()}"

    def get_gold(self):
        if self.__gold:
            return 'status GOLD'
        else:
            self.__verification()
            return 'USPESHNO'


online = MBank('Sanjar', 'Ayazov')
print(online.info())
print(online.get__cash())

online.set__cash(100000)
print(online.shopping(101000))
print(online.get__cash())

