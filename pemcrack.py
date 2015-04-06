#!/usr/bin/python

import subprocess, sys

filename = sys.argv[1]
print(filename)
print(sys.argv[2])
for x  in range(2,len(sys.argv)):
    print(sys.argv[x])
    password = "pass:" + sys.argv[x]
    retcode = subprocess.call(["openssl","rsa", "-in", filename,"-passin",password,"-out", "dec.key"])
    if(retcode == 0):
            print(password)
