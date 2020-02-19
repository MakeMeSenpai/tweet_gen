# made optional parameter to meet source_text requirements (note: this is an old way. in py 3.7.4? update there are optiional params and setting orders)
def histogram(source_text="", bysamlple=False):
    #this counts as a booleen, equvilent to none == false. this makes our default file, or the users be read
    if not source_text:
        f = open("everyManInHisHumor.txt", "r")
    else:
        f = open(source_text, "r") #FLASK STATES:  expected str, bytes or os.PathLike object, not list
    f = " ".join(f)
    f = f.split()

    word_histogram = {}

    #gives the user the option to choose a single word or see entire histogram if not ran by sample.py
    if bysamlple == False: #BYSAMPLE ALWAYS RETURNS TRUE?!
        user_input = input("Enter y to select a word (else see all): ")
        user_input.lower()
        if user_input == "y":
            return frequency(f, word_histogram)
            
    for word in f:    
        word = word.rstrip() # takes away extra white space
        word = word.rstrip('[@_!#$%^&*()<>?/"\'"|}{~:;,.]')
        word = word.capitalize()
        word_histogram[word] = word_histogram.get(word, 0) + 1

    #gives our dictiionary extra space when sprinted -note that sep and end only work in print statements
    #  becuase of this, and samples different requirements, we check if it's ran by sample first
    if bysamlple == True:
        return word_histogram
    else:
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
    
from sample import file_input
if file_input() == "True":
    pass
elif file_input() == "False":
    #Returns a clean output with seperatores to not confuse users when running the program multiple times
    print("-----------------------------------------------------------------------------------------------------")  
    print(histogram())
    print("#####################################################################################################")