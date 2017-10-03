from transactions import *

# The array of the menu options
items = ["WORKOUT", "WEIGHTS", "BIKES"]
# This is the matching array of menu prices
prices = [35.0, 10.0, 8.0]
running = True

while running:
    option = 1
    # Display the program's menu
    for choice in items:
        print(str(option) + ". " + choice)
        option = option + 1

    print(str(option) + ". Quit")
    # Prompt for the user to enter a menu option number
    choice = int(input("Choose an option: "))

    # This will be True if the user selects the LAST option on the menu
    # which is "Quit"
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        save_transaction(prices[choice - 1], credit_card, items[choice - 1])

