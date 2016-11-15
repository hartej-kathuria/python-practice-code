class Full(Exception):
	""" Error attempting to access an element from an empty container """

	def __init__(self, args):
		self._args = args


class ArrayStack:
	""" LIFO stack implementation usinng Python list as underlying storage """
	MAXLEN=8
	def __init__ (self):
		""" Creat an empty stack """
		self._data = []

	def len (self):
		""" Return the number of elements in the stack """
		return len (self._data)
	
	def is_empty (self):
		""" Return True if the stack is empty """
		return len(self._data) == 0

	def push (self, e):
		""" Add element e to the top of the Stack """
		if self.len()==8:
			try:
				raise Full('Unable to push, stack is full')
			except Full as err:
				print(err._args)
		else:
			self._data.append(e)

	def top (self):
		""" Return (but do not remove) the element at the top of the stack 

		"""
		if self.is_empty():
			print('Stack is empty')
		else:
			return self._data[-1]

	def pop (self):
		""" Remove and return the element from the top of the stack
		"""
		if self.is_empty():
			print('Stack is empty')			
		else:
			return self._data.pop()

	def printelements (self):
		print(self._data)

#testcases
s=ArrayStack()
for i in range(9):
	s.push(i)