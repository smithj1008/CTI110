    #Jaylen Smith
    #04/14/2024
    #P4HW1
    #Assignment assess student ability to edit and enhance exiting programs
n = int(input("How many scores do you want to enter? "))

score = []

for i in range(n):
    
    
    
    s = int(input("Enter a score #"+str(i+1)+": "))
    
    
    while(s<1 or s>100):
        print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
        s = int(input("Enter score #"+str(i+1)+" again: "))
    
    score.append(float(s))

print("\n----------------Results----------------")

low =min(score)
print("Lowest Score  :",low)

score.remove(low)

print("Modified List :",score)

avg = sum(score)/len(score)

print("Scores Average: %.2f" %avg)

if(avg>90 and avg<=100):
    print("Grade         : A")
elif(avg>80 and avg<=90):
    print("Grade         : B")
elif(avg>70 and avg<=80):
    print("Grade         : C")
elif(avg>60 and avg<=70):
    print("Grade         : D")
elif(avg>50 and avg<=60):
    print("Grade         : E")
else:
    print("Grade         : F")
print("---------------------------------------")

    



    
