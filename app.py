import pyrebase


config = {
    "apiKey": "AIzaSyDp85o4iD1gGSxOkZXpj3sNxCcZYmHl_Ss",
    "authDomain": "sprint1-f1e19.firebaseapp.com",
    "projectId": "sprint1-f1e19",
    "databaseURL": "https://sprint1-f1e19.firebaseio.com",
    "storageBucket": "sprint1-f1e19.appspot.com",
    "messagingSenderId": "550815542166",
    "appId": "1:550815542166:web:b6b14b14d409f2d66ccbb7" }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


email = input("Enter Your Email: \n")
password = input("Enter Your Password: \n")

user = auth.create_user_with_email_and_password(email, password)

print("Successfully created an account!")
sign_in = input("Would you like to sign in? [y/n]")

if sign_in == "y":
    print("you have been signed in")
else: print("thank you for signing up!")