import math

def entropy(X, b=2):
	S = float(sum(X))
	return -1.0*sum([x/S*math.log(x/S, b) for x in X if x/S > 0.0])

def normalize(v): 
	return v if sum(v) == 0 else map( lambda x:x/float(sum(v)), v)

def standard_deviation(v, normalized=False):
	v = normalize(v) if normalized else v
	N = float(len(v))
	miu = float(sum(v))/N
	return math.sqrt(sum([(x-miu)**2 for x in v])/N)

def avg(v):
	return sum(v)/float(len(v))	