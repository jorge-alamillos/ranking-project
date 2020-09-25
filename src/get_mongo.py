from src.server.database import db
import pandas as pd

def import_json(json):
    return pd.read_json(json)

#FUNCTIONS TO CREATE USERS IN MONGO
def create_users(x):
    users1 = list(x.groupby(["user1_login"]).count().reset_index()["user1_login"])
    users2 = list(x.groupby(["user2_login"]).count().reset_index()["user2_login"])
    usersfinal = users1 + users2
    return usersfinal

def git_mongo_users(user_login):
    new_user = {"user_login": user_login}  
    if db.students.find_one(new_user) != None:
         return "User already exists"
    else:
        print("ok import mongo user")
        return db.students.insert_one(new_user)

#FUNCTIONS TO CREATE LABS IN MONGO

def create_labs(x):
    return list(x.groupby(["pull_title"]).count().reset_index()["pull_title"])

def git_mongo_labs(labs):
    new_lab = {"lab_id": labs}  
    if db.labs.find_one(new_lab) != None:
         return "Lab already exists"
    else:
        return db.labs.insert_one(new_lab)

