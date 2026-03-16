# 💸 Smart Personal Finance Manager 💸
# Built by Bhagyashri and Team Neural Knights

print("--- Welcome to the Neural Knights Expense Tracker ---")

# This is an infinite loop that keeps our menu running!
while True:
    print("\n--- Main Menu ---")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Exit the tracker")
    
    # Asking the user what they want to do
    choice = input("What do you want to do? (Enter 1, 2, or 3): ")
    
    # Checking the user's choice using simple if-else conditions
    if choice == '1':
        print("Okay! We will add the logic to store your money here tomorrow.")
        
    elif choice == '2':
        print("Okay! We will add the logic to show your list here tomorrow.")
        
    elif choice == '3':
        print("Bye bye! Have a great day!")
        break # This breaks the infinite loop and stops the program
        
    else:
        print("Oops! Invalid choice. Please type 1, 2, or 3.")
