
def reversal():
    sw = input("Sentence or word? (S/W)")
    sw = sw.upper()
    while True:
        if sw == "S":
            sentence = input("Type out your sentence: ")
            words = sentence.split()
            new_sentence = words.reverse()
            new_sentence = " ".join(words)
            print(new_sentence)
            return False
        elif sw == "W":
            letters = []
            word = input("Type a word: ")
            if word.isalpha():
                for l in word:
                    letters.insert(0, l)
                new_word = "".join(letters)
                print(new_word)
                return False
            else:
                print("Sorry, what was that?")
                return True
        else:
            print("Sorry, what was that?")
            return True

reversal()
