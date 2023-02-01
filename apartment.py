from abc import abstractmethod


class Apartment(object):

    def __init__(self, ls):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: init the parameters,
                Return: Null"""
        self.list = ls
        self.__kitchentype = ""

    @property
    def kitchen(self):
        return self.__kitchentype

    @kitchen.setter
    def kitchen(self, k):
        self.__kitchentype = k

    @kitchen.deleter
    def kitchen(self):
        del self.__kitchentype

    # abstract method, calculate arnona, use in children
    @abstractmethod
    def calc_arnona(self):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: calc arnona to partment who inheritance me
                Return: sum price"""
        pass

    # abstract method, calculate price apartment, use in children
    @abstractmethod
    def calc_price_apartment(self):
        pass