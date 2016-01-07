'''
Created on Jun 1, 2015

@author: mft
'''
import json, requests
from time import sleep
import os

oouth_token="you wish...."
repo_list=[]
found_dir = "./founds/"
export_list=[]


def getJSONfromURL(url):
    response = requests.get(url)
    return json.loads(response.text)

def getStarsFromURL(url):
    data = getJSONfromURL(url)
    return data["stargazers_count"]


def checkLimit():
    free = getJSONfromURL("https://api.github.com/rate_limit?access_token="+oouth_token)["resources"]["search"]["remaining"]
    if(free==0):
        sleep(2)
        checkLimit()

def searchmultiple(thestr, substr):
    curindex = 0
    resultlist = []

    while curindex < len(thestr):
        curindex = thestr.find(substr, curindex+1)
        if curindex == -1:
            break
        else:
            resultlist.append(curindex)

    return resultlist



def searchRepo(reponame, searchword):

    checkLimit()

    url = "https://api.github.com/search/code?q="+ searchword +"+in:file+repo:"+reponame+"&access_token="+oouth_token
    # ab hier im repo
    data = getJSONfromURL(url)

    if "items" not in data.keys() or data["total_count"] == 0:
        if "items" not in data.keys():
            print(data)
        return
    export_list.append(reponame)
    print("\n\n\n=================================================================\n" + reponame + "\n")
    for item in data["items"]:
        print("============")
        print(item["path"])
        print(item["html_url"])
        print("============")


        data=getJSONfromURL(item["url"])
        if "download_url" in data.keys():
        #     save_path = os.path.join(found_dir, reponame)
        #     try:
        #         os.stat(save_path)
        #     except:
        #         os.makedirs(save_path)
        #
             cursourcefile = requests.get(data["download_url"]).text
             #file_found = open(os.path.join(save_path, item["name"]),"w+")
             #print json.dumps(data, sort_keys=True, indent=4,separators=(',', ': '))
        #
             foundindices = searchmultiple(cursourcefile, searchword)
             # printe das noch schoen
             startpos = 0
             endpos = 0
             width = 200
             for index in foundindices:
                 print("")
                 if index <= 100:
                     startpos = 0
                 else:
                     startpos = index - width

                 if index >= len(cursourcefile)-100:
                     endpos = len(cursourcefile)-1
                 else:
                     endpos = index + width

                 print(cursourcefile[startpos:endpos])
                 print("[...]")

        print("\n\n")


#=== START HERE =====================
if __name__ == "__main__":
    import_file="php_repo_file"
    export_file="php_sql_repos"


    if not os.path.isfile(import_file):
        exit()
    else:
        file = open(import_file, "r")
        text = file.read()

        if text is None or text =="":
            repo_list=[]
        else:
            repo_list=[element["name"] for element in json.loads(text)]




        for repo in repo_list:
            #print json.dumps(repo, sort_keys=True, indent=4, separators=(',',': '))
            searchword = "mysql"
            searchRepo(repo, searchword)



    file = open(export_file,"w")
    file.write(json.dumps(export_list))




# hier gibt man einfach das repository fullname    print(data["total_count"])  und den searchstring an
#searchRepo("markwatkinson/luminous", "eval")




