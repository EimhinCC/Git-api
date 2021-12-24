
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
    n=1
    f.write('User,RepoCount\n')
    dct = db.githubuser.find({'user': {'$exists': True}})
    for user in dct:
        pprint.pprint(user)
        print()
        f.write(str(n) + ',' + str(user['public_repos']) + '\n')
        n+=1
        
with open('data2.csv', 'w') as f:
    n=1
    f.write('group, Watchers, MaxStars, followers\n')
    dct = db.githubuser.find({'user': {'$exists': True}})
    for user in dct:
        pprint.pprint(user)
        print()
        f.write(str(n) + ',' + str(user['total_watchers']) + ',' + str(user['MaxStars'])+ ',' + str(user['followers']) + '\n')
        n+=1
        
with open('data3.csv', 'w') as f:
    f.write('Watchers,Forks\n')
    dct = db.githubuser.find({'user': {'$exists': True}})
    for user in dct:
        pprint.pprint(user)
        print()
        f.write(str(user['total_watchers']) + ',' + str(user['forks']) + '\n')

