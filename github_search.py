'''
Created on Jun 1, 2015

@author: mft
'''
import json, requests
import time
import os

oouth_token="e7ecc0fc0b6906a47cd91cda15d61faa58ce3496"
repo_list=[]
found_dir = "./founds/"

def getJSONfromURL(url):
    response = requests.get(url)
    return json.loads(response.text)

def getStarsFromURL(url):
    data = getJSONfromURL(url)
    return data["stargazers_count"]

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
    if reponame in repo_list:
        return

    url = "https://api.github.com/search/code?q="+ searchword +"+in:file+repo:"+reponame+"&access_token="+oouth_token
    # ab hier im repo
    data = getJSONfromURL(url)
    repo_list.append(reponame)

    if "items" not in data.keys() or data["total_count"] == 0:
        if "items" not in data.keys():
            print(data)
        return

    print("\n\n\n=================================================================\n" + reponame + "\n")
    for item in data["items"]:
        print("============")
        print(item["path"])
        print(item["html_url"])
        print("============")
        #print json.dumps(item, sort_keys=True, indent=4,separators=(',', ': '))
        # data=getJSONfromURL(item["url"])
        # if "download_url" in data.keys():
        #     save_path = os.path.join(found_dir, reponame)
        #     try:
        #         os.stat(save_path)
        #     except:
        #         os.makedirs(save_path)
        #
        #     cursourcefile = requests.get(data["download_url"]).text
        #     file_found = open(os.path.join(save_path, item["name"]),"w+")
        #    #print json.dumps(data, sort_keys=True, indent=4,separators=(',', ': '))
        #
        #     foundindices = searchmultiple(cursourcefile, searchword)
        #     # printe das noch schoen
        #     startpos = 0
        #     endpos = 0
        #     width = 200
        #     for index in foundindices:
        #         print("")
        #         if index <= 100:
        #             startpos = 0
        #         else:
        #             startpos = index - width
        #
        #         if index >= len(cursourcefile)-100:
        #             endpos = len(cursourcefile)-1
        #         else:
        #             endpos = index + width
        #
        #         print(cursourcefile[startpos:endpos])
        #         print("[...]")

        #else:
        #    break
        print("\n\n")


#=== START HERE =====================
if __name__ == "__main__":
    savefile="foo_file"

    if not os.path.isfile(savefile):
        file =open(savefile, "w+")
    else:
        file = open(savefile, "r")
        text = file.read()

        if text is None or text =="":
            repo_list=[]
        else:
            repo_list=json.loads(text)



    url = "https://api.github.com/search/repositories?q=stars:>50+language:PHP+pushed:>=2015-01-15&sort=stars&order=asc&access_token="+oouth_token

    data = getJSONfromURL(url)
    count=0
    if "items" in data.keys():
        for repo in data["items"]:
            count+=1
            if repo not in repo_list:
                print(repo["html_url"])
                #print json.dumps(repo, sort_keys=True, indent=4, separators=(',',': '))
                curreponame = repo["full_name"]
                searchword = "sql"
                searchRepo(curreponame, searchword)


    print(count)

    file = open(savefile,"w")
    file.write(json.dumps(repo_list))




# hier gibt man einfach das repository fullname    print(data["total_count"])  und den searchstring an
#searchRepo("markwatkinson/luminous", "eval")




