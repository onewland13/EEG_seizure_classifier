import os
import sys
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-whitegrid')
import csv
from collections import defaultdict

def main(a):
	subject_chunks, label_chunks = ingest_data(a[0])

	per_subject_plots(subject_chunks)

def per_subject_plots(subject_chunks):
	data = subject_chunks['V1.354']


	fig = plt.figure()
	ax = plt.axes()

	for chunk in data:
		sns.relplot(data=chunk, x='time', y='value', kind='line')

	plt.show()

def ingest_data(filename):
	data = list(csv.reader(open(filename)))
	subject_chunks = defaultdict(list)
	label_chunks = defaultdict(list)

	for row in data[1:]:
		row_info = row[0].split('.')
		subject = '.'.join(row_info[1:])

		subject_chunks[subject].append(row[1:])

		label_chunks[int(row[-1])].append(row[1:-1])

	return subject_chunks, label_chunks

if __name__ == '__main__': 
	sys.exit(main(sys.argv[1:]))