import requests
import os
from dotenv import load_dotenv
import re
from bs4 import BeautifulSoup
import requests
import json

#GETS THE LINKS TO PULL REQUESTS
def gen_url():
    urls = []
    load_dotenv()
    base_url = "https://api.github.com"
    owner = "ironhack-datalabs"
    repo = "datamad0820"
    endpoint = f"/repos/{owner}/{repo}/pulls"
    query = "?per_page=100&state=all"
    for i in range(1,8):
        urls.append(f"{base_url}{endpoint}{query}&page={i}")
    return urls

#EXECUTE THE API
def get_pulls(urls):
    authkey = os.getenv("AUTHKEY")
    headers = {"Authorization": f"Bearer {authkey}"}
    jsons = []
    slct = []
    for url in urls:
        jsons.append(requests.get(url,headers=headers).json())
    for page in jsons:
        for pull in page:
            if pull["state"] == "closed":
                slct.append({"pull_id":pull["id"],
                             "pull_url":pull["html_url"],
                             "pull_nbr":pull["number"],
                             "pull_title":pull["title"].split()[0][1:-1],
                             "name_participants":pull["title"].split()[1:],
                             "creation_date":pull["created_at"][:10],
                             "closing_date":pull["closed_at"][:10],
                             "pull_state":pull["state"][:10]})

            else:
                slct.append({"pull_id":pull["id"],
                             "pull_url":pull["html_url"],
                             "pull_nbr":pull["number"],
                             "pull_title":pull["title"].split()[0][1:-1],
                             "name_participants":pull["title"].split()[1],
                             "creation_date":pull["created_at"],
                             "closing_date": False,
                             "pull_state":pull["state"][:10]})
    return slct
                                      



#WEBSCRAPING PULL REQUESTS TO GET USERS AND MEME
def get_users(pulls):
    for pull in pulls:
        authors = []
        res = requests.get(pull["pull_url"])
        soup = BeautifulSoup(res.text,'html.parser')
        auth = soup.select("a.author[href]")
        for r in auth:
            authors.append(r.text)
        authors = set(authors)
        pull["user_login"] = list(authors)
        if pull["pull_state"] == "closed":        
              pull["meme"] = re.findall(r'src.*\s',str(soup.select("p > a > img[src]")))
        
