#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from datetime import datetime
from sys import exit
# Imports the sys.exit command. In case of wrong data it exits.

enter = "Enter your"  # An abbrevation.
Blood_types = ["a", "b", "ab", "0"] # Blood types in a list with lower case.


class DonorData(object):

    # WEIGHT
    @staticmethod
    def get_weight():
        global Weight  # Can be used outside the definition.
        isvalid = False  # A variable for the try/except.
        while not isvalid:  # Until it is not true.
            Weight = input("Please %s weight in the following format, 62: " % enter)
            try:  # If the entered data is an integer.
                int(Weight)
                isvalid = True
            except ValueError:  # Tries again.
                print("Nice, but", Weight, "is not a egész number. Try again! \n")
        return int(Weight)  # If correct, then return with the data.

    # BLOOD TYPE
    @staticmethod
    def get_blood_type():
        global Blood  # Can be used outside the definition.
        isvalid = False  # A variable for the try/except.
        while not isvalid:
            Blood = input("%s blood type (A, B, AB or 0): " % enter)
            try:
                if str(Blood).lower() in Blood_types:  # Converts input to lower case and checks if it matches the list.
                    isvalid = True
                else:
                    print("Your bloodtype should be A , B , AB or 0! Try again!")
            except: # No idea why we need this here, but won't run without it.
                pass
        return Blood  # If correct returns with the data.

    # ID EXPIRATION DATE
    @staticmethod
    def get_exp_date():
        global date_of_exp   # Can be used outside the definition.
        isvaild = False  # A variable for try/except.
        while not isvaild:
            data = input("Please enter the donor's ID expiration date in the following format, 2000.12.31: ")
            try:
                date_of_exp = datetime.strptime(data, "%Y.%m.%d")  # Only let the data pass if it matches this format.
                if date_of_exp > datetime.now():
                    isvaild = True
                elif date_of_exp < datetime.now():
                    date_of_exp = False
                    return False
            except:
                print("Wrong format. Please try again in the following format, 2000.12.31: ")
        return date_of_exp

    # HEMOGLOBIN LEVEL
    # Generates a random number: hemogblobin level between 80-200, that must be higher than 110.
    @staticmethod
    def hemo_level():
        global level # Can be used outside the definition
        level = (random.randrange(80, 200))  # generates a number between 80 and 200.
        if level > 110:
            return level  # If it is greater than 110, return with it.
        else:
            exit("Your Hemogblobin level is not high enough.")  # If it is lesser than 110, it exits.

    # EMAIL ADDRESS
    @staticmethod
    # Email address
    def get_email_address():  # The function asks for a valid email address
        global email_address
        isvalid = False
        while not isvalid:
            email_address = input("%s email address: " % enter)
            email_address_string = email_address.replace(" ", "")
            contains_at_sign = "@" in email_address_string and email_address_string.index("@") > 0
            ending_is_valid = email_address_string.endswith(".hu") or email_address_string.endswith(".com")
            isvalid = contains_at_sign and ending_is_valid
            if not isvalid:     # If it's not a valid address, the user gets this message.
                print("The given '%s' email address is not in a valid format!" % email_address)
            if not contains_at_sign:        # If the address misses an '@' sign, the user gets this message as well.
                print("Please add an '@' sign in your address!")
            if not ending_is_valid:                               # If the address misses the email providers location,
                print("Please specify where your email provider is ('.com' or '.hu')!")   # the user gets this message.
        return email_address

    # MOBILE NUMBER
    @staticmethod
    # Mobile number
    def get_mobile_number():  # The function asks for a valid mobile number
        global mobile_number
        isvalid = False
        while not isvalid:
            mobile_number = input("%s mobile number: " % enter)
            mobile_number_string = mobile_number.replace(" ", "")
            startswith_36_or_06 = mobile_number_string.startswith("+36") or mobile_number_string.startswith("06")
            contains_20_30_70 = "20" in mobile_number_string or "30" in mobile_number_string\
                                    or "70" in mobile_number_string
            valid_length = len(mobile_number_string) == 11
            isvalid = startswith_36_or_06 and contains_20_30_70 and valid_length
            if not isvalid:         # If it's not a valid address, the user gets this message.
                print("The given '%s' mobile number is not in a valid format!" % mobile_number)
            if not startswith_36_or_06:     # If the number misses 36 or 06, the user gets this message.
                print("Please specify your number and add '36' or '06' at the beginning!")
            if not contains_20_30_70:       # If the number misses the specifying number of the provider,
                print("Please specify your provider: 20/30/70 !")   # the user gets this message.
            if not valid_length:        # If the number is not in a valid length, the user gets this message.
                print("Please enter a mobile number with a valid (11 number) length!")

        return mobile_number

    # NAME
    @staticmethod
    def get_name():
        global Name     # A fügévnyen kívül is lehet használni ezt a változót
        isvalid = False
        while not isvalid:
            Name = input("Enter your full name: ")
            split_Name = Name.split(" ")        # Szétszedi a bekért adatot név részekre

            try:
                isvalid = Name.replace(" ", "").isalpha()\
                          and len(split_Name) > 1   # A név legalább 2 részből áll és csak betűket tartlmazhat
                if not isvalid:
                    raise ValueError

            except ValueError:      # Ha pl számokat adott meg  akkor ezt ki írja és újra lekéri.
                print("Try Again, it is not a name. The name can contain only letters and space! ex.: Angela Smith")

        return Name

    """
    FirstName = split_Name[0]
    LastName = split_Name[1]
    print(FirstName, end=", ")
    print(LastName)
    """

    # GENDER
    @staticmethod
    def get_gender():
        global gender
        entered_data_is_valid = False
        available_genders = ["f", "m"]
        while not entered_data_is_valid:
            gender = input("Enter your sex. For Female pres F, for Male press M: ")
            if gender.lower() in available_genders:
                entered_data_is_valid = True
            else:
                print("Try Again!")

        return gender.lower()

    # SICKNESS
    # Determining whether the donor was sick in the last month.
    @staticmethod
    def get_sickness():
        yes_or_no = ""
        # Asks for an input here first.
        yes_or_no = input("Was the donor sick in the last month? For no press N, for yes press Y: ")
        poss_ans = ["Y", "y", "N", "n"]
        # Keeps asking for the input while it is not in the above list.
        while yes_or_no not in poss_ans:
            yes_or_no = input("Wrong format. Please use Y or N: ")
        # Returns with Y or N.
        return yes_or_no.upper()

    # ID NUMBER
    # Asks the donor's unique identifier and determines whether it suggests a national ID or a passport.
    @staticmethod
    def get_id_number():
        id_number = ""
        # Asks for the ID number here first.
        id_number = input("Please enter the donor's ID number: ")
        # Keeps asking for the input while it is not 8 characters long and only alphanumeric.
        while len(id_number) != 8 or not id_number.isalnum():
            id_number = input("Wrong format. The ID has to be 8 characters long and contain only letters and numbers: ")
        # Decides whether the given string suggests a national ID number or a passport number.
        if id_number[:6].isdigit() and id_number[6:].isalpha():
            print("Your ID number is recorded.")
        elif id_number[:6].isalpha() and id_number[6:].isdigit():
            print("Your passport number is recorded.")
        else:
            # If it does not match any of the two mentioned, it says so too.
            print("The format of your ID number could not be defined, however it was recorded.")
        # Returns with the ID number.
        return id_number

    # LAST DONATION DATE
    # Determines whether the donor's last donation was more than 3 months ago or not.
    @staticmethod
    def get_donation_date():
        # Asks for the last donation date of the donor.
        donation_date = input("Please enter the donor's last donation date in the following format 2000.12.31: ")
        # Keeps asking for the input while the given date does not match the right format.
        while len(donation_date) != 10 or\
                donation_date[4] != "." or\
                donation_date[7] != "." or\
                not donation_date.replace(".", "").isdigit():
            donation_date = input("Wrong format. Please enter the following date form 2000.12.31: ")
        # Converts the given numbers to date format and puts it in variable.
        d_d = datetime.strptime(donation_date, '%Y.%m.%d')
        return d_d

    # BIRTH DATE
    @staticmethod
    def get_date_of_birth():
        global date_of_birth
        is_valid = False
        while not is_valid:
            date = input("Enter your birthday (YYYY.MM.DD)")
            try:
                date_of_birth = datetime.strptime(date, "%Y.%m.%d")
                is_valid = True
            except:
                print("Please enter again a correct date format! (YYYY.MM.DD")
        date_subtract = (datetime.now().date() - date_of_birth.date()).days // 365
        if date_subtract < 18:
            return 0
        else:
            return 1
