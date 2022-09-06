from py_linq.exceptions import NoElementsError

from BLL.Control.ExchangeService import ExchangeService
from BLL.Model.Currency import Currency
from BLL.Model.Rate import Rate
from DAL.MemoryDataStore import MemoryDataStore
from DAL.MongoDAO import MongoDAO


class DesktopAppDriver:
    exchangeService: ExchangeService

    def main(self):
        dao = MongoDAO()
        c = dao.fetchRate("CAD", "USD")
        print(c)
        # self.exchangeService = ExchangeService(dao=dao)
        # source = input("Source Currency: ").lower()
        # target = input("Target Currency: ").lower()
        #
        # try:
        #     rate = self.exchangeService.dao.fetchRate(source, target)
        #     print(f"Current market rate is: {rate.value}")
        #     amount = float(input("Amount: "))
        #     print(f"{rate.value * amount} {target.upper()}")
        # except IndexError:
        #     print("Input Error")
        # except NoElementsError:
        #     print("No results were found matching those parameters.")


DesktopAppDriver.main(DesktopAppDriver())
