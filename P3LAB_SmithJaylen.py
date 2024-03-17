    #Jaylen Smith
    #3/17/2024
    #P3LAB
    #Assignment tests student's knowledge of how to write code that displays information to users
is_leap_year = False
input_year = int(input())


if input_year % 4 == 0:
   
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            is_leap_year = True
    else:
        is_leap_year = True


if is_leap_year:
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")


        
        
            
            
                
        


    
