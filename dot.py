def dot_product(a,b):
	for i in range(len(a)):
		sum += a[i] * b[i]
	return sum

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
dot = dot_product(a,b)
print(dot)
