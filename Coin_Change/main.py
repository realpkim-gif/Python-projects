running = True

while running:
    global money
    print("This app will find out the minimum amount of coins needed in order to give a certain change\n")
    while True:
        amount = input("How much money? ")
        #exeption handling
        try:
            #split into two lists
            parts = amount.split('.')
            if len(parts) > 1 and len(parts[1]) > 2:
                print("Please enter a number with no more than 2 decimal places.\n")
                continue
            else:
                money = float(amount)
                if money < 0:
                    print("Please enter a positive number.\n")
                    continue
                break
        except ValueError:
            print("Please enter a number, not a string.\n")
            continue

    #Convert to cents (float not good)
    cents = round(money * 100)

    #Change finding
    Dollar = cents // 100
    cents = cents % 100
    print(Dollar, " dollars")

    Half_amount = cents // 50
    cents = cents % 50
    print(Half_amount, " 50 cent coins")

    Quarter = cents // 25
    cents = cents % 25
    print(Quarter, " 25 quarter coins")

    Dime = cents // 10
    cents = cents % 10
    print(Dime, " 10 cent coins")

    Nickel = cents // 5
    cents = cents % 5
    print(Nickel, " 5 cent coins")

    Penny = cents
    print(Penny, " 1 cent coins \n \n")

    #Continue or Not
    while True:
        go = input("Would you like to continue? (Y/N): ")

        if go == "Y" or go == "y":
            break
        elif go == "N" or go == "n":
            running = False
            break
        else:
            print("Invalid input\nAnswer Y or N\n")

    print("\n"*100)
