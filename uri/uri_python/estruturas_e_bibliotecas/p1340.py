import heapq

while True:
	try:
		N = int(input())

		stack = []
		queue = []
		heap = []
		flagStack = True
		flagQueue = True
		flagHeap = True
		
		for i in range(N):
			entry = input().split(" ")
			if int(entry[0]) == 1:
				stack.append(int(entry[1]))
				queue.append(int(entry[1]))
				heapq.heappush(heap, -1*int(entry[1]))
			else:
				r = int(entry[1])
				if stack.pop() != r:
					flagStack = False
				if queue.pop(0) != r:
					flagQueue = False
				if heapq.heappop(heap) != -1*r:
					flagHeap = False

		if (flagStack and flagQueue) or (flagStack and flagHeap) or (flagQueue and flagHeap):
			print("not sure")
		elif flagStack:
			print("stack")
		elif flagQueue:
			print("queue")
		elif flagHeap:
			print("priority queue")
		else:
			print("impossible")		

	except EOFError:
		break
