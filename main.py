#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Donor import DonorData
from Event import EventData
from datetime import datetime

# Welcomes to the program and starts an option.
print("Welcome to the blood donation program.\n")
d_e_s = ""
d_e_s_list = ["D", "E", "S", "d", "e", "s"]
# Keeps asking the user which program option to run till one of the above listed letters is chosen.
while d_e_s not in d_e_s_list:
    d_e_s = input("To start a Donor registration press D; \
                    \nTo start an Event registration press E; \
                    \nTo Stop the program press S: ")

# DONOR REGISTRATION
# In case D is entered, calls all the Donor definitions.
if d_e_s.upper() == "D":
    DonorData.get_name()
    DonorData.get_gender()
    # If the returned number from the def is not greater than 50, the program stops.
    if DonorData.get_weight() <= 50:
        print("\nDonors are only accepted above 50 kgs.")
        print("The program has ended because of not suitable donor.")
        exit()
    # If the returned date from the def is within 18 years of the current date, the program stops.
    if DonorData.get_date_of_birth() == 0:
        print("\nDonors are only accepted above 18 years.")
        print("The program has ended because of not suitable donor.")
        exit()
    # If the returned date from the def is within 90 days of the current date, the program stops.
    if (datetime.now() - DonorData.get_donation_date()).days <= 90:
        print("\nDonors can only give blood once in every 3 months.")
        print("The program has ended because of not suitable donor.")
        exit()
    DonorData.get_sickness()
    DonorData.get_id_number()
    DonorData.get_exp_date()
    DonorData.get_blood_type()
    DonorData.get_email_address()
    DonorData.get_mobile_number()
    print("The donor's data is recorded.")

# EVENT REGISTRATION
# In case E is entered, calls all the Event definitions.
elif d_e_s.upper() == "E":
    EventData.get_event_date()
    EventData.get_donation_start()
    EventData.get_donation_end()
    EventData.get_zip_code()
    EventData.get_city()
    EventData.get_address()
    EventData.get_available_beds()
    EventData.get_max_donor_number()
    EventData.get_planned_donor_number()
    EventData.success_rate()

# In case S is entered, the program stops.
elif d_e_s.upper() == "S":
    print("The program ended normally.")
    exit()
