import os
import pytest as pytest
import log_manage
from apartment_haifa import ApartHaifa
from dotenv import load_dotenv
load_dotenv()

l = log_manage.Log_manage()
l.open_file()


@pytest.fixture
def apart():
    """Author: Maor Maharizi,
            Created: 30.01.2023,
            Detail: init apart class
            Return: Null"""
    return ApartHaifa()


def test_ls_rooms(apart):
    assert apart.ls == [48,49,53,20]


def test_price_meter_room_haifa(apart):
    assert apart.price_meter_room_haifa == 20


def test_price_meter_apartment_haifa(apart):
    assert apart.price_meter_apartment_haifa == 800


def test_discount_price_apartment_haifa(apart):
    assert apart.discount_price_apartment_haifa == 0.05


def test_discount_arnona_room4(apart):
    assert apart.discount_arnona_room4 == 0.1


@pytest.mark.test_calc_arnona
def test_calc_arnona(apart):
    """Author: Maor Maharizi,
            Created: 30.01.2023,
            Detail: test calc arnona
            Return: Null"""
    try:
        assert apart.calc_arnona() == 3040
        l.write_to_log(os.getenv('HAIFA'), os.getenv('CALC_ARNONA_MESSAGE'), os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('HAIFA'), os.getenv('CALC_ARNONA_MESSAGE'), str(e))


@pytest.mark.test_calc_price_apartment
def test_calc_price_apartment(apart):
    """Author: Maor Maharizi,
            Created: 30.01.2023,
            Detail: test calc price apartment
            Return: Null"""
    try:
        assert apart.calc_price_apartment() == 170000
        l.write_to_log(os.getenv('HAIFA'), os.getenv('CALC_PRICE_APARTMENT_MESSAGE'), os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('HAIFA'), os.getenv('CALC_PRICE_APARTMENT_MESSAGE'), str(e))
