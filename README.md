![ranking](src/images/ranking.png)

##### Project developed in Ironhack 08.20 Data Analitics bootcamp
## Objective
There are two main goals for this project. The main objective is the practice in the development of web APIs with ```Flask``` library for Python. The second aim consists of integrating the required data in ```MongoDB``` database. 

## Project Structure

- `main.py`: Executable script to download data from GitHub and import into MongoDB. See more info in Program Use.
- `server.py`: Executable script to start Flask server.
-  `__Trash__/`: Jupyter file used for developement testing 
- `src/`:
	1. `get_github.py`: Script used in `main.py` to download data from GitHub
	2. `get_mongo`: Script used in `main.py` to import data into MongoDB
	3. `students.json`: Json file with the data downloaded from GitHub
	4. `server/`: folder containing configuration files for the server and MongoDB
	5. `controllers/`: 
		- `gen_api.py`: Script that executes the endpoints in the API
	 
## Using the program
T



#### Downloading data from GitHub and importing it into MongoDB
 Execute `python3 main.py <-OPTION>` from the terminal including one of the options below:

```bash
main.py -h
usage: main.py [-h] [-s] [-l] [-p] [-hu]

Indicate what you want to import into MongoDB database: users, labs or pulls

optional arguments:
  -h, --help      show this help message and exit
  -hu, --hub      Imports info from github to Json file
  -s, --students  Imports all users from Json file into MongoDB
  -l, --labs      Imports all labs from Json file into MongoDB
  -p, --pulls     Imports all pulls from Json file into MongoDB
```
#### Starting Flask server to run the API
 Execute `python3 server.py` from the terminal. You show obtain a message like this:
```bash
 * Serving Flask app "ranking" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 291-879-593
```
#### Using the API endpoints

Introduce the url in your internet navigator: ´http://localhost:3000/` followed by one of these endpoints:

##### `/student/create/<studentname>` --> Creates an student and saves it into MongoDB
##### `/student/all` --> Lists all students in MongoDB. See example:
```json
{
_id: {
$oid: "5f6c9fc5f40b5e1b5d8a07f4"
},
user_login: "AnaMA96"
},
{
_id: {
$oid: "5f6c9fc5f40b5e1b5d8a07f5"
},
user_login: "CarlosSanzDGP"
},
{
_id: {
$oid: "5f6c9fc5f40b5e1b5d8a07f6"
},
user_login: "Daniel-GarciaGarcia"
},[...]
```

##### `/lab/create/<labname>` --> Creates a lab to be analyzed
##### `/lab/<lab_id>/search` --> Searches statistics on specific lab. See example.
```json
{
-Number of total Pull Requests: 19,
-Number of open Pull Requests: 5,
-Number of closed Pull Requests: 14,
-Percentage of open Pull Requests over the total: 26.32
}
```


##### `/lab/<lab_id>/meme"` --> Gets a random meme joke (extracted from the ones used for each student pull request for that lab. See example.
```json
{
_id: {
$oid: "5f6cefb9cec9d01d6f316119"
},
meme: [
"https://user-images.githubusercontent.com/52798316/93356303-4e639a80-f83f-11ea-8d61-65fe94209815.png"
]
}
]
```

## Main sources and references
###### Data source
 - Student names, labs and pull requests in ironhack/datamad0820 repo in GitHub: [link to repo](https://github.com/ironhack-datalabs/datamad0820)
###### Python libraries and programs
- `flask`
- `pymongo`
- `argsparse`
- `MongoDB`
