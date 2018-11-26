#simple stack LIFO

class Stack():
	def __init__(self):
		self.stack = []

	def add(self, val):
		self.stack.append(val)

	def pop(self):
		self.stack.pop()

stack1 = Stack()

stack1.add(2)
stack1.add(4)
stack1.add(5)
print(stack1.stack)
stack1.pop()
print(stack1.stack)

