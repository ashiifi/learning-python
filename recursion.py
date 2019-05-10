"""
recursion has 2 components.
	stopping condition(s)
	set of procedures reducing all other conditions
	ex: Fibonacci sequence -- (function that is calling itself)
	f(n) = f(n-1) + f(n-2)...
"""
def F(n):
    #Computes the nth value in the Fibonacci sequence.
    if n == 0 or n == 1:
       return 1
    else:
       return F(n-1)+F(n-2)

def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)

def P(word):
	if len(word) <= 1:
		return True
	elif word[0] != word[-1]:
		return False
	elif len(word) == 2:
		return True
	else:
		return P(word[1:len(word)-1])


def main():
	#print(F(5))
	#print(fact(10))
	print(P(""))
main()
