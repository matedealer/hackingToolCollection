#!/usr/bin/python3
from functools import reduce
import hashlib
import struct

def matrixMult(a, b):
	newMatrix = [[0 for i in range(len(b[0]))] for j in range(len(a))]

	for i in range(len(a)):
		for j in range(len(b[0])):
			for c in range(len(a[0])):
				newMatrix[i][j] += a[i][c] * b[c][j]

	return newMatrix


def euklid(a, b):
	matrix = [[1,0],[0,1]]

	stop = False

	while not stop:
		r = a % b
		q = int(a / b)
		a = b
		b = r

		matrix = matrixMult([[0,1],[1,-q]], matrix)

		if r == 0:
			stop = True

	return (a, matrix[0][0], matrix[0][1])


def modexp(m, e, n):
	if e==0:
		return 1
	if e%2==1:
		return modexp(m, e-1, n)*m % n
	return modexp(m, e//2, n)**2 % n

def compare(a,b):
	if len(a)>len(b):
		return a
	else:
		return b

p = 982451219
q = 982451191
n = 965210370205951829
e = 364141

phi_n = (p-1)*(q-1)
d=euklid(phi_n, e)[2]

print(phi_n)
print(d)
outfile = open("weak_rsa.bin","wb")


game_enc = open("game.enc","r").read()
cleartext_list = []


print("==========================================================");
for element in game_enc.split("|"):
	int_element = int(str(element),16)
	cleartext = "0"+bin(modexp(int_element,d,n))[2:]
	cleartext_list.append(int(str(cleartext[0:8]),2))
	cleartext_list.append(int(str(cleartext[8:16]),2))
	cleartext_list.append(int(str(cleartext[16:24]),2))
	cleartext_list.append(int(str(cleartext[24:32]),2))

#print(cleartext_list)
outfile.write( bytes(cleartext_list))
	


