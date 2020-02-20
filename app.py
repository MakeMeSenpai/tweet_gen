from flask import Flask
from histogram import histogram
from sample import sample_by_frequency

app = Flask(__name__)

@app.route('/')
def hello():
    #build a histogram
    my_file = open("./words.txt", "r")
    lines = my_file.readlines()

    word = sample_by_frequency(histogram(lines))
    return str(word)
    

if __name__ == '__main__':
    app.run()