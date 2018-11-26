#Singularly linked list

class node:
	def __init__(self, dataval = None):
		self.dataval = dataval
		self.nextval = None

class SLL:
	def __init__(self):
		self.headval = None

	def printVals(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval) 		#value
			printval = printval.nextval #next object
	
	def newFrontNode(self, newData):
		newNode = node(newData)
		newNode.nextval = self.headval # newNodes next value is equal to the headval (head node)
		self.headval = newNode # the new head node is equal to the new node


linkedList = SLL()
linkedList.headval = node("One")
n2 = node("Two")
n3 = node("three")

linkedList.headval.nextval = n2
n2.nextval = n3


linkedList.printVals()
print("\n")
linkedList.newFrontNode("Zero")
linkedList.printVals()
