## Importing Pyrebase to use firebase authentication
import pyrebase

## Connecting to the Firebase project with credentials
config = {
    "apiKey": "AIzaSyDp85o4iD1gGSxOkZXpj3sNxCcZYmHl_Ss",
    "authDomain": "sprint1-f1e19.firebaseapp.com",
    "projectId": "sprint1-f1e19",
    "databaseURL": "https://sprint1-f1e19.firebaseio.com",
    "storageBucket": "sprint1-f1e19.appspot.com",
    "messagingSenderId": "550815542166",
    "appId": "1:550815542166:web:b6b14b14d409f2d66ccbb7" }

## Creating the log-in and new account page
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

## Creating a function to get email and password 
def get_credentials():
    email = input("Enter Your Email: \n")
    password = input("Enter Your Password: \n")
    return {email, password}

## Welcome statement
print("Hello, welcome to the course history database.")
new_or_not = input("Would you like to sign in or create a new account? [sign_in/create_new]\n")

## Either sign up for a new account or sign into an existing account

if new_or_not == "sign_in":
    # creds = get_credentials()
    # print(creds)
    email = input("Enter Your Email: \n")
    password = input("Enter Your Password: \n")
    user_key = auth.sign_in_with_email_and_password(email, password)
    print(user_key)

elif new_or_not == "create_new":
    # creds = get_credentials()
    email = input("Enter Your Email: \n")
    password = input("Enter Your Password: \n")
    user = auth.create_user_with_email_and_password(email, password)
    print("Successfully created an account!")

else: print("Invalid input, please try again")

## thank the user for signing up

sign_in = input("Would you like to sign in? [y/n]")

if sign_in == "y":
    print("You have been signed in")
if new_or_not == "create_new":
    print("Thank you for signing up!")