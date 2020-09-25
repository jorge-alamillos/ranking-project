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
import src.get_mongo as gm
import src.get_github as gh
import os
import sys
import argparse
import pandas as pd
import json

def parse():
    parser = argparse.ArgumentParser(description="Indicate what you want to import users, labs or pulls")
    
    parser.add_argument("-s", "--students",
                        dest='stdnts',
                        action= 'store_true',
                        help="Imports all users from Json file")
    parser.add_argument("-l","--labs",
                        dest="lbs",
                        action= 'store_true',
                        help="Imports all labs from Json file")
    parser.add_argument("-p","--pulls",
                        dest="plls",
                        action= 'store_true',
                        help="Imports all pulls from Json file")
    
    parser.add_argument("-hu","--hub",
                        dest='hb',
                        action= 'store_true',
                        help="Imports info from github to Json file")
        
    args = parser.parse_args()                                                              
    return args

def main():

    args = parse()
    stdnts = args.stdnts
    lbs = args.lbs
    plls = args.plls
    hb = args.hb
    print(args)

    #import users to mongo
    if stdnts is True:
        imprt = gm.import_json("src/students.json")
        users = gm.create_users(imprt)
        print(users)
        for user in users:
            gm.git_mongo_users(user)    
  
    #import labs to mongo     
    if lbs is True:
        labs = gm.create_labs(imprt)
        for lab in labs:
            gm.git_mongo_labs(lab) 
        print("new students and labs created")

    #import pulls to mongo
    if plls is True:
        os.system("mongoimport -d ranking_project -c pulls --jsonArray src/students.json") 
    
    #creates json file from github
    if hb is True:
        x = gh.gen_url()    
        y = gh.get_pulls(x)
        gh.get_users(y)
        with open("src/students.json",'w') as json_file:
            return json.dump(y,json_file) 

    

if __name__ == "__main__": 
    main()