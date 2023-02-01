from os.path import split

from apartment_herzelya import ApartHerzelya
from apartment_haifa import ApartHaifa
from dotenv import load_dotenv
import os

load_dotenv()


if __name__ == '__main__':
        a = ApartHerzelya()
        a.calc_arnona()
        a.calc_price_apartment()
        a = ApartHaifa()
        a.calc_arnona()
        a.calc_price_apartment()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/