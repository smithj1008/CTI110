    #Jaylen Smith
    #4/7/2024
    #P4LAB2
    #Assignment tests student's knowledge of how to write code that displays information to users
first_integer = int(input())
second_integer = int(input())



if second_integer < first_integer:
    print("Second integer can't be less than the first.")
else:

    current_value = first_integer
    while current_value <= second_integer:
        print(current_value, end=' ')
        current_value += 5

