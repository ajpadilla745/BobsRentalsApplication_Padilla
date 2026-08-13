# BobsRentalsApplication_Padilla
An application for the final project known as Bob's Rentals
========================================
Name: Antonio Padilla
Course: Object-Oriented Programming
Repository used: BobsRentals_EW
========================================
========================================
#1. Start up
========================================
The application starts by adding the starting amount of equipment before proceeding to the main menu

========================================
#2. Main menu
========================================
This gives the user to choose to add rentals, process returns, Keep track of inventory, 
and an end of day report for the total amount of equipment rented alongside the daily revenue.

*The prompts have been changed to numbers to keep it consistent when selecting a menu in contrast to
 typing the name of the menu.
========================================
#3. New Customer Rental
========================================
This will first process the customer's name, ID, and which rental period to choose. 
Afterwards, it will ask for either skis or snowboards and then brand which then adds them into the "rental_shop" class.
The amount of inventory will not be subtracted until the rental is complete. 

*variables in this function (example: hourly_rental and customer_obj) are often delcared as global to help carry over info and process returns.
========================================
#4. Rental Return
========================================
This will process returns for any existing customer that would return any equipment rented. 
It will ask for the name and ID of the customer to search in the database for the matching info.
This keeps track of the revenue in the shop from every return completed.

========================================
#5. Show Inventory
========================================
This shows the available inventory for the day. 
*The amounts will decrease and increase depending on rentals and returns.

========================================
#6. End of Day
========================================
Calculates the total amount of skis and snowboards rented for the day alongside with the daily amount of revenue.