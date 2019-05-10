"""
working with strings in python
"""

def number_of_unique_chars(s):
	Unique = []
	for char in s:
		if char not in Unique:
			Unique.append(char)
	print(len(Unique))

def character_frequency(s):
	Counts = [] # want every letter [e, 6] for example
	Unique = []
	for char in s:
		if char not in Unique:
			cnt = s.count(char)
			Counts.append([char, cnt])
			Unique.append(char)
	for element in Counts:
		print(element)


def main():
	s = "Wednesday" # doesnt matter what to use '' or ""
	"""
	print(len(s)) will print the length of s, ex: 9
	print(s[0])
	print(s[1])
	print(s[len(s)-1])
	print(s[3:]) 
	print(s.upper()) #uppercase letters for s
	print(s.lower()) #lowercase letters for s
	print(s.startswith('W')) does s start with something, case sensitive
	print(s.startswith('Wed'))
	print(s.endswith('y'))
	s2 = s.replace("Wednes", "Fri")
	print(s, s2)
	L = ['C','h','i','c','a','g','o']
	print(L)
	print("".join(L)) #leaving no space under quotation to join with no spaces
	s3 = 'MCS 260 meets every monday, Wednesday and Friday at 12 PM in SEL 138.'
	L2 = s3.split(" ") #the split function by default returns a list
	print(L2)
	print(len(L2)) #to find the amount of works in the list
	print("Week" + "|" + "end")
	"""
	s3 = 'MCS 260 meets every monday, Wednesday and Friday at 12 PM in SEL 138.'
	#number_of_unique_chars(s3)
	character_frequency(s3)
	print(s[len(s)-1])

main()
