from apartment import Apartment
from dotenv import load_dotenv
import log_manage
import os
load_dotenv()


class ApartHerzelya(Apartment):

    def __init__(self):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: init parent, send to initialization func to init all parameters
                Return: Null"""
        try:
            self.l = log_manage.Log_manage()
            self.l.open_file()
            self.initialization()
        except Exception as e:
            print(e)

    def initialization(self):
        """Author: Maor Maharizi,
                        Created: 30.01.2023,
                        Detail: init the parameters and check that list room correct
                        Return: Null"""
        try:
            self.check_ls_rooms()
            self.check_price_meter_room_herzelya()
            self.check_divisions_meters()
            self.check_price_meter_apartment_herzelya()
            self.check_percents_for_division_meteres()
            self.check_discount_price_apartment_herzelya()
            self.check_discount_arnona_room4()
        except LookupError:
            self.l.write_to_log(os.getenv('HERZELYA'), os.getenv('LIST_MESSAGE'), list(map(int, os.getenv('LIST').split(','))))
        except DeprecationWarning:
            self.l.write_to_log(os.getenv('HERZELYA'), os.getenv('DEVISION_METERS_MESSAGE'), list(map(int, os.getenv('DIVISION_METERS').split(','))))
        except ProcessLookupError:
            self.l.write_to_log(os.getenv('HERZELYA'), os.getenv('PRICE_METER_ROOM_HERZELYA_MESSAGE'), float(os.getenv('PRICE_METER_ROOM_HERZELYA')))
        except PermissionError:
            self.l.write_to_log(os.getenv('HERZELYA'), os.getenv('PRICE_METER_APARTMENT_HERZELYA_MESSAGE'), float(os.getenv('PRICE_METER_APARTMENT_HERZELYA')))
        except PendingDeprecationWarning:
            self.l.write_to_log(os.getenv('HERZELYA'), os.getenv('PERCENTS_FOR_DIVISION_METERS_MESSAGE'), list(map(float, os.getenv('PERCENTS_FOR_DIVISION_METERS').split(','))))
        except IsADirectoryError:
            self.l.write_to_log(os.getenv('HERZELYA'), os.getenv('DISCOUNT_PRICE_APARTMENT_HERZELYA_MESSAGE'), float(os.getenv('DISCOUNT_PRICE_APARTMENT_HERZELYA')))
        except NotADirectoryError:
            self.l.write_to_log(os.getenv('HERZELYA'), os.getenv('DISCOUNT_ARNONA_ROOM4_MESSAGE'), float(os.getenv('DISCOUNT_ARNONA_ROOM4')))

    def check_ls_rooms(self):
        # check size rooms > 0 and size first room > 0
        ls = list(map(int, os.getenv('LIST').split(',')))
        if len(ls) > int(os.getenv('ZERO')) and ls[0] > int(os.getenv('ZERO')):
            Apartment.__init__(self, ls)
            self.ls = ls
        else:
            raise LookupError

    def check_price_meter_room_herzelya(self):
        price_meter_room_herzelya = float(os.getenv('PRICE_METER_ROOM_HERZELYA'))
        if isinstance(price_meter_room_herzelya, float):
            self.price_meter_room_herzelya = price_meter_room_herzelya
        else:
            raise ProcessLookupError

    def check_divisions_meters(self):
        # check length divisions_meters = 2 and from small to large
        divisions_meters = list(map(int, os.getenv('DIVISION_METERS').split(',')))
        if len(divisions_meters) == 2 and divisions_meters[0] < divisions_meters[1]:
            self.divisions_meters = divisions_meters
        else:
            raise DeprecationWarning

    def check_price_meter_apartment_herzelya(self):
        # check if price meter apartment herzelya is int
        price_meter_apartment_herzelya = float(os.getenv('PRICE_METER_APARTMENT_HERZELYA'))
        if isinstance(price_meter_apartment_herzelya, float):
            self.price_meter_apartment_herzelya = price_meter_apartment_herzelya
        else:
            raise PermissionError

    def check_percents_for_division_meteres(self):
        # check if percents for division meteres is list and length = 2
        percents_for_division_meteres = list(map(float, os.getenv('PERCENTS_FOR_DIVISION_METERS').split(',')))
        if isinstance(percents_for_division_meteres, list) and len(percents_for_division_meteres) == 2:
            self.percents_for_division_meteres = percents_for_division_meteres
        else:
            raise PendingDeprecationWarning

    def check_discount_price_apartment_herzelya(self):
        # check if discount price apartment herzelya is float
        discount_price_apartment_herzelya = float(os.getenv('DISCOUNT_PRICE_APARTMENT_HERZELYA'))
        if isinstance(discount_price_apartment_herzelya, float):
            self.discount_price_apartment_herzelya = discount_price_apartment_herzelya
        else:
            raise IsADirectoryError

    def check_discount_arnona_room4(self):
        # check if discount arnona room4 is float
        discount_arnona_room4 = float(os.getenv('DISCOUNT_ARNONA_ROOM4'))
        if isinstance(discount_arnona_room4, float):
            self.discount_arnona_room4 = discount_arnona_room4
        else:
            raise NotADirectoryError

    def calc_arnona(self):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: calc arnona to partment in herzelya
                Return: sum price"""
        # collection
        # size rooms * price arnona per meter, discount on room number 4
        sum_arnona = [j * self.price_meter_room_herzelya if (i != 3)
                      else j * self.price_meter_room_herzelya * (1 - self.discount_arnona_room4) for i, j in enumerate(self.ls)]
        self.l.write_to_log(os.getenv('HERZELYA'), os.getenv('CALC_ARNONA_MESSAGE'), sum(sum_arnona))
        return sum(sum_arnona)

    def calc_price_apartment(self):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: calc price apartment in herzelya => [-50=1000,50-100=10%,+100=12%]
                Return: price apartment"""
        sum_meter_apartment = sum(self.ls)
        sum_price = 0
        # calc the first level, then second level and finally the rest.
        # sum price => 2 options: sum meter apartment < level ? sum meter apartment : level
        sum_price += sum_meter_apartment * self.price_meter_apartment_herzelya if sum_meter_apartment <= self.divisions_meters[0] else self.divisions_meters[0] * self.price_meter_apartment_herzelya
        sum_meter_apartment -= sum_meter_apartment if sum_meter_apartment <= self.divisions_meters[0] else self.divisions_meters[0]
        sum_price += sum_meter_apartment * self.price_meter_apartment_herzelya * self.percents_for_division_meteres[0] if sum_meter_apartment <= self.divisions_meters[1]-self.divisions_meters[0] else self.divisions_meters[0] * self.price_meter_apartment_herzelya * self.percents_for_division_meteres[0]
        sum_meter_apartment -= sum_meter_apartment if sum_meter_apartment <= self.divisions_meters[1]-self.divisions_meters[0] else self.divisions_meters[0]
        sum_price += sum_meter_apartment * self.price_meter_apartment_herzelya * self.percents_for_division_meteres[1]
        sum_price = sum_price if self.discount_price_apartment_herzelya == 0 else sum_price * (1 - self.discount_price_apartment_herzelya)
        self.l.write_to_log(os.getenv('HERZELYA'), os.getenv('CALC_PRICE_APARTMENT_MESSAGE'), sum_price)
        return sum_price
