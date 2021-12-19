
# a script to do python based access to the mongodb
# step 6 - Let's do a useful search

print("Demonstration python based mongodb access");


import pymongo              # for mongodb access
import pprint               # for pretty printing db data
4
#Let's get the user object from the db

# Establish connection

client = pymongo.MongoClient("mongodb+srv://Test:Password1@cluster0.bg843.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


with open('data.csv', 'w') as f:
    f.write('User,RepoCount\n')
    dct = db.githubuser.find({'user': {'$exists': True}})
    for user in dct:
        pprint.pprint(user)
        print()
        f.write(user['user'] + ',' + str(user['public_repos']) + '\n')
        
with open('data2.csv', 'w') as f:
    f.write('group, Watchers, LinesPerFork, AvrSize\n')
    dct = db.githubuser.find({'user': {'$exists': True}})
    for user in dct:
        pprint.pprint(user)
        print()
        f.write(user['user'] + ',' + str(user['total_watchers']) + ',' + str(user['linesPerFork'])+ ',' + str(user['avrSize']) + '\n')

