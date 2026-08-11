from equipment import Ski, Snowboard

class RentalShop:

    def __init__(self, starting_skis: int, starting_snowboards: int):
        self._available_skis = starting_skis
        self._available_snowboards = starting_snowboards
        
        self._total_skis_rented_today = 0
        self._total_snowboards_rented_today = 0
        self._total_revenue_collected_today = 0.0

    @property
    def available_skis(self) -> int:
        return self._available_skis

    @property
    def available_snowboards(self) -> int:
        return self._available_snowboards

    @property
    def total_skis_rented_today(self) -> int:
        return self._total_skis_rented_today

    @property
    def total_snowboards_rented_today(self) -> int:
        return self._total_snowboards_rented_today

    @property
    def total_revenue_collected_today(self) -> float:
        return self._total_revenue_collected_today

    def check_and_rent_inventory(self, rental_manifest) -> bool:
        ski_count = sum(1 for item in rental_manifest.items if isinstance(item, Ski))
        board_count = sum(1 for item in rental_manifest.items if isinstance(item, Snowboard))

        if ski_count > self._available_skis or board_count > self._available_snowboards:
            return False

        self._available_skis -= ski_count
        self._available_snowboards -= board_count

        self._total_skis_rented_today += ski_count
        self._total_snowboards_rented_today += board_count
        
        for item in rental_manifest.items:
            item.is_rented = True
            
        return True

    def process_return_to_inventory(self, rental_manifest, coupon_used: str = ""):
        ski_count = sum(1 for item in rental_manifest.items if isinstance(item, Ski))
        board_count = sum(1 for item in rental_manifest.items if isinstance(item, Snowboard))

        self._available_skis += ski_count
        self._available_snowboards += board_count

        for item in rental_manifest.items:
            item.is_rented = False

        final_bill = rental_manifest.calculate_total_bill(coupon_used)
        self._total_revenue_collected_today += final_bill
