import matplotlib.pyplot as plt

def plotBeliefStates(fc,trueId,meanfc,strname,iteration):
	print iteration
	x, y = zip(*fc)
	plt.clf()
	plt.plot(x, y, 'rx', trueId[1], trueId[2], 'bs', meanfc[1], meanfc[2], 'g^')
	#plt.show()
	plt.savefig(strname+`iteration`)