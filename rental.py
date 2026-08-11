from customer import Customer

class Rental:

    def __init__(self, customer: Customer, rental_period_type: str, duration: float):
        if rental_period_type.lower() not in ["hourly", "daily", "weekly"]:
            raise ValueError("Rental period type must be 'hourly', 'daily', or 'weekly'.")
            
        self._customer = customer
        self._rental_period_type = rental_period_type.lower()
        self._duration = duration
        self._items = []  

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def rental_period_type(self) -> str:
        return self._rental_period_type

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def items(self) -> list:
        return self._items

    def add_item(self, equipment_object):
        self._items.append(equipment_object)

    def calculate_best_item_price(self, item) -> float:
        rates = item.get_rates()
        
        if self._rental_period_type == "hourly":
            base_cost = rates["hourly"] * self._duration
            return min(base_cost, rates["daily"])
            
        elif self._rental_period_type == "daily":
            base_cost = rates["daily"] * self._duration
            return min(base_cost, rates["weekly"])
            
        elif self._rental_period_type == "weekly":
            return rates["weekly"] * self._duration
            
        return 0.0

    def calculate_total_bill(self, coupon_code: str = "") -> float:
        subtotal = sum(self.calculate_best_item_price(item) for item in self._items)
        current_total = subtotal

        if 3 <= len(self._items) <= 5:
            current_total *= 0.75

        if coupon_code.strip().upper().endswith("BBP"):
            current_total *= 0.90

        return round(current_total, 2)
