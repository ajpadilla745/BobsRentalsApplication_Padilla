from customer import Customer
from equipment import Ski, Snowboard
from rental import Rental
from rental_shop import RentalShop

def main():
    print("=" * 65)
    print("      BOB'S RENTAL SHOP CLASS LIBRARY VERIFICATION RUN      ")
    print("=" * 65)

    print("\n[Test 1] Instantiating Core RentalShop (10 Skis, 5 Snowboards)...")
    shop = RentalShop(starting_skis=10, starting_snowboards=5)
    print(f"-> Store Active Stock: {shop.available_skis} Skis, {shop.available_snowboards} Snowboards.")

    print("\n[Test 2] Setting up Customer Profile and 4-Hour Rental Order...")
    customer_object = Customer(customer_id=1402, name="John Doe")
    hourly_rental = Rental(customer=customer_object, rental_period_type="hourly", duration=4.0)
    
    ski_1 = Ski(equipment_id="SKI-101", brand="Rossignol")
    board_1 = Snowboard(equipment_id="SBD-202", brand="Burton")
    
    hourly_rental.add_item(ski_1)
    hourly_rental.add_item(board_1)
    print("-> Connected equipment instances to Alice's active manifest array.")

    print("\n[Test 3] Processing Check and Rent Inventory Verification...")
    if shop.check_and_rent_inventory(hourly_rental):
        print("-> Success: Allocation parameters approved.")
        print(f"-> Remaining Stock: {shop.available_skis} Skis, {shop.available_snowboards} Boards available.")
    else:
        print("-> Error: Request exceeded current stock parameters.")

    print("\n[Test 4] Verifying Best Price Optimization Formula Triggers...")
    ski_optimized_cost = hourly_rental.calculate_best_item_price(ski_1)
    print(f"-> Ski 4-Hour Price Calculation: ${ski_optimized_cost:.2f} (Expected: $50.00)")

    print("\n[Test 5] Evaluating Compound Sequential Discount Compounding...")
    family_customer = Customer(customer_id=1505, name="The Robinson Group")
    family_rental = Rental(customer=family_customer, rental_period_type="daily", duration=1.0)
    
    family_rental.add_item(Ski("SKI-02", "Salomon"))
    family_rental.add_item(Ski("SKI-03", "Salomon"))
    family_rental.add_item(Ski("SKI-04", "Nordica"))
    
    final_invoice = family_rental.calculate_total_bill("WINTERBBP")
    print(f"-> Family Daily Invoice (3 Items + 'WINTERBBP' Coupon): ${final_invoice:.2f} (Expected: $101.25)")

    print("\n[Test 6] Running Return Processing Actions and Logging Revenue...")
    shop.process_return_to_inventory(family_rental, "WINTERBBP")
    print(f"-> Returned items. Active Shop Stock: {shop.available_skis} Skis.")
    print(f"-> Daily Historic Revenue Collected: ${shop.total_revenue_collected_today:.2f} (Expected: $101.25)")
    print(f"-> Total Daily Skis Rented Aggregator Counter: {shop.total_skis_rented_today}")

    print("\n" + "=" * 65)
    print("              CLASS LIBRARY DIAGNOSTIC RUN SUCCESS              ")
    print("=" * 65)

if __name__ == "__main__":
    main()
