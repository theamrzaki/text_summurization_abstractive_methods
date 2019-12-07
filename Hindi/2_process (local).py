#pip install langdetect
import json
import os
import pandas
from langdetect import detect
import pickle

from __future__ import print_function
import io
import sys
import re

class ProgressBar(object):
    DEFAULT = 'Progress: %(bar)s %(percent)3d%%'
    FULL = '%(bar)s %(current)d/%(total)d (%(percent)3d%%) %(remaining)d to go'

    def __init__(self, total, width=40, fmt=DEFAULT, symbol='=',
                 output=sys.stderr):
        assert len(symbol) == 1

        self.total = total
        self.width = width
        self.symbol = symbol
        self.output = output
        self.fmt = re.sub(r'(?P<name>%\(.+?\))d',
            r'\g<name>%dd' % len(str(total)), fmt)

        self.current = 0

    def __call__(self):
        percent = self.current / float(self.total)
        size = int(self.width * percent)
        remaining = self.total - self.current
        bar = '[' + self.symbol * size + ' ' * (self.width - size) + ']'

        args = {
            'total': self.total,
            'bar': bar,
            'current': self.current,
            'percent': percent * 100,
            'remaining': remaining
        }
        print('\r' + self.fmt % args, file=self.output, end='')

    def done(self):
        self.current = self.total
        self()
        print('', file=self.output)



full_path = r"E:\Projects\Python\Hindi_News\data\data"
dirs = os.listdir(full_path)
resultdict = []

#with open('hindi.pkl', 'rb') as handle:
#	b = pickle.load(handle)

for d in dirs:
	list_files = [file_json for file_json in os.listdir(full_path+"\\"+d) if file_json.endswith('.json')]
	if len(list_files)==0:
		continue
	progress = ProgressBar(len(list_files), fmt=ProgressBar.FULL)
	for fili in list_files:
		with open(os.path.join(full_path+"\\"+d, fili), encoding="utf-8") as inputjson:
			objj = json.load(inputjson) 
			row = {}
			row["title"] = objj["title"]
			row["text"] = objj["text"]
			try:
				if detect(objj["text"]) == "hi" and objj['text'] != "":
					resultdict.append( row )
			except:
				resultdict.append( row )
			progress.current += 1
			progress()
	progress.done()

with open('hindi.pkl', 'wb') as handle:
	pickle.dump(resultdict, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("converting to dataframe ..")
dataframe = pandas.DataFrame(resultdict)

print("saving ..")
with open("HindiNewsBook.csv", "a" ,encoding='utf-8') as csvout:
	dataframe.to_csv(csvout, encoding='utf-8', index=False)

print("done el7")	
