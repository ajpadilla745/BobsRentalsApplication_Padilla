class RentalEquipment:

    def __init__(self, equipment_id: str, brand: str):
        self._equipment_id = equipment_id
        self._brand = brand
        self._is_rented = False

    @property
    def equipment_id(self) -> str:
        return self._equipment_id

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def is_rented(self) -> bool:
        return self._is_rented

    @is_rented.setter
    def is_rented(self, status: bool):
        if isinstance(status, bool):
            self._is_rented = status

    def get_rates(self) -> dict:
        return {"hourly": 0.0, "daily": 0.0, "weekly": 0.0}


class Ski(RentalEquipment):
    def get_rates(self) -> dict:
        return {"hourly": 15.0, "daily": 50.0, "weekly": 200.0}


class Snowboard(RentalEquipment):
    def get_rates(self) -> dict:
        return {"hourly": 10.0, "daily": 40.0, "weekly": 160.0}
