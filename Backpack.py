# Backpack.py
# Authors: Tyler Downey, Troy Green
""" Description:
    Contains all the functions used in the main.py program.
"""


# Global Functions:
def strandpad(value):
    valuestr = "${:,.2f}".format(value)
    valuepad = "{:>10}".format(valuestr)
    return valuepad

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
    

#### MAIN MENU ####
def print_menu():
    # Prints out a menu with headings and options 1 - 5.
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print("1. Enter an Employee Travel Claim.")
    print("2. Edit System Default Values.")
    print("3. Print the Travel Claim Report.")
    print("4. Graph Monthly Claim Totals.")
    print("5. Quit Program.")


def val_choice():
    # Presents user with an "Enter Choice" statement and gets a choice number (1 -5). Returns choice.
    while True:
        try: 
            choice = input("Enter Choice (1-5): ")
        except:
            Exception("Invalid Choice.")
        if choice == "":
            print("Choice cannot be blank.")
        elif int(choice) < 1 or int(choice) > 5:
            print("Choice must be 1 - 5.")
        elif len(choice) > 1:
            print("Choice must be one digit (1 - 5).")
        else:
            return choice

#### OPTION 1 ####

def enter_travel_claim():
    """ Gets input for travel claim and returns inputs and calculated values to a list (employee_data)."""
    
    # Get constants from TCDef.dat
    file = open("TCDef.dat", "r")
    claim_num = int(file.readline().strip())
    hst = float(file.readline().strip())
    low_perdiem_rate = float(file.readline().strip())
    high_perdiem_rate = float(file.readline().strip())
    mileage_rate = float(file.readline().strip())
    rent_rate = float(file.readline().strip())
    file.close()
    
    import datetime
    
    # Get claim number from TCDef.dat
    print(f"---CLAIM {claim_num}---")
    
    # Allow the user to enter information from the Travel Claim Form including the employee number, name, 
    # location of the trip, start date, end date, the number of days 
    employee_num = input("Employee Number: ")
    employee_name = input("Employee Name: ")
    location = input("Trip Location: ")
    start_date = input("Start Date (YY-MM-DD: ")
    end_date = input("End Date (YY-MM-DD): ")
    
    # Calculate number of days travelled (num_days)
    start_date_strp = datetime.datetime.strptime(start_date, "%y-%m-%d")
    end_date_strp = datetime.datetime.strptime(end_date, "%y-%m-%d")
    number_of_days = end_date_strp - start_date_strp
    num_days = int(number_of_days.days)
    
    # Determine if car is owned or rented and calculate car_cost
    own_or_rent = input("(O)wned or (R)ent?: ")
    
    if own_or_rent.upper() == "O":
        num_km = int(input("Distance Travelled (KM): "))
        car_cost = num_km * mileage_rate
    else:
        num_km = 0
        car_cost = num_days * rent_rate
    
    # Determine if days travelled <= 3 or > 4 and calculate perdiem amount based on perdiem rate (low or high)
    if num_days <= 3:
        perdiem_amount = num_days * low_perdiem_rate
    else:
        perdiem_amount = num_days * high_perdiem_rate
    
    # Calculate hst_ammount
    hst_amount = perdiem_amount * hst
    
    # Calculate total compensation
    total_amount = perdiem_amount + car_cost + hst_amount
    
    # Assign all inputs and calculated values to a list
    employee_data = [claim_num, employee_num, employee_name, location, start_date, end_date, num_days, own_or_rent.upper(), 
                    num_km, car_cost, perdiem_amount, hst_amount, total_amount]
    
    return employee_data


def print_and_save_data(data):
    """ Uses values from employee_list to assign variables and then prints all values to the screen."""
    # Get values for displaying from employee_data list
    claim_num = data[0]
    employee_num = data[1]
    employee_name = data[2]
    location = data[3]
    start_date = data[4]
    end_date = data[5]
    number_of_days = data[6]
    own_or_rent = data[7]
    num_km = data[8]
    car_cost = data[9]
    perdiem_amount = data[10]
    hst_amount = data[11]
    total_amount = data[12]
    
    # Display all inputs and calculated values to the screen
    print()
    print("---------CLAIM {}-----------------".format(claim_num))
    print("Employee Number: {}".format(employee_num))
    print("Employee Name:   {}".format(employee_name))
    print("Trip Location:   {}".format(location))
    print("Start Date:      {}".format(start_date))
    print("End Date:        {}".format(end_date))
    print("Total Days:      {}".format(number_of_days))
    if own_or_rent.upper() == "O":
        print("KM Travelled:    {}".format(num_km))
    else:
        pass
    print("-----------------------------------")
    print("Travel Expenses:  {}".format(strandpad(car_cost)))
    print("Perdiem Ammount:  {}".format(strandpad(perdiem_amount)))
    print("HST:              {}".format(strandpad(hst_amount)))
    print("Total:            {}".format(strandpad(total_amount)))
    print()
    
    # Save Data to Claims.dat
    employee_data = f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{data[9]},{data[10]},{data[11]},{data[12]}"
    f = open("Claims.dat", "a")
    f.writelines(str(employee_data + "\n"))
    f.close()
    
    # Write message to user saying claim has been processed and saved
    print("Claim has been processed and information has been saved.")
    
    # Update Claim Number
    replace_line("TCDef.dat", 0, f"{int(claim_num) + 1}\n")
    


#### OPTION 2 ####

def change_values():
    while True:
        # Get default data values from TCDef.dat
        file = open("TCDef.dat", "r")
        claim_num = int(file.readline().strip())
        hst = float(file.readline().strip())
        low_perdiem_rate = float(file.readline().strip())
        high_perdiem_rate = float(file.readline().strip())
        mileage_rate = float(file.readline().strip())
        rent_rate = float(file.readline().strip())
        file.close()
        
        # Print menu to change default values
        print("---NL CHOCOLATE COMPANY----")
        print("---CHANGE DEFAULT VALUES---")
        print(f"1. Claim Number:      {claim_num}")
        print(f"2. HST Rate:          {hst}")
        print(f"3. Low Perdiem Rate:  {low_perdiem_rate}")
        print(f"4. High Perdiem Rate: {high_perdiem_rate}")
        print(f"5. Mileage Rate:      {mileage_rate}")
        print(f"6. Rent Rate:         {rent_rate}")
        
        # Prompt user to enter line number to change
        while True:
            try: 
                line_to_change = int(input("Enter Choice (1-6): "))
            except:
                Exception("Invalid Choice.")
            if line_to_change == "":
                print("Choice cannot be blank.")
            elif int(line_to_change) < 1 or int(line_to_change) > 6:
                print("Choice must be 1 - 6.")
            elif len(str(line_to_change)) > 1:
                print("Choice must be one digit (1 - 6).")
            else:
                break
        
        # Prompt user to enter a new value        
        new_value = str(input(f"Enter New Value for Line {line_to_change}: " ))
        
        # Use line_to_change to determine line for new_value to replace
        replace_line("TCDef.dat", (line_to_change - 1), f"{new_value}\n")
        
        # Prompt user to change another line or break out of loop
        change_another_line = input("Change Another Line (Y/N)?: ")
        if change_another_line.upper() != "Y":
            break


#### OPTION 3 ####

def print_report():
    """Imports data from Claims.dat and print's out formatted report with a line for each claim."""
    
    import datetime
    cur_date = datetime.datetime.now()
    cur_date_s = datetime.datetime.strftime(cur_date, "%m-%d-%Y")
    
    # Initialize variables
    number_of_claims = 0
    perdiem_total = 0
    mileage_total = 0
    claim_total = 0
    
    # Print Headings
    print("                               NL CHOCOLATE COMPANY                            ")
    print()
    print("                     TRAVEL CLAIMS LISTING AS OF {}                          ".format(cur_date_s))
    print()
    print("  CLAIM   CLAIM       SALESPERSON      CLAIM             PER DIEM    MILEAGE   CLAIM    ")
    print("  NUMBER  DATE           NAME         LOCATION            AMOUNT     AMOUNT    AMOUNT   ")
    print("======================================================================================")
    
    # Read cata from file
    file = open("Claims.dat", "r")
    for line in file:
        # Get line data from Claims.dat
        employee_data = line.strip()
        employee_data_f = employee_data.split(",")
        claim_num = employee_data_f[0]
        claim_date = employee_data_f[4]
        employee_name = employee_data_f[2]
        location = employee_data_f[3]
        perdiem_amount = float(employee_data_f[10])
        mileage_amount = float(employee_data_f[9])
        claim_amount = float(employee_data_f[12])
        
        # Format Date
        claim_date_p = datetime.datetime.strptime(claim_date, "%y-%m-%d")
        claim_date_s = datetime.datetime.strftime(claim_date_p, "%d-%b-%y")
        
        # Acummulators
        number_of_claims += 1
        perdiem_total += perdiem_amount
        mileage_total += mileage_amount
        claim_total += claim_amount
        
        # Print values to screen
        print("   {}    {}   {:<15} {:<15} {} {} {}".format(claim_num, claim_date_s, employee_name, location, strandpad(perdiem_amount), strandpad(mileage_amount), strandpad(claim_amount)))
    file.close()
    
    # Print footer
    print("======================================================================================")
    print("{:>2} claims listed                                      {} {} {} ".format(number_of_claims, strandpad(perdiem_total), strandpad(mileage_total), strandpad(claim_total)))
    print()
    print("                                END OF REPORT                   ")
    
    input("Press Enter to Continue...")


#### OPTION 4 ####

def get_data():
    import datetime
    import matplotlib.pyplot as plt
    
    # Initialize month values
    month1 = 0
    month2 = 0
    month3 = 0
    month4 = 0
    month5 = 0
    month6 = 0
    month7 = 0
    month8 = 0
    month9 = 0
    month10 = 0
    month11 = 0
    month12 = 0
    
    # Initialize month list
    
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    # Get data from Claims.dat
    file = open("Claims.dat", "r")
    
    # Get month and claims data from Claims.dat
    for line in file:
        employee_data = line.strip()
        employee_data_f = employee_data.split(",")
        date = datetime.datetime.strptime(employee_data_f[4], "%y-%m-%d")
        month_val = str(date.month)
        claim_total = float(employee_data_f[12])
        
        # Determine month for claim entry
        if month_val == "1":
            month1 += claim_total
        elif month_val == "2":
            month2 += claim_total
        elif month_val == "3":
            month3 += claim_total
        elif month_val == "4":
            month4 += claim_total
        elif month_val == "5":
            month5 += claim_total
        elif month_val == "6":
            month6 += claim_total
        elif month_val == "7":
            month7 += claim_total
        elif month_val == "8":
            month8 += claim_total
        elif month_val == "9":
            month9 += claim_total
        elif month_val == "10":
            month10 += claim_total
        elif month_val == "11":
            month11 += claim_total
        elif month_val == "12":
            month12 += claim_total
        
    # Assign monthly totals to a list    
    monthly_totals = [month1, month2, month3, month4, month5, month6, month7, month8, month9, month10, month11, month12]
    
    # Assign month and monthly_totals to x and y variables
    x = month
    y = monthly_totals
    
    # Plot x and y values, label axis, and create title
    plt.plot(x, y)
    plt.xlabel("Month")
    plt.ylabel("Claim Totals")
    plt.title("Travel Claims for 2021")
    plt.show()