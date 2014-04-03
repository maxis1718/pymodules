import math

def entropy(X, b=2):
	S = float(sum(X))
	return -1.0*sum([x/S*math.log(x/S, b) for x in X if x/S > 0.0])

def normalize(v): 
	return v if sum(v) == 0 else map( lambda x:x/float(sum(v)), v)

def avg(v):
	return sum(v)/float(len(v))	

def variance(v, normalized=False):
	v = normalize(v) if normalized else v
	N = float(len(v))
	miu = float(sum(v))/N
	return sum([(x-miu)**2 for x in v])/N

def standard_deviation(v, normalized=False):
	return math.sqrt(variance(v, normalized))
	# v = normalize(v) if normalized else v
	# N = float(len(v))
	# miu = float(sum(v))/N
	# return math.sqrt(sum([(x-miu)**2 for x in v])/N)



def geomatric_mean(v):
	return reduce(lambda x,y:x*y, v)**(1/float(len(a)))

def arithmetic_mean(v):
	return avg(v)