__author__ = 'joti'


from PIL import Image
from os import listdir
from os.path import isfile, join
from io import BytesIO
from operator import itemgetter
import requests
import pytesseract


def freeTheText(input, output):
    colors=7
    im = Image.open(BytesIO(input))
    im = im.convert("P", palette=Image.ADAPTIVE, colors=colors)
    # im.save(output)
    # return

    im2 = Image.new("P",im.size, 255)
    #im2 = im.convert("P",palette=Image.ADAPTIVE, colors=7)

    his = im.histogram()


    values={}
    for i in range(colors):
        values[i] = his[i]

    sort_hist={}
    for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
        sort_hist[j]=k

    tmp={}
    for x in range(10):
        for y in range(im.size[1]):
            pix = im.getpixel((y,x))
            if pix in tmp:
                tmp[pix]+=1
            else:
                tmp[pix]=1
    #print(sort_hist)
    sort_hist[sorted(tmp.items(), key=itemgetter(1), reverse=True)[0][0]]=0

    tmp={}
    for x1 in range(im.size[0]-10, im.size[0]):
        for y1 in range(im.size[1]):
            pix = im.getpixel((x1,y1))
            if pix in tmp:
                tmp[pix]+=1
            else:
                tmp[pix]=1


    #print(sort_hist)
    sort_hist[sorted(tmp.items(), key=itemgetter(1), reverse=True)[0][0]]=0

    sort_hist[0]=0
    #print(sort_hist)
    font_colors=[]

    font_colors.append(sorted(sort_hist.items(), key=itemgetter(1), reverse=True)[0][0])



    # print(tmp)
    temp = {}
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y, x))
            temp[pix] = pix
            #if pix in font_colors:
            if pix ==0 :
                 im2.putpixel((y, x), 0)
            #im2.putpixel((y,x),pix)


   # im2.save(output)
    return  im2

def initialiseSession(url):
    proxie={"http":"http://localhost:8080"}
    s = requests.Session()
    s.get(url)
    return s

def getCaptcha(s,url):
    req=requests.Request("GET", url, cookies=s.cookies.get_dict())
    r = req.prepare()
    return s.send(r)._content

def submitCaptcha(s, url, solution):
    proxie={"http":"http://localhost:8080"}

    post_data = {"submit":"Send", "captcha":solution}
    req=requests.Request("POST", url, data=post_data, cookies=s.cookies.get_dict())
    r = req.prepare()
    response = str(s.send(r, proxies=proxie)._content)
    substring = response[response.find("/form>")+6:response.find("</body>")]
    number=""
    for i in range(len(substring)):
        tmp=""
        try:
            tmp=int(substring[i])
            number+=str(tmp)
        except:
            pass

        if substring[i]== "/":
            return int(number)

    return 0

'''
========================================================
Now the function calls ...
========================================================
'''


path="/home/joti/Dokumente/hacking/hDa_CTF/defcamp/misc_400/captcha/"
outpath="/home/joti/Dokumente/hacking/hDa_CTF/defcamp/misc_400/free_captcha/"
url="http://10.13.37.10/"
captcha_url=url+"captcha.php"

session = initialiseSession(url)
solved=0
i=0
max = 0
y=0
while(solved < 1337):
    captcha = getCaptcha(session, captcha_url)
    image = freeTheText(captcha, join(outpath,"test.png"))
    solution=pytesseract.image_to_string(image, lang="def", config="-psm 8")
    if len(solution)==6 and not " " in solution and not "1" in solution and not "7" in solution and not "M"in solution and not "S" in solution and not "P" in solution\
            and not "F" in solution and not "9" in solution and not "J" in solution and not "0" in solution:
        y+=1
        solved = submitCaptcha(session, url, solution)
        if solved > max:
            max = solved

        if solved == 0 and i < 500:
            image.save(join(outpath,"captcha_"+solution+"_"+str(i)+".png"))
            i+=1

        print(str((i/y)*100)+"%",solved, max)





# onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
#
# for f in onlyfiles:
#    freeTheText(join(path,f),join(outpath,f))
