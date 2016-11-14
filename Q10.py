#Suppose you have a stack S containing n elements and a queue Q that is initially empty. Write function that
#use Q to scan S to see if it contains a certain element x, with the additional constraint that your 
#algorithm must return the elements back to S in their original order. You may use S, Q and a constant
#number of other variables.

import Array_queue
import Array_stack

def findelemenet(s,ele):
	q=Array_queue.ArrayQueue()
	l=s.len()
	j=0
	for i in range(l):
		if s.top()==ele:
			print("Element present")
			break
		else:
			q.enqueue(s.pop())
			j +=1
	if j==l:
		print("element not present")
	if q.len()!=0:
		for i in range(j):
			s.push(q.dequeue())
		for i in range(j):
			q.enqueue(s.pop())
		for i in range(j):
			s.push(q.dequeue())
	s.printelements()

#testcases
s=Array_stack.ArrayStack()
for k in range(5):
	s.push(k*10)
s.printelements()
findelemenet(s,60)
