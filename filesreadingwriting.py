
def reading_a_file(s):
	I = []
	with open(s, 'r') as f:
		for line in f:
			line = line.replace("\n","")
			L = line.split(",")
			name = L[0]
			email = L[-1]
			E = email.split('@')
			user_name = E[0]
			#office = L[1]
			I.append([name, user_name, email])
		return I


def writing_info_to_file(s, I):
	cnt = 1
	with open(s,"w") as f:
		for info in I:
			name = info[0]
			#office = info[1]
			user_name = info[1]
			email = info[2]
			#f.write(str(cnt)+". %s, %s, %s, %s \n" % (name, user_name, email))
			#f.write(str(cnt) + ". "+str(name)+", "+str(office)+", "+str(user_name)+", "+str(email)+"\n")
			f.write(str(cnt) + ". "+str(name)+", "+str(email)+"\n")
			cnt = cnt + 1
#def append_file(s):
#	with open(s,"r") as f:

def main():
    I = reading_a_file("mathdepartment.txt") 
    writing_info_to_file("listing.txt", I)
main()











