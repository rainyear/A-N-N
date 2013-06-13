from bpnn import *

RANGE = 10
class BP(NN):
	pass

if __name__ == "__main__":
	tf = open("./trainSet.txt", 'r')
	ts = tf.read()
	tf.close()

	inputs = []
	output = []

	cfile = open('cfile.txt', 'r')
	pfile = open('pfile.txt', 'r')
	jfile = open('jfile.txt', 'r')

	cs = cfile.read()
	ps = pfile.read()
	js = jfile.read()

	cfile.close()
	pfile.close()
	jfile.close()

	for s in [cs, ps, js]:
		for t in xrange(RANGE):
			inl, oul = s.split('\n')[t].split('>')
			inputs.append([float(i) for i in inl.split()])
			output.append([float(i) for i in oul.split()])
	print len(inputs)
	print len(output)
	pat  = []
	for i in xrange(len(inputs)):
		pat.append([inputs[i], output[i]])
	net = BP(20, 8, 3)
	net.train(pat)

	testPat = []
	for s in [cs, ps, js]:
		for t in xrange(20):
			inl, oul = s.split('\n')[RANGE+10+t].split('>')
			testPat.append([[float(i) for i in inl.split()],[float(k) for k in oul.split()]])
	net.test(testPat)
