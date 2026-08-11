class Customer:
    def __init__(self, customer_id: int, name: str):
        self._customer_id = customer_id
        self._name = name

    @property
    def customer_id(self) -> int:
        return self._customer_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if value.strip() != "":
            self._name = value
