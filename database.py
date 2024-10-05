
## Importing firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

## Accessing private key to read/write to the database
cred = credentials.Certificate(r"C:\Users\andre\projects\Firestore1key\privatekey1.json")
firebase_admin.initialize_app(cred)

## Creating the database object
db = firestore.client()

## Reference a collection
fall21 = db.collection('Fall21')
winter22 = db.collection('Winter22')

## Creating an Array of all the tables/collections to
## do queries on the whole data set
all_tables = ['Fall21', 'Winter22']

            ### QUERIES ###
## Going through each collection in the DB and getting the documents into
## dictionaries so that queries can be run and print the information to the screen
# for table_name in all_tables:
#     items = db.collection(table_name).get()
#     for item in items:
#         item_dic = item.to_dict()
#         ## making a print statement to see classes over 2 credits and their grades
#         if item_dic['Credits'] > 2 :
#             print(f'{item.id} was a big class, it was {item_dic['Credits']} credits')
#             print(f'You got a {item_dic['Grade']} in the class\n')


## Simple query: Get all items in the collection
# items = fall21.get()
# for item in items:
#     item_dic = item.to_dict()
#     print(item_dic['Grade'])
#     if item_dic['Grade'] != 'A' :
#         print(f'It looks like you need to work on {item_dic['Name']}!')
#     else: print('Great Job, keep up the good work!')

## Using the .where to specify a query
# good_grades = fall21.where('Grade', '==', "A").get()
# print(good_grades)
# for item in good_grades:
#     good_grades_dic = item.to_dict()
#     print(good_grades_dic)


            ### ADD/CREATE OR UPDATE ITEMS ###

## Data that will be added/updated to the database
# data = {
#     'Grade' : '',
#     'Credits' : '',
#     'Name' : ''
# }

## Creating the table 
# db.collection('Semester name').document('Course code').set('data')


            ### DELETING ITEMS ###
            
# db.collection('Semester name').document('Course code').delete()
