from numpy import random
from numpy.random import choice
from dictogram import Dictogram


class MarkovChain:
    def __init__(self, word_list):
        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(word_list)
         self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                # histogram[next_word] = histogram.get(next_word, 0) + 1
                histogram.add_count(next_word) # ensures that tokens/total is updated
            else: #first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        #defines markov_chain as a dictonary
        markov_chain = {}
        # selects a random word for our object from markov chain keys
        current_word = random.choice(list(self.markov_chain.keys()))
        # Creates our sentence list
        sentence = []
        # while i is 0-num_words
        for i in range(num_words):
            #defines our Dictogram object
            markov_chain[current_word] = Dictogram([current_word])
            #sets temp_word to a random word by weighted frequency
            temp_word = markov_chain[current_word].sample_by_frequency()
            # appends it to our sentence
            sentence.append(temp_word)
            #changes our focus to the next word
            current_word = temp_word
        #return the list as a string
        return " ".join(sentence)

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))