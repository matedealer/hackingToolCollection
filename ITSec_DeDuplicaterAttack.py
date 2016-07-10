__author__ = 'joti'
import requests
import itertools
import hashlib


def getFile(url):
	f = requests.get(url);
	#print(url)
	if f.status_code != 404:
		print("==========")
		print(f.content)
		print("")
		exit()



for i in range(867):
	m = hashlib.md5()
	m.update(str(i).encode("utf8"))
	#print(str(i) + " "+m.hexdigest())
	file_name = m.hexdigest()[0:8]
	#print(str(i) + "  "+ file_name)

	url="https://securitylab.sit.tu-darmstadt.de/assets/tasks/dedup/107-2567029b64c52fc9701f92670a537781/{0}.txt".format(file_name)
	getFile(url)


