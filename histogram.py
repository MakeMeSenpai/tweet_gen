def histogram(f):
    word_histogram = {}
    total = 0

    for word in f:    
        word = word.rstrip() # takes away extra white space
        word = word.rstrip('[@_!#$%^&*()<>?/"\'"|}{~:;,.]')
        word = word.capitalize()
        word_histogram[word] = word_histogram.get(word, 0) + 1
        total += 1

    print(total)
    return word_histogram

def unique_words(f):
    for count in range(len(f)):
        count += 1
    return count
