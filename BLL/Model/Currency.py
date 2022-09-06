class Currency:
    __AUTO_ID: int = -1
    id: int
    name: str
    country: str

    def __init__(self, name: str, country: str):
        self.id = self.__AUTO_ID + 1
        self.name = name
        self.country = country

    def __repr__(self) -> str:
        return f"id: {self.id}, " \
               f"name: \"{self.name}\", " \
               f"country: \"{self.country}\""
