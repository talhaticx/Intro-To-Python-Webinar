def printMenu():
    print("Enter 1 to display current amount\nEnter 2 to deposit money\nEnter 3 to withdraw money\nEnter q to quit")

AMOUNT = 10000

while True:
    printMenu()
    choice = input("Enter: ")
    print()
    
    if choice == "q":
        print('Thanks for using ATM Service.')
        break

    if choice == "1":
        print(f"The current amount is {AMOUNT}")

    elif choice == "2":
        deposit = int(input("Enter the amount to deposit: "))
        AMOUNT += deposit
        print(f"Amount after deposit: {AMOUNT}")

    elif choice == "3":
        withdrawal = int(input("Enter the amount to withdraw: "))
        
        if withdrawal <= AMOUNT:
            AMOUNT -= withdrawal
            print(f"Amount after withdrawal: {AMOUNT}")
            
        else:
            print("Insufficient funds")
            
    else:
        print("Invalid choice")
    
    print() 