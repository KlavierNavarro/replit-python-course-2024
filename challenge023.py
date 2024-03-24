#Challenge 023 - Subroutines: The Recipe for Coding
def login(username, password):
    if username == "klavier" and password == "klavier":
        print("Welcome to Replit!")
        return 1
    else:
        print("Wrong username or password. Try again!")
        return 0
    
success = False

while not success:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    success = login(username, password)