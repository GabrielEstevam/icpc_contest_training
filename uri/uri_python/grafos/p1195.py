
class bree(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

	def add(self, data):
		if self.data is None:
			self.data = data
		else:
			node = bree()
			if data > self.data:
				if self.right is None:
					node.data = data
					self.right = node
				else:
					self.right.add(data)			
			else:
				if self.left is None:
					node.data = data
					self.left = node
				else:
					self.left.add(data)

def pre(node):
	aux1 = ""
	aux2 = ""
	if node.left != None:
		aux1 = pre(node.left)
	if node.right != None:
		aux2 = pre(node.right)
	return " " + str(node.data) + aux1 + aux2

def post(node):
	aux1 = ""
	aux2 = ""
	if node.left != None:
		aux1 = post(node.left)
	if node.right != None:
		aux2 = post(node.right)
	return  aux1 + aux2 + " " + str(node.data)

def infix(node):
	aux1 = ""
	aux2 = ""
	if node.left != None:
		aux1 = infix(node.left)
	if node.right != None:
		aux2 = infix(node.right)
	return aux1 + " " + str(node.data) + aux2

N = int(input())
for n in range(N):
	arvore = bree()
	size = int(input())
	entry = input().split(" ")
	for i in range(size):
		arvore.add(int(entry[i]))

	print("Case", str(n+1)+":")
	out = pre(arvore)
	print("Pre.:"+out)
	out = infix(arvore)
	print("In..:"+out)
	out = post(arvore)
	print("Post:"+out)
	print("")
