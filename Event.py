from datetime import time
from datetime import timedelta
from datetime import datetime

preparation_time = 30
donation_time = 30

class EventData(object):

    # @Nori
    # Definition explanation comes here...
    @staticmethod
    def get_event_date():
        global ev_date

        isvaild = False
        while not isvaild:
            data = input("Enter your Event date (YYYY.MM.DD):")
            try:
                ev_date = datetime.strptime(data, "%Y.%m.%d") # Csak akkor engedi tovább az adatot ha ilyen formátumba van
                if ev_date.isoweekday() != 6 and ev_date.isoweekday() != 7:
                    if (ev_date.date() - datetime.now().date()).days > 10:
                        isvaild = True
                    else:
                        print("Your donation date have to be 10 days later from now")
                else:
                    print("Event of date must not be on weekends")
            except ValueError:
                print(data, "is not vaild date! Try again(YYYY.MM.DD): ex: 2010.10.10")
        return ev_date
    # @Nori
    # Definition explanation comes here...
    @staticmethod
    def get_donation_start():
        global don_start
        isvaild = False
        while not isvaild:
            data = input("Enter your Start of donation (HH:MM):")
            try:
                don_start = datetime.strptime(data, "%H:%M") # Csak akkor engedi tovább az adatot ha ilyen formátumba van
                isvaild = True
            except ValueError:
                print(data, "is not a valid time! HH:MM. ex: 13:10")
        return don_start

    # @Bandi
    # Definition explanation comes here... A donation event vége. HH:MM formátmban, pl 12:10
    @staticmethod
    def get_donation_end():
        global don_end
        isvaild = False
        while not isvaild:
            data = input("Enter your End of donation (HH:MM):")
            try:
                don_end = datetime.strptime(data, "%H:%M") # Csak akkor engedi tovább az adatot ha ilyen formátumba van
                if don_start < don_end:
                    isvaild = True
                else:
                    print("Donation End have to be later thad Donation Start! (Donation start:", don_start.strftime("%H:%M"), "):")
            except ValueError:
                print(data, "is not a valid time! HH:MM. ex: 13:10")
        return don_end
    # @Bandi
    # Definition explanation comes here... nem nulla az els? szám, és 4 karakter valamint csak számok.

    @staticmethod
    def get_zip_code():
        ZIP = None
        isvaild = False
        while not isvaild:
            ZIP = input("Enter your ZIP CODE (XXXX):")

            try:
                if int(ZIP) and len(ZIP) == 4:

                    if ZIP[0] != "0":
                        isvaild = True
                    else:
                        print(ZIP, "is not vaild! 1. number must not be 0!")
                else:
                    print("ZIP must be 4 digits!")
            except ValueError:

                print("Only Numbers!")
        return ZIP

    # @Atilla
    # Asks for the donor's city.
    @staticmethod
    def get_city():
        cities = ["Miskolc", "Kazincbarcika", "Szerencs", "Sarospatak"]
        # Asks for the input here first.
        city = input("Please enter the donor's city: ")
        # Keeps asking for the city while it does not match one from the cities list.
        while city not in cities:
            city = input("Donor's are accepted only from the following cities:\
            Miskolc, Kazincbarcika, Szerencs and Sarospatak: ")
        # Returns with the city.
        return city

    # @Atilla
    # Asks for the donor's address.
    @staticmethod
    def get_address():
        # Asks for the input here first.
        street = input("Please enter the donor's address: ")
        # Keeps asking for the address while it does not less or equal than 25 characters.
        while not len(street) <= 25:
            street = input("The address should be less than 25 characters!: ")
        # Returns with the address.
        return street

    @staticmethod
    def get_available_beds():
        global available_beds
        isvalid = False

        while not isvalid:
            available_beds = input("Please enter the number of available beds: ")
            isvalid = available_beds.isdigit()
            if not isvalid:
                print("Please enter only numbers!")

        return available_beds

    @staticmethod
    def get_max_donor_number():
        global max_donor_number
        event_duration_in_minutes = don_end - don_start
        event_duration_in_minutes = timedelta.total_seconds(event_duration_in_minutes) // 60
        max_donor_number = ((event_duration_in_minutes - preparation_time) // donation_time) * int(available_beds)
        return max_donor_number

    # The function asks for the planned donor number
    @staticmethod
    def get_planned_donor_number():
        global planned_donor_number
        isvalid = False

        while not isvalid:
            planned_donor_number = input("Please enter the planned donor number for the event: ")
            isvalid = planned_donor_number.isdigit() and int(planned_donor_number) <= max_donor_number

            if not planned_donor_number.isdigit():
                print("Please enter only numbers!")

            if not int(planned_donor_number) <= max_donor_number:
                print("That's too much donor for the event! The max donor number is: %.d" % max_donor_number)

            if not isvalid:
                print("Try again!")

        return planned_donor_number

    # @Adam
    # Definition explanation comes here...

    # The function calculates how successful the event was
    @staticmethod
    def success_rate():
        successfull_donor_numbers = input("Please enter how many successfull donations were during donation event (x out of %s): " % planned_donor_number)
        if float(successfull_donor_numbers) / float(planned_donor_number) < 0.2:
            print("pina1")
        if 0.2 <= float(successfull_donor_numbers) / float(planned_donor_number) <= 0.75:
            print("pina2")
        if 0.75 <= float(successfull_donor_numbers) / float(planned_donor_number) <= 1.1:
            print("pina3")
        if float(successfull_donor_numbers) / float(planned_donor_number) > 1.1:
            print("pina4")