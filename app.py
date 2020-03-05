from flask import Flask
from markov import *
from histogram import histogram
from sample import sample_by_frequency

app = Flask(__name__)

@app.route('/')
def markov():
    return 

@app.route('/sample')
def sample():
    return ' '.join(sample_by_frequency(15)) #runs our program giving us 15 random words
    
if __name__ == '__main__':
    app.run()