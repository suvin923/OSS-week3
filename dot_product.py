def dot_product(a,b):
	sum = 0
	for i in range(len(a)):
		sum = sum + a[i] * b[i]
	return sum

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
dot = dot_product(arr1,arr2)
print(dot)
