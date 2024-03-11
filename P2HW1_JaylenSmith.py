    #Jaylen Smith
    #3/10/2024
    #P2LAB2
    #Assignment assess student ability to edit and enhance exiting programs
print("This program calculates and displays travel expenses")
budget = float(input("Enter budget : "))   # reading user budget
destination = input("Enter your Travel destination : ")    # reading user destination
gas_expenses = float(input("How much do you think you will spend on gas : "))    # reading user fuel expenses
accomodation = float(input("Approximately how much you need for accomodation/hotel ? : "))    # reading user hostel expenses
food_expenses = float(input("Last, how much do you need for food? : "))     # reading user food expenses
remaining_balance = budget - gas_expenses - accomodation - food_expenses    # calculating remaining balance
print("------------------------------travel expenses----------------------------------")
print("Location : " + destination)
print("Initial budget : " + str(budget))
print("Fuel : " + str(gas_expenses))
print("Accomodation/hotel : " + str(accomodation))
print("Food : " + str(food_expenses))
print("Remaining balance : " + str(remaining_balance))
