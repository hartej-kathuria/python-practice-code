# Implement a function with signature transfer(S,T) that transfers all elements from Stack S onto Stack T,
# so that that elements that starts at the top of S is the first to be inserted into T, 
# and element at the bottom of S ends up at the top of T.
import Array_stack

def stckexch(s,t):
	print(s.top())
	length=s.len()
	l=0
	while(l < length):
		t.push(s.pop())
		#print(t.top())
		l=l+1
	print(t.top())

if __name__=='__main__':
	s=Array_stack.ArrayStack()
	t=Array_stack.ArrayStack()
	s.push(10)
	s.push(20)
	s.push(30)
	stckexch(s,t)

