# main.py
# Authors: Tyler Downey, Troy Green
# Date: March 13th, 2021
""" Description:
    Travel Claim processing program for NL Chocolate Company.
    Presents a menu with five choices and then gets choice input from user.
    Allows user to enter travel claims, edit default values, print summaries of claims, and graph monthly claim totals.
"""

from Backpack import *


# Main Loop
while True:
    # Print the Menu
    print_menu()
    
    # Get and validate choice input
    choice = val_choice()
    
    # Make decision based on choice value
    if choice == "1":
        while True:
            travel_data = enter_travel_claim()
            print_and_save_data(travel_data)
            try:
                another_claim = input("Enter another claim (Y/N)?: ")
            except:
                Exception("Invalid Option")
            if another_claim.upper() != "Y":
                break
            else:
                pass
            
    elif choice == "2":
        change_values()
        
    elif choice == "3":
        print_report()
        
    elif choice == "4":
        get_data()
        
    elif choice == "5":
        break

