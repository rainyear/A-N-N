from bpnn import *

TRAIN_SIZE = 20
TEST_SIZE = 600

class BP(NN):
	def test(self, testPat):
		cor = 0
		for p in testPat:
			output = self.update(p[0])
			output = self.mask(output)
			if p[1] == output:
				flag = "CORR"
				cor += 1
			else:
				flag = "INCORR"
			print "Output -> ", output , flag
		print "Test result: %.2f%%" % (float(cor) / len(testPat) * 100)
	def mask(self, output):
		output = [abs(1 - o) for o in output]
		i = 0
		m = min(output)
		for o in output:
			if o == m:
				break
			i += 1
		output = [0]*len(output)
		output[i] = 1
		return output

if __name__ == "__main__":
	inputs = []
	output = []

	cfile = open('dataSet/cfile.txt', 'r')
	pfile = open('dataSet/pfile.txt', 'r')
	jfile = open('dataSet/jfile.txt', 'r')

	cs = cfile.read()
	ps = pfile.read()
	js = jfile.read()

	cfile.close()
	pfile.close()
	jfile.close()

	for s in [cs, ps, js]:
		for t in xrange(TRAIN_SIZE):
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
		for t in xrange(TEST_SIZE):
			inl, oul = s.split('\n')[TRAIN_SIZE+10+t].split('>')
			testPat.append([[float(i) for i in inl.split()],[float(k) for k in oul.split()]])
	net.test(testPat)
