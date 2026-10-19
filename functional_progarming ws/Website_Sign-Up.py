
def Sign_up_Form_Validation(username, email, password):
    if len(username) > 3 and len(password) >= 8 and "@" in email and any(i.isdigit() for i in password):
        print("Your entered data is correct")
    else:
        print("Pls re try with diff username, password and email")


username = input("Enter your Username: ")
password = input("Enter your password: ")
email = input("Enter your email: ")

Sign_up_Form_Validation(username, email, password)
