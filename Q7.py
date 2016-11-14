#Design a stack using a single queue as an instance variable, and only constant additional local memory 
#within the method bodies

import Array_queue

class queuestack:
	def __init__(self):
		self.s=Array_queue.ArrayQueue()

	def lengths(self):
		return self.s.len()

	def checkempty(self):
		return self.s.is_empty()

	def push(self,e):
		self.s.enqueue(e)

	def pop(self):
		a=[]	
		for i in range(self.lengths()):
			a.append(self.s.dequeue())
		ele=a.pop()
		for i in range(len(a)):
			self.s.enqueue(a[i])
		return ele

	def top(self):
		a=[]
		for i in range(self.lengths()):
			a.append(self.s.dequeue())
		for i in range(len(a)):
			if a[i]!=None:
				self.s.enqueue(a[i])
		return a.pop()
		
#Test cases		
sq=queuestack()
sq.push(10)
assert(sq.lengths()==1)
sq.push(20)
sq.push(30)
sq.push(40)
assert(sq.pop()==40)
assert(sq.top()==30)
assert(sq.lengths()==3)
