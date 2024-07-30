import json 
import os
import random


class JsonManager:
    """
    This class is applied to manage working with json files
    """

    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def check_existence(self):
        """
        This method checks the existence of the file and if the file is not empty
        """
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) != 0

    def read_file(self):
        """
        This method reads the data of the file
        """
        if self.check_existence():
            with open(self.file_name, mode="r") as file:
                return json.load(file)
        return []

    def write_file(self, all_data):
        """
        This method writes all data into the file
        """
        with open(self.file_name, mode="w") as file:
            json.dump(all_data, file, indent=4)
            return "Data is written to a file"

    def add_one_data_to_file(self, data: dict):
        """
        This method writes one given data into the file
        """
        all_data = self.read_file()
        all_data.append(data)
        self.write_file(all_data)

    def validate_data(self, data):
        """
        Validate if the given data has all necessary keys
        """
        required_keys = ['id', 'battery', 'location', 'model_name', 'price_per_minute']
        for key in required_keys:
            if key not in data:
                return False
        return True
    
    def get_all_data(self):
        """
        This method retrieves all valid data from the file
        """
        all_data = self.read_file()
        
        valid_data = []
        for data in all_data:
            if self.validate_data(data):
                valid_data.append(data)
                
        return valid_data
    
    def remove_data(self, identifier):
        """
        This method removes data from the file based on a given identifier
        """
        all_data = self.read_file()
        updated_data = [data for data in all_data if data.get('id') != identifier]

        if len(updated_data) < len(all_data):
            self.write_file(updated_data)
            return True
        else:
            print("Data with given ID not found.")
            return False
        
    

class ScooterOwner(JsonManager):
    """
    Class representing a scooter owner
    """

class ScooterOwner(JsonManager):
    """
    Class representing a scooter owner
    """

    def __init__(self, username, password, file_name="scooter_owners.json"):
        super().__init__(file_name)
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self):
        """
        Login method for scooter owner
        """
        entered_username = input("Enter your username: ").strip()
        entered_password = input("Enter your password: ").strip()

        if entered_username == self.username and entered_password == self.password:
            print("Login successful!")
            self.logged_in = True
            return True
        else:
            print("Incorrect username or password. Login failed.")
            return False

    def logout(self):
        """
        Logout method for scooter owner
        """
        self.logged_in = False
        print("Logged out successfully.")

    def add_scooter(self, scooter_data):
        """
        Method to add a new scooter
        """
        if self.logged_in:
            self.add_one_data_to_file(scooter_data)
            print("Scooter added successfully!")
        else:
            print("You need to login first to add a scooter.")

    def display_menu(self):
        """
        Display menu for scooter owner after logging in
        """
        while True:
            print("\nScooter Owner Menu:")
            print("1. Add Scooter")
            print("2. Logout")
            print("3. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                battery = input("Enter battery level: ")
                location = input("Enter scooter location: ")
                model_name = input("Enter scooter model name: ")
                price_per_minute = input("Enter price per minute: ")

                scooter = {
                    "id": random.randint(10, 99),
                    "battery": battery,
                    "location": location,
                    "model_name": model_name,
                    "price_per_minute": price_per_minute
                }
                self.add_scooter(scooter)

            elif choice == '2':
                self.logout()
                break

            elif choice == '3':
                print("Exiting Scooter Owner menu.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")


class Client(JsonManager):
    """
    Class representing a client
    """

    def __init__(self, username, password, file_name="clients.json"):
        super().__init__(file_name)
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self):
        """
        Login method for client
        """
        entered_username = input("Enter your username: ").strip()
        entered_password = input("Enter your password: ").strip()

        if entered_username == self.username and entered_password == self.password:
            print("Login successful!")
            self.logged_in = True
            return True
        else:
            print("Incorrect username or password. Login failed.")
            return False

    def logout(self):
        """
        Logout method for client
        """
        self.logged_in = False
        print("Logged out successfully.")

    def rent_scooter(self):
        """
        Method to rent a scooter
        """
        if self.logged_in:
            scooters = ScooterOwner(self.username, self.password).get_all_data()

            if scooters:
                print("\nAvailable Scooters:\n")
                for scooter in scooters:
                    print(f"ID: {scooter['id']}")
                    print(f"Location: {scooter['location']}")
                    print(f"Model: {scooter['model_name']}")
                    print(f"Price per minute: ${scooter['price_per_minute']}")
                    print("--------------------")

                scooter_id = input("Enter the ID of the scooter you want to rent: ")
                self.rent_scooter_by_id(scooter_id)

            else:
                print("No scooters available.")
        else:
            print("You need to login first to rent a scooter.")

    def rent_scooter(self):
        """
        Method to rent a scooter
        """
        if self.logged_in:
            scooters = ScooterOwner(self.username, self.password).get_all_data()

            if scooters:
                print("\nAvailable Scooters:\n")
                for scooter in scooters:
                    if self.validate_data(scooter):  # Validate each scooter entry
                        print(f"ID: {scooter['id']}")
                        print(f"Location: {scooter['location']}")
                        print(f"Model: {scooter['model_name']}")
                        print(f"Price per minute: ${scooter['price_per_minute']}")
                        print("--------------------")

                scooter_id = input("Enter the ID of the scooter you want to rent: ")
                self.rent_scooter_by_id(scooter_id)

            else:
                print("No scooters available.")
        else:
            print("You need to login first to rent a scooter.")

    def display_menu(self):
        """
        Display menu for client after logging in
        """
        while True:
            print("\nClient Menu:")
            print("1. View available scooters")
            print("2. Rent a scooter")
            print("3. Logout")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.view_available_scooters()

            elif choice == '2':
                self.rent_scooter()

            elif choice == '3':
                self.logout()
                break

            elif choice == '4':
                print("Exiting Client menu.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    def view_available_scooters(self):
        """
        Method to display available scooters
        """
        scooters = self.read_file()

        if scooters:
            print("\nAvailable Scooters:\n")
            for scooter in scooters:
                if 'id' in scooter:
                    print(f"ID: {scooter['id']}")
                    print(f"Location: {scooter['location']}")
                    print(f"Model: {scooter['model_name']}")
                    print(f"Price per minute: ${scooter['price_per_minute']}")
                    print("--------------------")
                else:
                    print("Invalid scooter data - missing 'id' key.")
        else:
            print("No scooters available.")

def register_owner():
    print("\nOwner Registration:\n")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    owner = ScooterOwner(username, password)
    owner.add_one_data_to_file({"username": username, "password": password})

    if owner.login():
        owner.display_menu()

def register_client():
    print("\nClient Registration:\n")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    client = Client(username, password)
    client.add_one_data_to_file({"username": username, "password": password})

    if client.login():
        client.display_menu()

def display_menu():
    print("Welcome to the Scooter Rental System.")

    while True:
        print("\nMain Menu:")
        print("1. Register as Owner")
        print("2. Register as Client")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            register_owner()

        elif choice == '2':
            register_client()

        elif choice == '3':
            print("Exiting Scooter Rental System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    display_menu()
