import random

# Generate the Random number between 1 to 10
win = random.randint(1,10)

# Ask user name
user_name = input("Enter your name: ")
i = 1

# Main game loop
while True:
    if user_name: # Check if user has entered their name
        print(f"\nWelcome {user_name} to the Number Guessing Game!")
        user_num = input("\nEnter your number: ")
        while True:
            if user_num: # Check if user has entered their number
                while True:
                    if int(user_num) == win:
                        print(f"\nCongratulations {user_name}, You Win! in {i} times")
                        break
                    else:
                        # Hint if guess is wrong
                        if int(user_num) < win:
                         print(f"{user_num} is less than the winning number")
                        else:
                            print(f"{user_num} is greather than the winning number")
                        
                        # For guess the number again 
                        user_num = input("\nGuess Again!: ")
                        if user_num: # Check user entered the number
                            pass
                        else:
                            print("Game Over!\nYou didn't enter the number")
                            break
                        i += 1
                break
            else:
                # Prompt the user to enter a number
                user_num = input("Please enter a number to start the Game: ")
        break
    else:
        # Prompt the user to enter their name
        user_name = input("Please enter your name: ")