"""
Sets in python 
"""

def main():
	E = {}
	S = {1,2,3,3,4,5,5,6} #the set will remove redundances!!!!! unique elements only
	# S = set((6,6,4,1,2,3,3,4,5,5,6))  ---> this converts it from tuple to a set
	# S = set([6,6,4,1,2,3,3,4,5,5,6])  ---> this converts it from list to a set
	S.add('hello') #----> adds unique element
	S.clear() #----> clears the set altogether, meaning makes it empty
	#A = {1,2,3,4,5,6,7,8}
	#B = {4,5,6,7,8,9,10,11}
	#print(A.difference(B)) # A-B, ---->elements in A but not in B
	#B.discard(11) # remove 11, permanentently
	#print(B)
	#print(A.union(B)) # A | B ---> stands for union
	#print(A.intersection(B)) #returns values that both lists have in common, A & B
	#print({7,8,9,}.isdisjoint({0,1,2,3,4})) #share no elements in common, no intersection, true or false
	#print({1,2,3}.issubset({0,1,2,3,4,5})) # is the first set a part of the other set, true or false
	#print({8,9}.issuperset({1,2,3,4,5,6,7,8,9})) #is the first set a superset of the second, opposite of subset
	#print({4,6,8,9,5}.pop()) #pops the item with the lowest hash, totally random
	#C = {1,2,3,4,5}
	#C.remove(5) #----> get rid of an element
	#print(C)
	#D = A.symmetric_difference(B) # elements that are in one and not in the other, basically those that are unique
	#print(D)
	A = {-5,1,2,3,4,5,6,7,8,20}
	#print(len(A))
	#print(max(A)) # only works if elements are the same, ex: numbers
	#print(sum(A))
	#print(8 in A)
	#for k in A:
	#	print(k)
	"""
	for k in range(len(A)): # this will generate error, since sets do not have indexing
		print(A[K])
	"""

main()
