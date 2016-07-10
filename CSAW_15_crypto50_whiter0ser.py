__author__ = 'joti'

import random
import string

# file="/home/joti/Dokumente/hacking/hDa_CTF/CSAW_2015/crypto_whiter0se/eps1.7_wh1ter0se_2b007cf0ba9881d954e85eb475d0d5e4.m4v"
#
# f= open(file, "r").read()
#
#
# print(f)
chiper = ""
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
chiperFreq={}

for key in englishLetterFreq:
    chiperFreq[key]=chiper.count(key, 0, len(chiper))


#print(chiperFreq)
orderdList = []
tmp_highest = ""
while len(orderdList)!= len(chiperFreq):
    tmp_highest = list(chiperFreq.keys()) [random.randint(0, len(chiperFreq)-1)]
    while(tmp_highest in orderdList):
        tmp_highest = list(chiperFreq.keys()) [random.randint(0, len(chiperFreq)-1)]

    for key in chiperFreq:
        if key not in orderdList and chiperFreq[tmp_highest] < chiperFreq[key] :
            tmp_highest = key

    orderdList.append(tmp_highest)

print(orderdList)
orderdListEng = []
tmp_highest = ""
while len(orderdListEng)!= len(englishLetterFreq):
    tmp_highest = list(engli/home/jotishLetterFreq.keys()) [random.randint(0, len(englishLetterFreq)-1)]
    while(tmp_highest in orderdListEng):
        tmp_highest = list(englishLetterFreq.keys()) [random.randint(0, len(englishLetterFreq)-1)]

    for key in englishLetterFreq:
        if key not in orderdListEng and englishLetterFreq[tmp_highest] < englishLetterFreq[key] :
            tmp_highest = key

    orderdListEng.append(tmp_highest)

print(orderdListEng)
translate_dict = {}
for i in range(len(orderdList)):
    translate_dict[orderdList[i]]=orderdListEng[i]

print (chiper)


#print(chiper.translate(str.maketrans(translate_dict)))

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)





