# Implement a transfer function and two temporary stacks, 
# to replace the contents of a given stack S with those same elements, but in reverse order.

import Array_stack

def reversestack(s):
	a=Array_stack.ArrayStack()
	b=Array_stack.ArrayStack()
	l=s.len()
	for i in range(l):
		a.push(s.pop())
	for i in range(l):
		b.push(a.pop())
	for i in range(l):
		s.push(b.pop())

s=Array_stack.ArrayStack()
s.push(10)
s.push(20)
s.push(30)
reversestack(s)
print(s.top())	 