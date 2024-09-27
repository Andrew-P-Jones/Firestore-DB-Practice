
## Importing frirebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

## Accessing private key to read/write to the database
cred = credentials.Certificate(r"C:\Users\andre\projects\Firestore1key\privatekey1.json")
firebase_admin.initialize_app(cred)

## Creating the database object
db = firestore.client()

## Data that will be added to the database
data = {
    'Column3' : 'Entry 3',
    'Column4' : 'Entry 4'
}

## Choosing/Creating the table 
doc_ref = db.collection('FirstDB').document()

## Adding the items from the data variable into the collection
doc_ref.set(data)


print(f'It worked!')