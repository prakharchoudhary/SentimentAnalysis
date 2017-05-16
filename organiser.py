'''
assemble the individual text documents from the decompressed 
download archive into a single CSV file
'''

import pyprind
import pandas as pd
import os
pbar = pyprind.ProgBar(50000)
labels = {'pos':1, 'neg':0}

def organise_data():
	df = pd.DataFrame()

	for s in ('test', 'train'):
		for l in ('pos', 'neg'):
			path = './aclImdb/%s/%s' % (s, l)
			for file in os.listdir(path):
				with open(os.path.join(path, file), 'r', encoding='utf-8') as infile:
					txt = infile.read()
				df = df.append([[txt, labels[l]]], ignore_index=True)
				pbar.update()
	df.columns = ['review', 'sentiment']
	return df

if __name__=='__main__':
	organise_data()