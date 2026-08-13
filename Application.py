#=======================================================
# Name: Antonio Padilla
# Course: Object-Oriented Programming
# Assignment: Final Project Pt.2
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
            if customer_input == "":
                raise Exception("Invalid name")
            print("Enter customer ID")
            id_input = int(input("->"))
            id_input = ValidateIntegerInput(id_input)
            if id_input != "":
                global customer_obj
                customer_obj = Customer(customer_id = id_input, name = customer_input)
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
                    global hourly_rental
                    hourly_rental = Rental(customer = customer_obj, rental_period_type = rental_input, duration = duration_input)
            elif rental_input == "daily":
                    global daily_rental
                    daily_rental = Rental(Customer, rental_period_type = rental_input, duration = 1)
            elif rental_input == "weekly":
                        global weekly_rental
                        weekly_rental = Rental(Customer, rental_period_type = rental_input, duration = 1)
            else:
                raise Exception("invalid input")
            
            while True:
                print("Select a rental type")
                print("1. Skis")
                print("2. Snowboards")
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
                    elif rental_input == "daily":
                        daily_rental.add_item(ski_item) 
                    elif rental_input == "weekly":
                        weekly_rental.add_item(ski_item)

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
                        snowboard_item = Snowboard(equipment_id= "SBD-203", brand = "Rossignol")
                    if rental_input == "hourly":
                        hourly_rental.add_item(snowboard_item) 
                    elif rental_input == "daily":
                        daily_rental.add_item(snowboard_item)
                    elif rental_input == "weekly":
                        weekly_rental.add_item(snowboard_item)



                print("Complete rental? Y/N")
                finish_input = input("->")
                if finish_input == "Y":
                    print("Enter a promo code")
                    global promo_input
                    promo_input = input("->")         
                    if rental_input == "hourly":
                        grand_total = hourly_rental.calculate_total_bill(promo_input)
                        rent_shop.check_and_rent_inventory(hourly_rental)
                        print("")
                        print(f"Total: ${grand_total:.2f}")
                        print("")
                    elif rental_input == "daily":
                        grand_total = daily_rental.calculate_total_bill(promo_input)
                        rent_shop.check_and_rent_inventory(daily_rental) 
                        print("")
                        print(f"Total: ${grand_total:.2f}")
                        print("")
                    elif rental_input == "weekly":
                        grand_total = weekly_rental.calculate_total_bill(promo_input)
                        rent_shop.check_and_rent_inventory(weekly_rental)
                        print("")
                        print(f"Total: ${grand_total:.2f}")
                        print("")
                    print("")
                    print("The rental is complete")
                    print("")
                    break
        except Exception as ex :
            print(f"An error has occurred, {ex=}, {type(ex)=}")
        

#This is to process returns for any rental equipment and a bill to collect revenue    
def rental_return():
    while True:
        try:
            if rent_shop.total_skis_rented_today == 0 and rent_shop.total_snowboards_rented_today == 0:
                print("")
                print("No rentals have been made today")
                print("")
                break
            else:
                print("Enter the customer's name")
                customer_input = input("-> ")
                if customer_input != "":
                    print("Enter customer ID")
                id_input = int(input("->"))
                id_input = ValidateIntegerInput(id_input)
                if id_input != "":
                    if id_input == customer_obj.customer_id and customer_input == customer_obj.name:
                        print("Customer has been found!")
                else:
                 print("No rentals have been made by this person/group")
                 break
                print(f"Name: {customer_obj.name}")
                print(f"ID: {customer_obj.customer_id}")
                if hourly_rental.rental_period_type == "hourly":
                    print(f"Rental Period: {hourly_rental.rental_period_type}")
                    print("Processing return...")
                    rent_shop.process_return_to_inventory(hourly_rental, promo_input)
                elif daily_rental.rental_period_type == "daily":
                    print(f"Rental Period: {daily_rental.rental_period_type}")
                    print("Processing return...")
                    rent_shop.process_return_to_inventory(daily_rental, promo_input)
                elif weekly_rental.rental_period_type == "weekly":
                    print(f"Rental Period: {weekly_rental.rental_period_type}")
                    print("Processing return...")
                    rent_shop.process_return_to_inventory(weekly_rental, promo_input)
                print("Return was successful")
            break
        except Exception as ex :
            print(f"An error has occurred, {ex=}, {type(ex)=}")
               
#Shows the current inventory available for rent
def show_inventory():
     print("=" * 65)
     print("Total amount of skis during the day:", rent_shop._available_skis)
     print("Total amount of snowboards during the day:", rent_shop._available_snowboards)
     print("=" * 65)

#A report calculating all the skis, snowboards, and revenue collected for the day.
def end_of_day_report():
    print("=" * 65)
    print("                       End of Day Report                      ")
    print("=" * 65)
    print("")
    print("Total skis rented:", rent_shop.total_skis_rented_today)
    print("Total Snowboards rented:", rent_shop.total_snowboards_rented_today)
    print(f"Total daily revenue: {rent_shop.total_revenue_collected_today:.2f}")
    print("=" * 65)


#The boot up sequence
print("Starting up application...")
print("")
number_of_skis = int(input("Enter the number of skis: "))
number_of_skis = ValidateIntegerInput(number_of_skis)
number_of_snowboards = int(input("Enter the number of snowboards: "))
number_of_snowboards = ValidateIntegerInput(number_of_snowboards)
rent_shop = RentalShop(starting_skis = number_of_skis, starting_snowboards = number_of_snowboards)

#The main menu used to navigate through
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

    if menu_input == "1":
        customer_rental()
    elif menu_input == "2":
           rental_return()
    elif menu_input == "3":
           show_inventory()
    elif menu_input == "4":
           end_of_day_report()
           break

