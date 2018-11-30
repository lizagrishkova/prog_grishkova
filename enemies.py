# coding: utf-8
# license: GPLv3
from gameunit import *
from random import *


class Enemy(Attacker):
    pass


def generate_random_enemy():
    random_enemy_type = choice(enemy_types)
    enemy = random_enemy_type()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


def generate_random_troll():
    random_troll_type = choice(troll_types)
    troll = random_troll_type()
    return troll


def generate_troll_list(troll_number):
    troll_list = [generate_random_troll() for i in range(troll_number)]
    return troll_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 20
        self._color = 'зелёный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 20
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 20
        self._color = 'черный'

    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GuessTroll(Troll):
    def __init__(self):
        self._attack = 5
        self._health = 50
        self._color = 'GuessTroll'

    def question(self):
        x = randint(1, 5)
        self.__quest = 'Угадай число'
        self.set_answer(x)
        return self.__quest


def prime_check(x):
    cnt = 0
    for i in range(1, x):
        if not x % i:
            cnt += 1
    if cnt == 1:
        return 'да'
    else:
        return 'нет'


class PrimeTroll(Troll):
    def __init__(self):
        self._attack = 10
        self._health = 50
        self._color = 'PrimeTroll'

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Является ли число ' + str(x) + ' простым?'
        self.set_answer(prime_check(x))
        return self.__quest


enemy_types = [GreenDragon, RedDragon, BlackDragon]
troll_types = [GuessTroll, PrimeTroll]