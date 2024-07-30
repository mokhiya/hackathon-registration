from datetime import datetime
from file_manager import taxi_ann_manager

# regions = (
#     "Andijan", "Namangan", "Fergana", "Navoiy", "Buxoro", "Samarkand",
#     "Khorazm", "Surhandarya", "Qashqadaryo", "Sirdarya", "Tashkent", "Tashkent city",
#     "Karakalpakstan"
# )

regions = {
    "1": "Andijan", "2": "Namangan", "3": "Fergana"
}


class Announcement:
    def __init__(self, from_place, to_place, price, expire_time):
        self.from_place = from_place
        self.to_place = to_place
        self.price = price
        self.expire_time = expire_time
        self.is_active = True
        self.created_at = str(datetime.now())


class ClientAnnouncement(Announcement):
    print(regions)
    from_place = input("Where are you: ")
    while from_place not in regions.keys():
        from_place = input("Where are you: ")
    else:
        from_place = regions[from_place]

    print(regions)
    to_place = input("Where you want to go: ")
    while to_place not in regions.keys():
        to_place = input("Where you want to go: ")
    else:
        to_place = regions[to_place]
        if from_place == to_place:
            print("Wrong regions selected")

    price = input("How much do is the cost per seat: ")
    expire_time = input("How many hours it should be valid: ")
    
    client = Announcement(from_place=from_place, to_place=to_place, price=price, expire_time=expire_time)
    


class TaxiAnnouncement(Announcement):
    def __init__(self, from_place, to_place, price, car_name, comment, expire_time, seats):
        super().__init__(from_place, to_place, price, expire_time)
        self.car_name = car_name
        self.comment = comment
        self.seats = seats


def add_announcement_as_taxi():
    try:
        print(regions)
        from_place = input("Where are you: ")
        while from_place not in regions.keys():
            from_place = input("Where are you: ")
        else:
            from_place = regions[from_place]

        print(regions)
        to_place = input("Where you want to go: ")
        while to_place not in regions.keys():
            to_place = input("Where you want to go: ")
        else:
            to_place = regions[to_place]
            if from_place == to_place:
                print("Wrong regions selected")
                add_announcement_as_taxi()

        price = input("How much do is the cost per seat: ")
        expire_time = input("How many hours it should be valid: ")
        car_name = input("What kind of car: ")
        seats = input("How many seats are available: ")
        comment = input("Enter comment: ")

        taxi = TaxiAnnouncement(from_place, to_place, price, car_name, comment, expire_time, seats)
        print(taxi.__dict__)
        taxi_ann_manager.add_data(taxi.__dict__)
        print("Announcement added")
        return True
    except Exception as e:
        print(e)
        return False

