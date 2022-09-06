from BLL.Model.Rate import Rate
from DAL import NoSQLRepositoryDAO
from DAL.NoSQLRepositoryDAO import NoSQLRepositoryDAO
from DAL.MemoryDataStore import MemoryDataStore


class ExchangeService:
    """
    `Description`: Control class that fetches the rate from the data source, and does the conversion.
    """
    dao: NoSQLRepositoryDAO | MemoryDataStore

    def __init__(self, dao: NoSQLRepositoryDAO | MemoryDataStore):
        """
        :param dao: data access object, reads from data source.
        """
        self.dao = dao

    def getRate(self, source: str, target: str) -> Rate:
        """
        returns Rate object corresponding to search params

        :param source: three letter tag of source currency, ex: CAD
        :param target: three letter tag of target currency
        :return: rate object
        """
        return self.dao.fetchRate(source, target)

    def convert(self, rate: float, amount: float) -> float:
        """
        converts the amount to the foreign currency

        :param rate: rate value
        :param amount: money to be converted
        :return: multiplication of both params
        """
        return amount * rate
