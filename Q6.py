

import Array_stack

def function(R,S,T):
	tl=T.len()
	sl=S.len()
	for i in range(sl):
		R.push(S.pop())
	for i in range(tl):
		R.push(T.pop())
	for i in range(sl+tl):
		S.push(R.pop())


R=Array_stack.ArrayStack()
S=Array_stack.ArrayStack()
T=Array_stack.ArrayStack()
R.push(1)
R.push(2)
R.push(3)
S.push(4)
S.push(5)
for i in range(6,10):
	T.push(i)
function(R,S,T)
S.printelements()	