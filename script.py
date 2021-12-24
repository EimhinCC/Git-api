
# a script to do python based access to the github api
# step 4 - Let's store our data in a mongodb
# remember to pip install pymongo

print("Demonstration python based github api access");


from github import Github   # github api access
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access

from dotenv import load_dotenv
load_dotenv()

import os

#we initialise a PyGithub Github object with our access token.
#     note that this token is ours, and now deleted. You must 
#     crete your own access token and use here instead. 
tk = os.getenv('GITHUB')
g = Github(tk)

#Let's get the user object and build a data dictionary
usr = g.get_user("jonathanong")
repos = usr.get_repos()

forks = 0
watcherCount = 0
size = 0
reposWithForks =0
MaxStars =0
for repo in repos:
    watcherCount = watcherCount + repo.watchers_count;
    if MaxStars < repo.stargazers_count:
          MaxStars = repo.stargazers_count
    if repo.fork is True:
        reposWithForks += 1
    forks = forks +(repo.forks_count)
    size = size + repo.size

dct = {
        'user': usr.login,
        'public_repos': usr.public_repos,
        'followers': usr.followers,
        'total_watchers' : watcherCount,
        'forks' : forks,
        'reposWithForks' : reposWithForks,
        'MaxStars' : MaxStars

      }

print ("dictionary is " + json.dumps(dct))

# now let's store the dictionary in a mongodb

# first we need to remove null fields from the dictionary, because
# if we don't we'll end up with null fields in the db. This will cause us
# lots of debugging problems later. The convention is only store actual data
# in the database.

for k, v in dict(dct).items():
    if v is None:
        del dct[k]

print ("cleaned dictionary is " + json.dumps(dct))

# now let's store the data.

# Establish connection

client = pymongo.MongoClient("mongodb+srv://Test:Password1@cluster0.bg843.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


db.githubuser.insert_many([dct])
