import numpy as np
import string
import math
import re

class feval(object):
	"""docstring for eval"""
	
	def eventSim(self, ev, tr):


		set1 = set(ev)
		set2 = set(tr)
		print(set1)
		print(set2)
		
		set_event_trend = set(set1).intersection(set2)
		print(set_event_trend)

		if len(set_event_trend) == 0:
			print("detected event is not in trending event list")
		else:
			common_event_ratio = (len(set_event_trend))/(len(set1)+len(set2))
			print(common_event_ratio)


if __name__ == '__main__':

	devent = []
	tevent = []

	with open("event_details.txt", "r") as f1:
		for line in f1:
			term = line.replace('\n', '')
			terms = re.findall('[a-zA-Z]+', term)
			devent.append(terms)
	d = sum(devent, [])

	with open("trending_event.txt", "r") as f2:
		for line in f2:
			term = line
			trend = term.replace('#', '')
			trends = trend.replace('\n', '')
			tevent.append(trends)

	ss = feval()
	ss.eventSim(d, tevent)