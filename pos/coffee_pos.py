from transactions import *
import promotion
import starbuzz

# The array of the menu options
items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
# This is the matching array of menu prices
prices = [1.50, 2.20, 1.80, 1.20]
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
        price = promotion.discount(prices[choice - 1])
        if input("Starbuzz_card? ") == "y":
            price = starbuzz.discount(price)
        save_transaction(price, credit_card, items[choice - 1])

