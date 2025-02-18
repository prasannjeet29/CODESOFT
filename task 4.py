import random  

# Initialize scores  
user_score = 0  
computer_score = 0  

while True:  
    # User input  
    try:  
        user_choice = int(input("\nEnter your choice:\n0 for Rock\n1 for Paper\n2 for Scissors\n"))  
        if user_choice not in [0, 1, 2]:  
            print("Invalid choice! Please enter 0, 1, or 2.")  
            continue  
    except ValueError:  
        print("Invalid input! Please enter a number (0, 1, or 2).")  
        continue  

    # Computer choice  
    computer_choice = random.randint(0, 2)  
    choices = ["Rock", "Paper", "Scissors"]  
    print(f"\nYou chose: {choices[user_choice]}")  
    print(f"Computer chose: {choices[computer_choice]}")  

    # Determine the winner  
    if user_choice == computer_choice:  
        print("It's a tie!")  
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):  
        print("You win!")  
        user_score += 1  
    else:  
        print("You lose!")  
        computer_score += 1  

    # Display scores  
    print(f"\nScore: You - {user_score} | Computer - {computer_score}")  

    # Ask to play again  
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()  
    if play_again != "yes":  
        print("\nThanks for playing! Final Score:")  
        print(f"You - {user_score} | Computer - {computer_score}")  
        break