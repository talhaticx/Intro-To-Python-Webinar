a = 0
b = 100

guess = int((a+b)/2) # mean

while True:
    print(f"Is the number {guess} correct? (y/n)")
    response = input().lower()

    if response == 'y':
        print("Congratulations, you've found the number!")
        break
    
    elif response == 'n':
        print("Enter 'l' for lower, or 'h' for higher.")
        direction = input().lower()

        if direction == 'l':
            b = guess
        elif direction == 'h':
            a = guess
        else:
            print("Invalid input. Please enter 'l' or 'h'.")
            continue

        guess = int((a+b)/2)
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue