import math
def entropy(X, b=2):
	S = float(sum(X))
	return -1.0*sum([x/S*math.log(x/S, b) for x in X if x/S > 0.0])


def standard_deviation(X):
	N = float(len(X))
	miu = float(sum(X))/N
	return math.sqrt(sum([(x-miu)**2 for x in X])/N)

def geomatric_mean(X):
	return reduce(lambda x,y:x*y, X)**(1/float(len(a)))