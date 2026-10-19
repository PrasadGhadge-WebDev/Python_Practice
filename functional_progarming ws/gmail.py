

def login_Check(username, password):

    if username == "admin" and password == "admin123":

        print("Login Successful....")
    else:

        print("Invalid Password....")

username = input("Enter Username: ")

password = input("Enter Password: ")

login_Check(username, password)