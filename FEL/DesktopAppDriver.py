from py_linq.exceptions import NoElementsError
from BLL.Control.ExchangeService import ExchangeService
from DAL.MemoryDataStore import MemoryDataStore, InvalidCurrencyError
from DAL.MongoDAO import MongoDAO


class DesktopAppDriver:
    exchangeService: ExchangeService

    def main(self, dao):
        self.exchangeService = ExchangeService(dao=dao)
        source = input("Source Currency: ").upper()
        target = input("Target Currency: ").upper()

        try:
            rate = self.exchangeService.getRate(source, target)
            print(f"Current rate is: {str(rate['value'])}")
        except InvalidCurrencyError:
            print("Invalid currency")
        except IOError:
            print("Invalid input")
        except NoElementsError:
            print("No results were found matching those parameters.")
        finally:
            amount = float(input("Amount: "))
            result = self.exchangeService.convert(rate['value'], amount)
            print(f"{result} {target}")


DesktopAppDriver.main(DesktopAppDriver(), MongoDAO())
