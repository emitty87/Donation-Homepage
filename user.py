def login(database, username, password):
    if username in database.keys() and password in database.values():
        print(f"Welcome back, {username}!")
        return username
    elif username == database.keys() and password != database.values():
        print("Invalid Credentials\n")
        return ""
    else:
        print("User not found. Please try again or Register to continue.\n")
        return ""


def register(database, username):
    if username in database.keys():
        print("Username already registered.\n")
        return ""
    else:
        print(f"\nUsername has been registered.\n")
        return username
