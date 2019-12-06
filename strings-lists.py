"""
Working with strings and lists in python
See slicing.py for more examples of string and list Slicing
"""

def number_of_unique_chars(s):
	Unique = [] #initiates an empty list, can also use list()
	for char in s: #iterates by each element in the string s, char is just a made up variable
		if char not in Unique: #here we are using that element char and checking if it is in unique
			Unique.append(char) #now that we are sure it is not in unique, then we add to the list unique
	print(Unique) #here we are printing the list of unique letters
	print(len(Unique)) #here we are printing the length of Unique

def character_frequency(s):
	Counts = [] #want every letter [e, 6] for example
	Unique = [] #initiates an empty list, can also use list()
	for char in s:
		if char not in Unique:
			cnt = s.count(char)
			Counts.append([char, cnt]) #this is adding a smaller list to the larger Counts list
			Unique.append(char) #the char is now added to unique, so it wont be iterated again
	for element in Counts: #iterates by each element in the list Counts
		print(element) #prints each element

def main():
	s = "something" # doesnt matter if you use '' or ""
	#strings:
	"""
	print(len(s)) #will print the length of s, ex: 9
	print(s[0]) #prints the first index of s
	print(s[1]) #prints the second index of s
	print(s[len(s)-1]) #this is one way to print the last letter in s
	print(s[-1]) #this is another way to print the last letter in s
	print(s[3:])  #print [starting:ending:interval]
	print(s.upper()) #uppercase letters for s
	print(s.lower()) #lowercase letters for s
	print(s.startswith('W')) #boolean, does s start with something, case sensitive
	print(s.startswith('Wed'))
	print(s.endswith('y')) #other boolean
	s2 = s.replace("some", "other") #allows replace ("item to replace","replacement")
	print(s, s2)
	"""

	#lists
	"""
	L = ['C','h','i','c','a','g','o'] #this is a list
	print(L)
	print(L[0]) #first element in L
	print(s[1:4])  #print [starting:ending:interval]
	print("".join(L)) #leaving no space under quotation to join with no spaces
	#join allows for joining strings in a list, **must be strings only
	s3 = 'MCS 260 meets every monday, Wednesday and Friday at 12 PM in SEL 138.'
	L2 = s3.split(" ") #the split function by default returns a list
	#the above (split) creates a list strings that were seperated by " "
	print(L2)
	print(len(L2)) #to find the amount of works in the list
	print("Week" + "|" + "end")
	L3 = L.append(1) #this is how you add items to a list

	s3 = 'MCS 260 meets every monday, Wednesday and Friday at 12 PM in SEL 138.'
	#number_of_unique_chars(s3)
	character_frequency(s3)
	print(s[len(s)-1])
	"""

main()
