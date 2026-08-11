#=======================================================
# Name: Antonio Padilla
# Course: Object-Oriented Programming
# Assignment: Final Project PT.2
#=======================================================
from customer import Customer
from rental import Rental
from rental_shop import RentalShop




print("Starting up application...")
print("")
number_of_skis = input("Enter the number of skis: ")
number_of_snowboards = input("Enter the number of snowboards: ")
shop = RentalShop(starting_skis = number_of_skis, starting_snowboards = number_of_snowboards)

print("Starting main menu...")
print("=" * 65)
print("                 Bob's Ski & Snowboard Rentals               ")
print("=" * 65)
print("")
print("1. New Customer Rental")
print("2. Rental Return")
print("3. Show Inventory")
print("4. End of Day")
menu_input = input("-> ")
