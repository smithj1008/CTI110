    #Jaylen Smith
    #04/14/2024
    #P4HW2
    #Assignment assess student ability to edit and enhance exiting programs

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
total_employees = 0
overtime_hours = 0


while True:
    employee_name = input("Enter employee's name or 'None' to terminate: ")
    
    if employee_name.lower() == 'none':
        break
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    
    if hours_worked <= 40:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
    else:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    
    gross_pay = regular_pay + overtime_pay
    
    
    total_employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    
    
    print(f"Employee name: {employee_name}\n")
    print(f"Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
    print("-" * 100)
    print(f"{hours_worked:.1f}\t\t{pay_rate:.2f}\t{overtime_hours:.1f}\t\t"
          f"${overtime_pay:.2f}\t\t${regular_pay:.2f}\t\t${gross_pay:.2f}\n")


print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
