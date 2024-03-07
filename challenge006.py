#Challenge 006 - Make your own login program
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "user" and password == "pass":
  print(f"Welcome to the system, {username}!")
elif username == "admin" and password == "admin":
    print(f"Access granted for {username}")
elif username == "guest":
  if password:
    print("Access denied")
  else:
    print(f"Welcome, {username}")
else:
  print("Access denied")