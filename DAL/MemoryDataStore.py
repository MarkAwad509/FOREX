from BLL.Model.Currency import Currency
from BLL.Model.Rate import Rate
from DAL.ICurrencyDAO import ICurrencyDAO
from DAL.IRateDAO import IRateDAO
from py_linq import Enumerable


class MemoryDataStore(IRateDAO, ICurrencyDAO):
    currencies: list[Currency]
    rates: list[Rate]

    def __init__(self):
        self.currencies, self.rates = MemoryDataStore.populate()

    def fetchRate(self, source: str, target: str):
        ratesEnum = Enumerable(self.rates)
        return ratesEnum\
            .where(lambda r: r.source.name.lower().__eq__(source))\
            .where(lambda r: r.target.name.lower().__eq__(target))\
            .first()

    def fetchAllRates(self):
        return self.rates

    def fetchAllCurrencies(self):
        return self.currencies

    @staticmethod
    def populate():
        currencies = []
        rates = []

        currencies.append(Currency("CAD", "Canada"))
        currencies.append(Currency("USD", "United-States"))
        currencies.append(Currency("EUR", "Europe"))
        currencies.append(Currency("GBP", "England"))
        currencies.append(Currency("EGP", "Egypt"))

        rates.append(Rate(currencies[0], currencies[1], 0.76))
        rates.append(Rate(currencies[0], currencies[2], 0.76))
        rates.append(Rate(currencies[0], currencies[3], 0.66))
        rates.append(Rate(currencies[0], currencies[4], 14.64))
        rates.append(Rate(currencies[1], currencies[0], 1.31))
        rates.append(Rate(currencies[1], currencies[2], 1))
        rates.append(Rate(currencies[1], currencies[3], 0.87))
        rates.append(Rate(currencies[1], currencies[4], 19.23))
        rates.append(Rate(currencies[2], currencies[0], 1.31))
        rates.append(Rate(currencies[2], currencies[1], 1))
        rates.append(Rate(currencies[2], currencies[3], 0.86))
        rates.append(Rate(currencies[2], currencies[4], 19.14))
        rates.append(Rate(currencies[3], currencies[0], 1.51))
        rates.append(Rate(currencies[3], currencies[1], 1.15))
        rates.append(Rate(currencies[3], currencies[2], 1.16))
        rates.append(Rate(currencies[3], currencies[4], 22.15))
        rates.append(Rate(currencies[4], currencies[0], 0.068))
        rates.append(Rate(currencies[4], currencies[1], 0.052))
        rates.append(Rate(currencies[4], currencies[2], 0.052))
        rates.append(Rate(currencies[4], currencies[3], 0.045))

        return currencies, rates


class InvalidCurrencyError(Exception):
    def __init__(self, msg: str):
        print(msg)
