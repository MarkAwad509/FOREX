from DAL import mongoDbConfig


class NoSQLRepositoryDAO:
    host: str
    username: str
    password: str
    dbName: str

    def __init__(self):
        config = mongoDbConfig()
        self.host = config.get("host")
        self.username = config.get("username")
        self.password = config.get("password")
        self.dbName = config.get("dbName")

    def connect(self):
        pass
