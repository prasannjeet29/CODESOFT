print("\n\nmaking calculatoer using python to perform operation like addition,subtraction, multiplication & division4\n")
num1=int(input("enter 1st number\n"))
num2=int(input("enter 2nd number\n"))
operation=int(input("\nenter \n1.for addition \n2.for subtraction \n3.for mul & \n4for div\n"))

if operation==1:
    print("addition=",num1+num2)

elif operation==2:
    print("subtraction=",num1-num2)

elif operation==3:
    print("multiplication=",num1*num2)

elif operation==4:
    print("division=",num1/num2)

else:
    print("\nenter valid operation number\n")