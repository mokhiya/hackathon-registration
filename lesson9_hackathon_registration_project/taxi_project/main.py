def display_user_menu():
    """
    This function is used to handle admin's menu
    """
    text = """
    1. Taxi driver.
    2. Client.
    3. Filter taxis.
    4. Filter clients.
    5. Show my announcmenets.
    6. Logout. """

    print(text)

    user_input = int(input("Choose a number from menu: "))

    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    else:
        print("Choose a proper number!")


def display_main_menu():
    """
    This function is used to handle main menu
    """
    print("Welcome to registration for hackathon.")
    
    text = """
    1. Register.
    2. Login.
    3. Exit. """

    print(text)

    user_input = int(input("Choose a number from menu: "))

    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quitted the program. See you!")
        else:
            return display_main_menu()
    else:
        print("Choose a proper number! ")
        return display_main_menu()
    
if __name__ == "__main__":
    display_main_menu()