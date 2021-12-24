
# a a script to clear the db
# step 7 - Let's do a useful search

print("Demonstration python based mongodb access");


import pymongo              # for mongodb access
import pprint               # for pretty printing db data

#Let's get the user object from the db

# Establish connection
client = pymongo.MongoClient("mongodb+srv://Test:Password1@cluster0.bg843.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


# Create a database
db = client.classDB

db.githubuser.delete_many({});
