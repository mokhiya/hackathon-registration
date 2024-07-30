import json 
import os

admin_login = "admin01"
admin_password = "1111"


class JsonManager:
    """
    This class is applied to manage working with json files
    """

    def __init__(self, file_name) -> None:
        self.file_name = file_name


    def check_existance(self):
        """
        This method checks the existance of the file and if the file is not empty
        """
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) != 0


    def read_file(self):
        """
        This method reads the data of the file
        """
        if self.check_existance():
                with open(self.file_name, mode="r") as file:
                    return json.load(file)
        return []
        

    def write_file(self, all_data):
        """
        This method writes all data into the file
        """
        with open(self.file_name, mode= "w") as file:
            json.dump(all_data, file, indent=4)
            return "Data is written to a file"


    def add_onedata_to_file(self, data: dict):
        """
        This method writes one given data into the the file
        """
        all_data = self.read_file()
        all_data.append(data)
        return self.write_file(all_data)
    
    def get_all_participants(self):
        """
        This method retrieves all participants from the file
        """
        return self.read_file()
    
    def removing_participants(self, team_name):
        all_data = self.read_file()
        updated_data = []

        for participant in all_data:
            if participant.get('Team_name') != team_name:
                updated_data.append(participant)

        if len(updated_data) < len(all_data):
            self.write_file(updated_data)
            return True
        else:
            print("There is no such team in the list. Please try again later.")
            return False


class Participant(JsonManager):
    """
    This class is applied to manage participant info

    Attributes:
        - full_name (str): gets full name of the group leader
        - contact (str): gets a contact of the group leader
        - team_name (str): gets a team name
        - file_name (json): inherits file_name attribute from JsonManager class.
    """
    def __init__(self, full_name, contact, team_name, file_name="participants.json"):
        super().__init__(file_name)
        self.full_name = full_name
        self.contact = contact
        self.team_name = team_name
        self.participants = []

    def add_team_member(self, member_name):
        """This method is used to add other team members to the list"""
        self.participants.append(member_name)

    def formatting_team(self):
        """This method is used to format input data in dict format"""
        return {
            'Leader_name': self.full_name,
            'Leader_contact': self.contact,
            'Team_name': self.team_name,
            'Other_participants': self.participants
        }
    

def register_participants():
    """
    This function is used to register participants
    """
    print("\nParticipant registration:\n")
    full_name = input("Enter your full name: ").title().strip()
    
    while True:  # Validating email format
        user_email = input("Enter your email: ").strip()
        if user_email.endswith('@gmail.com') or user_email.endswith('@mail.ru') or user_email.endswith('@yahoo.com'):
            break
        else:
            print("Invalid input, enter an email again!")
    
    team_name = input("Enter your team name: ").title().strip()
    
    while True:  # Adjusting maximum participants upto 5 including the leader
        participant_quantity = int(input("How many people do you want to add (including yourself)? "))
        if participant_quantity >= 3 and participant_quantity <= 5:  
            break
        else:
            print("Please enter between 3 to 5 participants (including yourself).")

    participant = Participant(full_name=full_name, contact=user_email, team_name=team_name)  # Making an object from  Participant class
    
    for i in range(participant_quantity - 1):  # Looping to add team members
        member_name = input(f"Enter participant {i+1} name: ").title().strip()
        participant.add_team_member(member_name)

    participant.add_onedata_to_file(participant.formatting_team())

    print("Data about your team has been saved successfully!")
    return display_menu()


def ckecking_admin():
    """
    This function is used to check admin's login and password
    """
    login  = input("Enter your login: ").strip()
    password = input("Enter your password: ").strip()

    if login == admin_login and password == admin_password:
        return display_admin_menu()
    print("Something went wrong with login or password. Note that only admins can log in!")
    return display_menu()

def printing_all_prticipants():
    """
    This function is used to print all teams
    """
    json_manager = JsonManager(file_name="participants.json")
    participants = json_manager.get_all_participants()
    
    if participants:
        print("\nAll Teams:\n")
        for participant in participants:
            print(f"Team: {participant['Team_name']}")
            print(f"Leader: {participant['Leader_name']} ({participant['Leader_contact']})")
            if participant['Other_participants']:
                print("Other Participants:")
                for name in participant['Other_participants']:
                    print(f"- {name}")
            print("--------------------")
    else:
        print("No participants found.")
    return display_admin_menu()

def remove_team_by_name():
    """
    This function is used to remove teams by their name
    """
    json_manager = JsonManager(file_name="participants.json")
    team_name = input("Enter the team name you want to remove: ").title().strip()
    json_manager.removing_participants(team_name)
    print(f"Team '{team_name}' has been removed successfully!")
    return display_admin_menu()

def display_admin_menu():
    """
    This function is used to handle admin's menu
    """
    text = """
    1. See all teams.
    2. Remove teams.
    3. Exit. """

    print(text)

    user_input = int(input("Choose a number from menu: "))

    if user_input == 1:
        printing_all_prticipants()
    elif user_input == 2:
        remove_team_by_name()
    elif user_input == 3:
        return display_menu()
    else:
        print("Choose a proper number!")

def display_menu():
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
        participant = register_participants()
        print(participant.formatting_team())
    elif user_input == 2:
        if ckecking_admin():
            display_admin_menu()
    elif user_input == 3:
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quitted the program. See you!")
        else:
            return display_menu()
    else:
        print("Choose a proper number! ")
        return display_menu()
    
if __name__ == "__main__":
    display_menu()