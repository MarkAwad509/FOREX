from pymongo.database import Database
from BLL.Model.Currency import Currency
from BLL.Model.Rate import Rate
from DAL.NoSQLRepositoryDAO import NoSQLRepositoryDAO
from DAL.IRateDAO import IRateDAO
from DAL.ICurrencyDAO import ICurrencyDAO
from pymongo import MongoClient
import pymongo


class MongoDAO(NoSQLRepositoryDAO, IRateDAO, ICurrencyDAO):
    dao: NoSQLRepositoryDAO = NoSQLRepositoryDAO()
    client: MongoClient
    db: Database

    def __init__(self):
        self.client = self.connect()
        self.db = self.client[self.dao.dbName]

    def connect(self) -> MongoClient | str:
        """
        connects to MongoDB by instantiating a MongoClient object
        :returns: MongoClient instance, if the connection is successful, failure message otherwise
        """
        conn_str = f"mongodb+srv://{self.dao.username}:{self.dao.password}@cluster0.tpvwp.mongodb.net/"\
                   f"{self.dao.dbName}?authSource=admin&retryWrites=true&w=majority"
        try:
            return pymongo.MongoClient(conn_str)
        except pymongo.errors.ConnectionFailure:
            return "Connection failed, check connection parameters"

    def fetchRate(self, source: str, target: str):
        return self.db.rate.find_one({"source.name": source, "target.name": target})

    def fetchAllRates(self):
        rates = list[Rate]
        for r in self.db.rate.find():
            rates.append(Rate(
                r.get("source"),
                r.get("target"),
                r.get("value")
            ))
        return rates

    def fetchAllCurrencies(self):
        currencies = list[Currency]
        for c in self.db.get_collection("currency").find():
            currencies.append(Currency(
                c.get("name"),
                c.get("country")
            ))
        return currencies
