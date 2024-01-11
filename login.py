# User credentials (replace these with your own credentials)
valid_username = "user123"
valid_password = "pass123"

def login():
    print("Welcome to the Login Page")

    # Get user input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if credentials are valid
    if username == valid_username and password == valid_password:
        print("Login successful! Welcome, " + username + "!")
    else:
        print("Invalid credentials. Please try again.")

# Call the login function
login()
