from BLL.Model.Currency import Currency


class IRateDAO:
    def __init__(self):
        pass

    def fetchRate(self, source: str, target: str):
        pass

    def fetchAllRates(self):
        pass
