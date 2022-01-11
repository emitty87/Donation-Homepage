from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
database = {"admin": "password123"}
donations = ["donation"]
authorized_user = ""


show_homepage()
if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print(f"Logged in as: {authorized_user}")

while True:
    user_option = int(input("Choose an option: "))
    if user_option == 1:
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)

    elif user_option == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
        show_homepage()
    elif user_option == 3:
        if authorized_user == "":
            print("You are not logged in.\n\n")
        else:
            donation = donate(authorized_user)
            print(str(donation))
            donations.append(donation)
        show_homepage()
    elif user_option == 4:
        show_donations(donations)
        show_homepage()
    elif user_option == 5:
        print("Leaving DonateMe...")
        break
