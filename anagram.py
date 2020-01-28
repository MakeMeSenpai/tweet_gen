f = open("words.txt", "r")
f = f.read()
f = "".join(f)
f = str(f)
f = f.split(" ")
user_input = input("type an anagram: ")
def check(user_input, f):
    for word in f:
        if(sorted(user_input)== sorted(word)): 
            print(word)          
            
check(user_input, f)