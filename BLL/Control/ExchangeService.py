from DAL.IRateDAO import IRateDAO


class ExchangeService:
    dao: IRateDAO

    def __init__(self, dao):
        self.dao = dao
