"""
Dictionary comprehension:
Key Value pairs
"""
from operator import itemgetter #importing package operator

def book_word_frequency(s):
    with open(s, r, errors='ignore') as f:
        text = f.read() #read in the entire book at once and assign it to variable text
        text = text.replace("\n"," ")
        text = text.replace(".","")
        text = text.replace("?","")
        text = text.replace("!","")
        text = text.replace("-","")
        text = text.replace("(","")
        text = text.replace(")","")
        text = text.replace(",","")
    text = text.lower() #convert all words to lowercase
    words = text.split(" ") #split an empty space turns the tex to a list of words

    D = {} #empty dictionary
    for word in words:
        if word not in D:
            D.update({word: 1}) #putting the word into the dictionary with a value 1
        else:
            D[word] = D[word] + 1 #adding 1 to the value every time that word is used
    E = sorted(D.items(), key = lambda x: x[1]) # add ,reverse = true to reverse the order
    for e in E:
        print(e)

    print(len(E))

def main():
    """
    D = {} #empty dictionary
    D = {'January': 1, 'February': 2, 'March': 3, 'April': 4} #first element is key, key-value pairs January = key, 1 = value
    #print(len(D)) #returns the number of key-value pairs in D
    D['June'] = 6 # adding key-value pair to a dictionary g # another way of adding key-value pair to a dictionary
    D[key] gives you the value
    K = D.keys() #returns all keys inside dictionary or use list(D.keys()) to convert into list
    V = D.values() #returns all values inside dictionary
    #for k in D: # another way to call keys and values
    #print(k, D[k])
    del D['July'] #remove key-value from dictionary
    """
    book_word_frequency('thehoundofthebaskerviles.txt')
    
main()
