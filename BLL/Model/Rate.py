from BLL.Model.Currency import Currency


class Rate:
    source: Currency
    target: Currency
    value: float

    def __init__(self, source: Currency, target: Currency, value: float):
        self.source = source
        self.target = target
        self.value = value

    def __repr__(self) -> str:
        return f"source: \"{self.source.name}\", " \
               f"target: \"{self.target.name}\", " \
               f"value: {self.value}"
