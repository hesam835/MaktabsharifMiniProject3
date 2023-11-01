import requests
import json
user="hesam835"
repo="MaktabsharifMiniProject3"
url=f"https://api.github.com/repos/{user}/{repo}/commits"
token="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"
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json',}
response=requests.get(url , headers=headers)
authors_commits= list()
for commit in response.json():
    authors_commits.append({commit["author"]["login"]:commit["commit"]["message"]})
with open("authors_commits","w") as fp:
     json.dump(authors_commits, fp, 
                        indent=4,  
                        separators=(',',': '))

