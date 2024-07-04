
num1= float(input("Enter First No: "))
num2= float(input("Enter Secound No: "))
print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")

C= int(input("Enter Operator from 1-4: "))
if C==1:
    print(num1 + num2)
elif C==2:
    print(num1 - num2)
elif C==3:
    print(num1 * num2)
elif C==4:
    print(num1 / num2)
else:
    print("Invalid Input")
    
    
    