

"""
ooooooooo.         .o.       ooooo      ooo oooo    oooo ooooo ooooo      ooo   .oooooo.        ooooooooo.   ooooooooo.     .oooooo.      oooo oooooooooooo   .oooooo.   ooooooooooooo 
`888   `Y88.      .888.      `888b.     `8' `888   .8P'  `888' `888b.     `8'  d8P'  `Y8b       `888   `Y88. `888   `Y88.  d8P'  `Y8b     `888 `888'     `8  d8P'  `Y8b  8'   888   `8 
 888   .d88'     .8"888.      8 `88b.    8   888  d8'     888   8 `88b.    8  888                888   .d88'  888   .d88' 888      888     888  888         888               888      
 888ooo88P'     .8' `888.     8   `88b.  8   88888[       888   8   `88b.  8  888                888ooo88P'   888ooo88P'  888      888     888  888oooo8    888               888      
 888`88b.      .88ooo8888.    8     `88b.8   888`88b.     888   8     `88b.8  888     ooooo      888          888`88b.    888      888     888  888    "    888               888      
 888  `88b.   .8'     `888.   8       `888   888  `88b.   888   8       `888  `88.    .88'       888          888  `88b.  `88b    d88'     888  888       o `88b    ooo       888      
o888o  o888o o88o     o8888o o8o        `8  o888o  o888o o888o o8o        `8   `Y8bood8P'       o888o        o888o  o888o  `Y8bood8P'  .o. 88P o888ooooood8  `Y8bood8P'      o888o     
                                                                                                                                       `Y888P                                          
"""

from src.server.app import app
from flask import request, Response
from src.server.json_response import asJsonResponse
import re
from src.server.database import db
from bson.json_util import dumps
import re


@app.route('/') 
def welcome():
     return {                                                                                                                                
        "1.status": "OK",
        "2.message": "Welcome to range-api",
        "3.Available endpoints": "" ,
        "A.--> /student/create/<studentname>.": "Creates a student and save into DB",
        "B.--> /student/all": "Lists all students in database",
        "C.--> /lab/create/<labname>": "Creates a lab to be analyzed",
        "D.--> /lab/<lab_id>/search": "Search student submissions on specific lab",
        "E.--> /lab/<lab_id>/meme": "Get a random meme (extracted from the ones used for each student pull request for that lab"
    }

#STUDENT ENDPOINTS
@app.route("/student/create/<studentname>")
@asJsonResponse
def create_student(studentname):
    '''
    Purpose: Create a student and save into DB
    Params: studentname the student name
    Returns: student_id
    '''
    new_student = {"username": studentname}

    if db.students.find_one(new_student) != None:
        return "Student already exists" 
    else:
        db.students.insert_one(new_student)
        return f"User {studentname} created"


@app.route("/student/all")
def findall_stdnts():
    '''
    Purpose: List all students in database
    Returns: An array of student objects
    '''
    foundStudent = db.students.find({"user_login":{"$exists":True}})
    return dumps(list(foundStudent))


#LAB ENDPOINTS

@app.route("/lab/create/<labname>")
def create_lab(labname):
    '''
    Purpose: Create a lab to be analyzed.
    Params: The lab-prefix to be analyzed. Example: [lab-scavengers]
    Returns: lab_id
    '''
    new_lab = {"lab_name": labname}  
    if db.labs.find_one(new_lab) != None:
        return "Lab already exists" 
    else:
        db.labs.insert_one(new_lab)
        return f"Lab {labname} created"


@app.route("/lab/<lab_id>/search")
def get_lab(lab_id):
    '''
    Purpose: Search student submissions on specific lab
    Params: user_id
    Returns: See Lab analysis section
    '''
 
    total_pulls = db.pulls.find({"pull_title":lab_id},{"pull_title":1}).count()
    open_pulls = db.pulls.find({"$and":[{"pull_title":lab_id},{"pull_state": "open"}]}).count()
    closed_pulls = db.pulls.find({"$and":[{"pull_title":lab_id},{"pull_state": "closed"}]}).count()
    perc_open = round((open_pulls/total_pulls)*100,2)
    

    #foundStudent = db.students.find({{"user_login":{"$exists":True}},{"user_login":1}})

    #pullStudent = db.pulls.find({"pull_title":lab_id},{"pull_title":1})
    

    result={'-Number of total Pull Requests': total_pulls,'-Number of open Pull Requests': open_pulls,
     '-Number of closed Pull Requests': closed_pulls, '-Percentage of open Pull Requests over the total': perc_open
     }
  
    return dumps(result)


"""
@app.route("/lab/memeranking")
def all_stdnts():
    '''
    Purpose: Ranking of the most used memes for datamad0820 divided by labs
    '''
 
"""

@app.route("/lab/<lab_id>/meme")
def random_meme(lab_id):
    '''
    Purpose: Get a random meme (extracted from the ones used for each student pull request for that lab
    '''
    meme_projections = {"meme":1}
    random_meme = list(db.pulls.aggregate([{"$match": {"$and": [{"pull_title": lab_id}, 
    {"pull_state":"closed"}]}}, {"$sample": {"size": 1}}, {"$project": meme_projections}]))

    return dumps(f"Chosen meme from {lab_id} is {random_meme}")   