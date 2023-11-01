import requests
import json
user="hesam835"
repo="MaktabsharifMiniProject3"
url=f"https://api.github.com/repos/{user}/{repo}/commits"
token="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"
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json',}
response=requests.get(url , headers=headers)
if response.status_code == 200:
    try:
        authors_commits= list()
        for commit in response.json():
            authors_commits.append({commit["author"]["login"]:commit["commit"]["message"]})
        with open("authors_commits.json","w") as fp:
            json.dump(authors_commits, fp, 
                                indent=4,  
                                separators=(',',': '))
    except Exception as e:
        print(e)
else:
    print("Request Error")