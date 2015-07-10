#!/usr/bin/python

import subprocess, sys
import itertools
import hashlib


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(7, maxlength + 1)))



filename = sys.argv[1]
if(len(sys.argv)>2):
    print(filename)
    print(sys.argv[2])
    for x  in range(2,len(sys.argv)):
        print(sys.argv[x])
        password = "pass:" + sys.argv[x]
        retcode = subprocess.call(["openssl","rsa", "-in", filename,"-passin",password,"-out", "dec.key"])
        if(retcode == 0):
            print(password)
else:
    i=0
    charset=list(map(str,"abcdefghijklmnopqrstuvwxyz"))
    completList = bruteforce(charset, 8)
    for element in completList:
        retcode = subprocess.call(["openssl","rsa", "-in", filename,"-passin","pass:"+element,"-out", "dec.key"],stderr =open("/dev/null","w"))
        if(retcode==0):
            print(element)
            break

        i +=1
        if i%1000==0:
            print(str(i/((len(charset)+1)**7))+" : "+str(element))
