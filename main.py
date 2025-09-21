username="admin"
password_length=12
if username=="admin" and password_length>=10:
    print("Login succesfull")
    if password_length<=10:
        print("Admin password Inccorect")
if username == "user" and password_length>=6:
    print("Login succsesfull")
else:
    print("User password must be 6+")
