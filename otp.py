#!/usr/bin/env python3

optkey = bytearray(open("otpkey.bin", "rb").read())
optcipher = bytearray(open("otpcipher.bin", "rb").read())
opttext = bytearray()
outfile = open("otpclear.bin","wb")

for i in range(len(optcipher)):
    opttext.append(optkey[i]^optcipher[i])


outfile.write(opttext)


print( "".join(map(chr, opttext)))



#y = int(chiper_bin,2) ^ int(key_bin,2)
#print('{0:b}'.format(y))

#print(chiper_bin);