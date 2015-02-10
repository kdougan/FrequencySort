#!/usr/bin/python
import pprint
import math
from collections import Counter

def fsort(incoming_list, interval):
	tmp = []
	slist = []
	icopy = incoming_list
	for i in range(interval):
		slist.append([])
	buc = {'total': 0.0,
		   'items': {}}
	for i in icopy:
		buc['total'] += 1.0
		if i not in tmp:
			slist.append([])
			tmp.append(i)
			buc['items'][i] = {'count': 1.0,
							   'ratio': 0.0}
		else:
			buc['items'][i]['count'] += 1.0
		tot = float(len(icopy))
		count = float(buc['items'][i]['count'])
		buc['items'][i]['ratio'] = count / tot

	for i in range(interval):
		for x in buc['items']:
			tmp = []
			ratio = buc['items'][x]['ratio']
			for l in icopy:
				if not (slist[i].count(x) >= math.ceil(interval * ratio)):
					slist[i].append(x)
					tmp.append(x)
			for t in tmp:
				if icopy.count(x):
					icopy.remove(t)
	for i in range(len(slist)):
		slist[i].sort(key=Counter(slist[i]).get, reverse=True)
	ret = [item for sublist in slist for item in sublist]
<<<<<<< HEAD
	return ret
=======
	return ret
>>>>>>> FETCH_HEAD
