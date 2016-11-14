# Design a queue using two stacks as instance variables, 
# such that all queue operations execute in amortized O(1) time.

import Array_stack

class stackqueue:

	def __init__(self):
		self.q1=Array_stack.ArrayStack()
		self.q2=Array_stack.ArrayStack()

	def lengths(self):
		return self.q1.len()

	def checkempty(self):
		return self.q1.is_empty()

	def first(self):
		for i in range(self.lengths()-1):
			self.q2.push(self.q1.pop())
		a=self.q1.pop()
		self.q1.push(a)
		for i in range(self.q2.len()):
			self.q1.push(self.q2.pop())
		return a

	def enqueue(self,ele):
		self.q1.push(ele)

	def dequeue(self):
		for i in range(self.lengths()-1):
			self.q2.push(self.q1.pop())
		a=self.q1.pop()
		for i in range(self.q2.len()):
			self.q1.push(self.q2.pop())
		return a

#testcases
qs=stackqueue()
qs.enqueue(10)
assert(qs.lengths()==1)
qs.enqueue(20)
assert(qs.first()==10)
assert(qs.dequeue()==10)
