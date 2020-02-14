# made optional parameter to meet source_text requirements (note: this is an old way. in py 3.7.4? update there are optiional params and setting orders)
def histogram(source_text=None):
    #this counts as a booleen, due to none = false. this makes our default file, or the users be read
    if not source_text:
        f = open("everyManInHisHumor.txt", "r")
    else:
        f = open(source_text, "r")
    f = " ".join(f)
    f = f.split()

    word_histogram = {}

    #gives the user the option to choose a single word or see entire histogram
    user_input = input("Enter y to select a word (else see all): ")
    user_input.lower()
    if user_input == "y":
        return frequency(f, word_histogram)
            
    for word in f:    
        word = word.rstrip() # takes away extra white space
        word = word.capitalize()
        word_histogram[word] = word_histogram.get(word, 0) + 1

    #gives our dictiionary extra space when sprinted -note that sep and end only work in print statements
    for k, v in word_histogram.items():
        print(str(k), str(v), sep="-->", end=" | ")

def unique_words(f):
    for count in range(len(f)):
        count += 1
    return count

def frequency(f, word_histogram):
    selected = input("Type your word: ")
    selected = selected.capitalize() # cleans our output by turning them all capital
    for word in f:
        word = word.capitalize()
        if selected == word:
            word_histogram[selected] = word_histogram.get(selected, 0) + 1
    return f"{word_histogram} | Out of Unique words:{unique_words(f)}"
    

#Returns a clean output with seperatores to not confuse users when running the program multiple times
print("-----------------------------------------------------------------------------------------------------")  
print(histogram())
print("#####################################################################################################")