import random
user_choice=int(input("enter \n0 for rock\n1.for paper and \n2.for scissor\n "))


if user_choice>=3 or user_choice<0:
    print("invalid number")

else:
    computer_choice=random.randint(0,2)
    print("computer choice:",computer_choice)

    if computer_choice==user_choice:
        print("its a tie")

    elif computer_choice==0 and user_choice==2:
        print("user loose")

    elif computer_choice==2 and user_choice==0:
        print("user win")

    elif computer_choice>user_choice:
        print("user lose")
    
    elif user_choice>computer_choice:
        print("user wins")




