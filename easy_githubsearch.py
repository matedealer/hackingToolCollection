import json, requests
import os
from time import sleep

oouth_token="<oouth_token>"
repo_list=[]
found_dir = "./founds/"

def getJSONfromURL(url):
    response = requests.get(url)
    return json.loads(response.text)



def getNextPage(list, url, page):
    free = getJSONfromURL("https://api.github.com/rate_limit?access_token="+oouth_token)["resources"]["search"]["remaining"]
    if(free>0):
        print(free)
    else:
        sleep(5)
    data = getJSONfromURL(url+"&page="+str(page))
    if "items" in data.keys():
        for repo in data["items"]:
            list.append({"name":repo["full_name"],"html_url":repo["html_url"], "stars":repo["stargazers_count"]})

    return list


if __name__ == "__main__":
    savefile="php_repo_file"



    url = "https://api.github.com/search/repositories?q=stars:>=50+language:PHP+pushed:>=2015-01-15&sort=stars&order=asc&per_page=1000&access_token="+oouth_token
    data = getJSONfromURL(url)
    total_count = data["total_count"]
    repo_list=[]
    page=0
    while(len(repo_list) < 1000):
        page+=1
        print(total_count,len(repo_list),page)
        repo_list=getNextPage(repo_list,url,page)


    print(len(repo_list), len(data["items"]))

    file = open(savefile,"w+")
    file.write(json.dumps(repo_list))
