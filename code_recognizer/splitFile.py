pat   = {'c': "1 0 0", 'py': "0 1 0", 'java': "0 0 1"}


f = open('trainSet.txt', 'r')
s = f.read()
f.close()


cfile = open('cfile.txt', 'a')
pfile = open('pfile.txt', 'a')
jfile = open('jfile.txt', 'a')

def cntPat():
	cf = pf = jf = 0
	for l in s.split('\n')[:-1]:
		p = l.split('>')[1][1:]
		if p == pat['c']:
			cf += 1
			cfile.write(l+"\n")
		elif p == pat['py']:
			pf += 1
			pfile.write(l+"\n")
		elif p == pat['java']:
			jf +=1
			jfile.write(l+"\n")
	print "C: %d, PY: %d, JAVA: %d" % (cf, pf, jf)
#cntPat()
