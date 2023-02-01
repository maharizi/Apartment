import os
import pytest as pytest
from dotenv import load_dotenv
from apartment_herzelya import ApartHerzelya
load_dotenv()


@pytest.fixture
def apart():
    """Author: Maor Maharizi,
            Created: 30.01.2023,
            Detail: init apart class
            Return: Null"""
    return ApartHerzelya()


def test_ls_rooms(apart):
    assert apart.ls == [48,49,53,20]


def test_price_meter_room_herzelya(apart):
    assert apart.price_meter_room_herzelya == 30


def test_divisions_meters(apart):
    assert apart.divisions_meters == [50,100]


def test_price_meter_apartment_herzelya(apart):
    assert apart.price_meter_apartment_herzelya == 1000


def test_percents_for_division_meteres(apart):
    assert apart.percents_for_division_meteres == [1.10,1.12]


def test_discount_price_apartment_herzelya(apart):
    assert apart.discount_price_apartment_herzelya == 0


def test_discount_arnona_room4(apart):
    assert apart.discount_arnona_room4 == 0.1


def test_calc_arnona(apart):
    """Author: Maor Maharizi,
            Created: 30.01.2023,
            Detail: test calc arnona
            Return: Null"""
    assert apart.calc_arnona() == 5040


def test_calc_price_apartment(apart):
    """Author: Maor Maharizi,
            Created: 30.01.2023,
            Detail: test calc price apartment
            Return: Null"""
    assert apart.calc_price_apartment() == 183400