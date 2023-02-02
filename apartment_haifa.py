from apartment import Apartment
from dotenv import load_dotenv
import log_manage
import os
load_dotenv()


class ApartHaifa(Apartment):

    def __init__(self):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: init parent, send to initialization func to init all parameters
                Return: Null"""
        try:
            self.l = log_manage.Log_manage()
            self.l.open_file()
            self.initialization()
        except:
            print('init haifa')

    def initialization(self):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: init the parameters and check that room sizes correct
                Return: Null"""
        try:
            self.check_ls_rooms()
            self.check_price_meter_room_haifa()
            self.check_price_meter_apartment_haifa()
            self.check_discount_price_apartment_haifa()
            self.check_discount_arnona_room4()
        except LookupError:
                self.l.write_to_log(os.getenv('HAIFA'), os.getenv('LIST_MESSAGE'), list(map(int, os.getenv('LIST').split(','))))
        except ProcessLookupError:
            self.l.write_to_log(os.getenv('HAIFA'), os.getenv('PRICE_METER_ROOM_HAIFA_MESSAGE'), float(os.getenv('PRICE_METER_ROOM_HAIFA')))
        except PermissionError:
            self.l.write_to_log(os.getenv('HAIFA'), os.getenv('PRICE_METER_APARTMENT_HAIFA_MESSAGE'), float(os.getenv('PRICE_METER_APARTMENT_HAIFA')))
        except DeprecationWarning:
            self.l.write_to_log(os.getenv('HAIFA'), os.getenv('DISCOUNT_PRICE_APARTMENT_HAIFA_MESSAGE'), float(os.getenv('DISCOUNT_PRICE_APARTMENT_HAIFA')))
        except IsADirectoryError:
            self.l.write_to_log(os.getenv('HAIFA'), os.getenv('DISCOUNT_ARNONA_ROOM4_MESSAGE'), float(os.getenv('DISCOUNT_ARNONA_ROOM4')))
        except Exception as e:
            self.l.write_to_log(os.getenv('HAIFA'), os.getenv('ERROR_MESSAGE'), e)

    def check_ls_rooms(self):
        # check size rooms > 0 and size first room > 0
        ls = list(map(int, os.getenv('LIST').split(',')))
        if len(ls) > int(os.getenv('ZERO')) and ls[0] > int(os.getenv('ZERO')):
            Apartment.__init__(self, ls)
            self.ls = ls
        else:
            raise LookupError

    def check_price_meter_room_haifa(self):
        # check price meter room haifa is float
        price_meter_room_haifa = float(os.getenv('PRICE_METER_ROOM_HAIFA'))
        if isinstance(price_meter_room_haifa, float):
            self.price_meter_room_haifa = price_meter_room_haifa
        else:
            raise ProcessLookupError

    def check_price_meter_apartment_haifa(self):
        # check price meter apartment haifa is int
        price_meter_apartment_haifa = float(os.getenv('PRICE_METER_APARTMENT_HAIFA'))
        if isinstance(price_meter_apartment_haifa, float):
            self.price_meter_apartment_haifa = price_meter_apartment_haifa
        else:
            raise PermissionError

    def check_discount_price_apartment_haifa(self):
        # check if discount price apartment haifa is float
        discount_price_apartment_haifa = float(os.getenv('DISCOUNT_PRICE_APARTMENT_HAIFA'))
        if isinstance(discount_price_apartment_haifa, float):
            self.discount_price_apartment_haifa = discount_price_apartment_haifa
        else:
            raise DeprecationWarning

    def check_discount_arnona_room4(self):
        # check if discount arnona room4 is float
        discount_arnona_room4 = float(os.getenv('DISCOUNT_ARNONA_ROOM4'))
        if isinstance(discount_arnona_room4, float):
            self.discount_arnona_room4 = discount_arnona_room4
        else:
            raise IsADirectoryError


    def calc_arnona(self):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: calc arnona to partment in haifa
                Return: sum price"""
        # collection
        # size rooms * price arnona per meter, discount on room number 4
        four = float(os.getenv('DISCOUNT_PRICE_APARTMENT_HAIFA'))
        sum_arnona = [j * self.price_meter_room_haifa if (i != 3)
                      else j*self.price_meter_room_haifa*(1-self.discount_arnona_room4) for i,j in enumerate(self.ls)]
        self.l.write_to_log(os.getenv('HAIFA'), os.getenv('CALC_ARNONA_MESSAGE'), sum(sum_arnona))
        return (sum(sum_arnona) * (1 - self.discount_price_apartment_haifa))

    def calc_price_apartment(self):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: calc price apartment in haifa => [meter apartment * 1000 - 5%]
                Return: price apartment"""
        sum_meter_apartment = sum(self.ls)
        sum_price_apartment = sum_meter_apartment * self.price_meter_apartment_haifa  \
            if self.discount_price_apartment_haifa != 0 \
            else sum_meter_apartment * self.price_meter_apartment_haifa
        self.l.write_to_log(os.getenv('HAIFA'), os.getenv('CALC_PRICE_APARTMENT_MESSAGE'), sum_price_apartment)
        self.l.close_log_file()
        return sum_price_apartment
