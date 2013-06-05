import os, os.path, sys, re
from collections import Counter

codes = ['c', 'py', 'java']
chars = [')', '(', '_', '.', '=', ';', '"', ',', "'", '*', '/', '{', '}', ':', '-', '0', '+', '1', '[', ']']

#rats = cnts = {'c':Counter(chars), 'py': Counter(chars), 'java': Counter(chars)}
#tots = {'c': 0, 'py': 0, 'java': 0}

def showFile(args, path, fname):
	for f in fname:
		rats = cnts = {'c':Counter(chars), 'py': Counter(chars), 'java': Counter(chars)}
		tots = {'c': 0, 'py': 0, 'java': 0}
		#print os.path.join(path, f)
		tmpf = open(os.path.join(path, f), 'r')
		tmps = tmpf.read()
		tmpf.close()
		tmps = re.sub(r'\s', '', tmps)

		tots[args] += len(tmps)
		if tots[args] < 200:
			continue
		#print tmps
		for s in tmps:
			if s in chars:
				cnts[args][s] += 1
		calRatios(args, rats, cnts, tots)
def calRatios(code, rats, cnts, tots):
	#print "Counter of #FILE<*.%s>:" % code
	#print cnts[code]
	tmps = ""
	for i in range(len(chars)):
		#print cnts[code][chars[i]]
		rats[code][chars[i]] = float('%.4f' % ((cnts[code][chars[i]] - 1.0) / tots[code]))
		tmps += str(rats[code][chars[i]]) + " "
	tmps += "> %s\n" % code
	#print "Ratios of #FILE<*.%s>:" % code
	#print rats[code]
	#print '\n'
	trainSet = open('trainSet.txt', 'a')
	trainSet.write(tmps)
	trainSet.close()
def main():
	for c in codes:
		os.path.walk(c, showFile, (c))
main()