#=======================================================
# Name: Antonio Padilla
# Course: Object-Oriented Programming
# Assignment: Final Project PT.2
#=======================================================
from customer import Customer
from rental import Rental
from rental_shop import RentalShop
from equipment import Ski, Snowboard



def ValidateIntegerInput (integer_input):
    try:
        integer_input = int(integer_input)
        if integer_input > 0:
            global flag_string
            flag_string = True
        else:
            integer_input = 0
            print("Must be positive")
    except ValueError:
        integer_input = 0
        print("Must be numeric")
    return integer_input

def customer_rental():
        try:

            print("Enter the customer's name")
            customer_input = input("-> ")
            if customer_input != "":
                print("Enter customer ID")
            id_input = int(input("->"))
            id_input = ValidateIntegerInput(id_input)
            if id_input != "":
                customer_object = Customer(customer_id = id_input, name = customer_input)
            print("Select a rental period")
            print("1.hourly")
            print("2.daily")
            print("3.weekly")
            rental_input = input("-> ")
            if rental_input == "hourly":
                print("How many hours?")
                duration_input = int(input("-> "))
                duration_input = ValidateIntegerInput(duration_input)
            if duration_input > 0 and duration_input < 24:
                hourly_rental = Rental(customer = customer_object, rental_period_type = rental_input, duration = duration_input)
                if rental_input == "daily":
                    daily_rental = Rental(Customer, rental_period_type = rental_input, duration = 1)
                    if rental_input == "weekly":
                        weekly_rental = Rental(Customer, rental_period_type = rental_input, duration = 1)
            else:
                raise Exception("invalid input")
            while True:
                print("Skis or Snowboards? ")
                equipment_input = input("-> ")
                if equipment_input == "Skis": 
                    print("Select Ski brand")
                    print("1. Salomon")
                    print("2. Burton")
                    print("3. Rossignol")
                    equipment_input = input("-> ")
                    if equipment_input == "Salomon":
                        ski_item = Ski(equipment_id= "SKI-201", brand = "Salomon")
                    elif equipment_input == "Burton":
                        ski_item = Ski(equipment_id= "SKI-202", brand = "Burton")
                    elif equipment_input == "Rossignol":
                        ski_item = Ski(equipment_id= "SKI-203", brand = "Rossignol")
                    if rental_input == "hourly":
                        hourly_rental.add_item(ski_item) 
                        rent_shop.check_and_rent_inventory(hourly_rental)
                    elif rental_input == "daily":
                        daily_rental.add_item(ski_item) 
                        rent_shop.check_and_rent_inventory(daily_rental)
                    elif rental_input == "weekly":
                        weekly_rental.additem(ski_item)
                        rent_shop.check_and_rent_inventory(weekly_rental)

                if equipment_input == "Snowboards":
                    print("Select Snowboard brand")
                    print("1. Salomon")
                    print("2. Burton")
                    print("3. Rossignol")
                    equipment_input = input("-> ")
                if equipment_input == "Salomon":
                        snowboard_item = Snowboard(equipment_id= "SBD-201", brand = "Salomon")
                elif equipment_input == "Burton":
                    snowboard_item = Snowboard(equipment_id= "SBD-202", brand = "Burton")
                elif equipment_input == "Rossignol":
                    snowboard_item = Snowboard(equipment_id= "SBD-203", brand = "Burton")
                if rental_input == "hourly":
                        hourly_rental.add_item(snowboard_item) 
                        hourly_cost = hourly_rental.calculate_best_item_price 
                elif rental_input == "daily":
                    daily_rental.add_item(snowboard_item) 
                    daily_cost = daily_rental.calculate_best_item_price 
                elif rental_input == "weekly":
                    weekly_rental.additem(snowboard_item)
                    weekly_cost = weekly_rental.calculate_best_item_price 
                print("finished? Y/N")
                finish_input = input("->")
                if finish_input == "Y":
                    print("Have a promocode? Y/N")
                    finish_input = input("-> ")
                    if finish_input == "Y":  
                            print("Enter a promo code")
                            promo_input = input("->")
                    else:
                        promo_input == ""           
                    if rental_input == "hourly":
                        grand_total = hourly_rental.calculate_total_bill(promo_input)
                        print("")
                        print(f"Total: ${grand_total:.2f}")
                        print("")
                    elif rental_input == "daily":
                        grand_total = daily_rental.calculate_total_bill(promo_input)
                        print("")
                        print(f"Total: ${grand_total:.2f}")
                        print("")
                    elif rental_input == "weekly":
                        grand_total = weekly_rental.calculate_total_bill(promo_input)
                        print("=" * 30)
                        print(f"Total: ${grand_total:.2f}")
                        print("=" * 30)
                    break
        except Exception as ex :
            print(f"An error has occurred, {ex=}, {type(ex)=}")
        

          
#def rental_return():

def show_inventory():
     print("=" * 65)
     print("Total amount of skis during the day:", rent_shop._available_skis)
     print("Total amount of snowboards during the day:", rent_shop._available_snowboards)
     print("=" * 65)

def end_of_day_report():
    print("=" * 65)
    print("                       End of Day Report                      ")
    print("=" * 65)
    print("")
    print("Total skis rented:", rent_shop.total_skis_rented_today)
    print("Total Snowboards rented:", rent_shop.total_snowboards_rented_today)
    print("Total daily revenue:", rent_shop.total_revenue_collected_today)
    print("=" * 65)



#Variables
promo_validation = False


#The boot up sequence
print("Starting up application...")
print("")
number_of_skis = int(input("Enter the number of skis: "))
number_of_skis = ValidateIntegerInput(number_of_skis)
number_of_snowboards = int(input("Enter the number of snowboards: "))
number_of_snowboards = ValidateIntegerInput(number_of_snowboards)
rent_shop = RentalShop(starting_skis = number_of_skis, starting_snowboards = number_of_snowboards)

print("Starting main menu...")
print("=" * 65)
print("                 Bob's Ski & Snowboard Rentals               ")
print("=" * 65)
print("")
while True:

    print("1. New Customer Rental")
    print("2. Rental Return")
    print("3. Show Inventory")
    print("4. End of Day")
    menu_input = input("-> ")

    if menu_input == "New Customer Rental":
        customer_rental()
    #elif menu_input == "Rental Return":
           #rental_return()
    elif menu_input == "Show Inventory":
           show_inventory()
    elif menu_input == "End of Day":
           end_of_day_report()
           break

