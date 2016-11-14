# Implement a function that reverses a list of elements by pushing them onto a stack in one order, 
# and write them back to the list in reversed order.
import Array_stack

def reverselist(l):
	s=Array_stack.ArrayStack()
	length=len(l)
	i=0
	while(i<length):
		s.push(l[i])
		i=i+1
	length=s.len()
	i=0
	while(i<length):
		l[i]=s.pop()
		i=i+1
	return l

if __name__=='__main__':
	l =[]
	l.append(10)
	l.append(20)
	l.append(30)
	print(l)
	print(reverselist(l))