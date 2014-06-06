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
	return reduce(lambda x,y:x*y, v)**(1/float(len(v)))

def arithmetic_mean(v):
	return avg(v)

if __name__ == '__main__':

	seq = [1,1,1,4,10,4,1,2,1]

	print 'intput sequence:',seq
	print '='*50
	print 'normalized data is', normalize(seq)
	print 'avg is', entropy(seq)
	print 'entropy is', entropy(seq)
	print 'variance is', variance(seq)
	print 'standard_deviation is', standard_deviation(seq)
	print 'geomatric_mean is',geomatric_mean(seq)
	print 'arithmetic_mean is',arithmetic_mean(seq)
