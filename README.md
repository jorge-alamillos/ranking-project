![ranking](src/images/ranking.png)

#### Project made in Ironhack 08.20 bootcamp
## Objective
There are two main goals for this project. The main objective of this project is the practice in the development of web APIs with ```Flask``` library for Python. The second objective consists of integrating the required data in ```MongoDB``` database.

## Using the program and available commands

Run some of these commands in Terminal as follows. Two types of report are available:
##### - Report by user-defined period of time: Run commands ```-t``` and ```-f```
##### - Report by user-defined model: Run command ```-l```


- ``python3 main.py -h``, ``--help``  show this help message and exit

- ``python3 main.py -m MAIL``,``--mail MAIL``=>  Introduce your mail

- ``python3 main.py  -f DATEFROM``, ``--dateFrom`` DATEFROM => Introduce the starting date for the analysis in format YYYY-MM-DD. Please, note that data is only available from 2010 so the input date must be equal or later

- ``python3 main.py  -t DATETO``, `--dateTo DATETO` => Introduce the ending date for the analysis in format YYYY-MM-DD. Please, note that data is only available until september 2020 so the input date must be equal
  or later
  
- `python3 main.py  -l MODEL`, ``--model MODEL`` => Introduce Iphone model. Available from iPhone 4 (2010) to iPhone SE (2020). Input must be equal to: iphone 4 iPhone 4s iPhone 5 iPhone 5s iPhone 5c iPhone 6 iPhone 6 Plus iPhone 6s iPhone 6s Plus iPhone SE (1ª generación) iPhone 7 iPhone 7 Plus iPhone 8 iPhone 8 Plus iPhone X iPhone XS iPhone XS Max iPhone XR iPhone11 iPhone 11 Pro iPhone 11 Pro Max iPhone SE (2ª generación)


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
	 

## API and main.py Use

#### main.py



## Main sources and references

###### Data source
 - Student names, labs and pull requests in ironhack/datamad0820 repo in GitHub: [link to repo](https://github.com/ironhack-datalabs/datamad0820)
###### Python libraries and programs
- `flask`
- `pymongo`
- `argsparse`
- `MongoDB`
