import sys, time

class ProgressBar(object):
	"""
	ProgressBar
	usage:

		## new an object
		pbr = ProgressBar( <total instance number> )

		## in for loop
			pbr.draw( <current instance index> )

		## close
		pbr.close()
	"""
	total = 100
	current = 0
	percent = 0.0
	def __init__(self, total):
		super(ProgressBar, self).__init__()
		self.total = total

	def _update(self, current):
		self.current = current
		self.percent = current/float(total)*100

	def draw(self, current):

		self._update(current)

		sys.stderr.write('[%s> %.2f%%%s]\r' % ('='*(int(self.percent)+1), self.percent, ' '*(100-int(self.percent) ) ) )
		sys.stderr.flush()

	def close(self):
		sys.stderr.write('\n')
	
if __name__ == '__main__':
	
	total = 500
	pbr = ProgressBar(total)

	for i in range(total):
		
		current = i+1

		pbr.draw(current)
		
		time.sleep(0.005)
	
	pbr.close()