def show_homepage():

    print("      ===  DonateMe Homepage ===       ")
    print("---------------------------------------")
    print("| 1.   Login     | 2.   Register      |")
    print("---------------------------------------")
    print("| 3.   Donate    | 4.  Show Donations |")
    print("---------------------------------------")
    print("|             5. Exit                 |")
    print("---------------------------------------")


username = ""
password = ""


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_amt = float(donation_amt)
    donation = str(f"{username} donated: ${donation_amt}")
    print("Thank You!\n")
    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        print(donations)
