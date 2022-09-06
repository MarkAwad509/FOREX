class Currency:
    name: str
    country: str

    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    def __repr__(self) -> str:
        return f"name: \"{self.name}\", " \
               f"country: \"{self.country}\""
