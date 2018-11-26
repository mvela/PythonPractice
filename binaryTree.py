#simple binary treee

class bTree:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val
	
	def insert(self, val):
		#if val exists
		if self.val:
			
			if val < self.val:
				if self.left == None:
					self.left = bTree(val)
				else:
					self.left.insert(val)
			
			elif val > self.val:
				if self.right == None:
					self.right = bTree(val)
				else:
					self.right.insert(val)	
		
		else: self.val = val

	def printTree(self):
		if self.left:
			self.left.printTree()
		if self.right:
			self.right.printTree()
		print(self.val)

myTree = bTree(10)
myTree.insert(22)
myTree.insert(24)
myTree.insert(16)
myTree.insert(56)
myTree.insert(34)
myTree.insert(4)
myTree.insert(7)
myTree.printTree()

