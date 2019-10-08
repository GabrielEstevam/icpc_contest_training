n = int(input())
raiz = 1
fr = 0
for i in range(n):
	fr = 1/(fr+2)
raiz += fr
print("%.10f" % raiz) 
