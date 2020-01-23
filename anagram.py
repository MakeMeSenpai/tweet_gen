f = open("dictionary_words.txt", "r")
f = f.readlines()
f = "".join(f)
f = f.split("\n")
user_input = input("type an anagram: ")

def check(user_input, f):
    for word in f:
        if(sorted(user_input)== sorted(word)): 
            print(word)          
            
check(user_input, f)