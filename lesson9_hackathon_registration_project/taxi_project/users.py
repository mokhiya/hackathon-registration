from file_manager import JsonManager

class User(JsonManager):
    """
    This class is applied to manage participant info

    Attributes:
        - full_name (str): gets full name of the group leader
        - contact (str): gets a contact of the group leader
        - team_name (str): gets a team name
        - file_name (json): inherits file_name attribute from JsonManager class.
    """
    def __init__(self, full_name, contact, file_name="users.json"):
        super().__init__(file_name)
        self.full_name = full_name
        self.contact = contact


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