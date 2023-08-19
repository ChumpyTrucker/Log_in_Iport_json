import json

# Function to load user data from a JSON file.
def load_user_data():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save user data to a JSON file.
def save_user_data(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

# Function to register a new user
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    users = load_user_data()

    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[username] = password
        save_user_data(users)
        print("Registration successful!")

# Function to log in a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    users = load_user_data()

    if username in users and users[username] == password:
        print("Login successful!")
        # Call your app's main function or perform additional actions
    else:
        print("Invalid username or password. Please try again.")

# Main function
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to start the program
main()
