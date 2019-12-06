"""
Slicing of lists and strings
"""

def main():
	"""
	slicing: L[start : stop : increment]
	"""
	L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	S = "0123456789abscdef"
	"""
	print(L[0]) #first element of L
	print(S[0])

	print(L[-3]) #third to last element
	print(S[-3])

	print(L[:]) #prints all elements since there is no start or stop
	print(S[:])

	print(L[0:]) #prints from index 0 to the end
	print(S[0:])

	print(L[2:]) #prints from index 2 to the end
	print(S[2:])

	print(L[:3]) #prints from the beginning to index 3
	print(S[:3])

	print(L[:-1])
	print(S[:-1])

	print(L[4:9])
	print(S[4:9])

	print(L[::2])
	print(S[::2])

	print(L[1:9:3])
	print(S[1:9:3])

	L2 = [1,2,3]
	S2 = "MCS"
	#print(L2+L2,S2+S2)
	#print(4*L2,3*S2)
	#print(sorted(S2))
	print("".join(sorted(S2)))
	"""
	#List comprehensions
	L3 = [x**2 for x in range(0,10)]
	L4 = [2*z + z for z in [6,1,0,3,2]]
	L5 = ['a', 'X', 3.1, 7,8,9, [1,2,3], 'hello']
	L6 = [x**2 for x in L5 if type(x) == int]
	L7 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	L8 = [k for k in L7 if k >5]
	print(L8)

main()
