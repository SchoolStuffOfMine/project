from donation import *
from donor import *
print("Welcome to the Blood Bank!")
def menu():
    print("""
    Press 1 to register donor
    Press 2 to view donor
    Press 3 to delete donor
    Press 4 to register donation
    Press 5 to view donation log
    Press 6 to view statistics
    Press 999 to display menu again
    Press 1000 to exit
    """)
menu()
while True:
    while True:
        try:
            opt = int(input("Please enter your choice [999 for menu]: "))
            break
        except:
            print("Invalid option! \n Please try again")
    if opt == 1:
        RegisterDonor()
    elif opt == 2:
        ViewDonor()
    elif opt == 3:
        KillDonor()
    elif opt == 4:
        RegisterDonation()
    elif opt == 5:
        ViewDonation()
    elif opt == 6:
        DonationStats()
    elif opt == 999:
        menu()
    elif opt == 1000:
        break
    else:
        print("Invalid option!")
print("Thank You for using the program! \n Have a good day!")



