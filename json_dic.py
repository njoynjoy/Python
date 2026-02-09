import requests

pull_details = requests.get("https://api.github.com/repos/njoynjoy/first/pulls")


#print (pull_details.json())

for pull in pull_details.json():
    print(f"pull request title: {pull['title']}, id: {pull['id']}, user: {pull['user']['login']}")


    #NJOY#
