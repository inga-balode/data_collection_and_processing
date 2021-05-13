import requests
import json

username = 'octokit'
url = f"https://api.github.com/orgs/{username}/repos"
req = requests.get(url)

data = req.json()
with open('data.json', 'w') as f:
    json.dump(data, f)

for i in range(len(data)):
    print(data[i]['name'])
    i +=1

