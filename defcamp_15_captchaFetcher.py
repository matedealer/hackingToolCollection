__author__ = 'joti'


import requests

url="http://10.13.37.10/captcha.php"
path = "/home/joti/Dokumente/hacking/hDa_CTF/defcamp/misc_400/captcha/"
image_count = 3000

for i in range(image_count):
    file = open(path+"captcha_"+str(i)+".png","wb")
    file.write(requests.get(url)._content)
    file.close()
