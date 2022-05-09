# use natural language toolkit
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
stemmer = LancasterStemmer()

# 2 classes of training data
training_data = []
training_data.append({"class":"positive", "sentence":"better-than-expected"})
training_data.append({"class":"positive", "sentence":"rose to"})
training_data.append({"class":"positive", "sentence":"increased"})
training_data.append({"class":"positive", "sentence":"hit an all-time high"})
training_data.append({"class":"positive", "sentence":"higher than expected"})
training_data.append({"class":"positive", "sentence":"sales have rebounded thanks to better-than-expected demand"})
training_data.append({"class":"positive", "sentence":"Boosted by the rising tide of record highs, Apple hit a record intraday share price"})
training_data.append({"class":"positive", "sentence":"shares surged"})
training_data.append({"class":"positive", "sentence":"with strong performance across the board."})
training_data.append({"class":"positive", "sentence":" upbeat forecast for 2018."})
training_data.append({"class":"positive", "sentence":"doubled"})
training_data.append({"class":"positive", "sentence":"grew"})
training_data.append({"class":"positive", "sentence":"increase"})
training_data.append({"class":"positive", "sentence":" demand continues to rise"})
training_data.append({"class":"positive", "sentence":"stock has risen "})
training_data.append({"class":"positive", "sentence":"smashed Wall Street's expectations, sending shares sharply higher."})
training_data.append({"class":"positive", "sentence":"stock was up more than 6 percent in premarket trading"})
training_data.append({"class":"positive", "sentence":" will add 40 points to the Dow Jones industrial index for the day."})
training_data.append({"class":"positive", "sentence":" raised its guidance"})
training_data.append({"class":"positive", "sentence":"Parks and resorts: $5.15 billion vs. $4.86 billion expected"})
training_data.append({"class":"positive", "sentence":'''"outpacing every other superhero movie ever made, driven in part to the phenomenal reaction to the premier last week."'''})
training_data.append({"class":"positive", "sentence":"enhance its direct-to-consumer initiatives"})
training_data.append({"class":"positive", "sentence":"rise"})
training_data.append({"class":"positive", "sentence":"rose"})
training_data.append({"class":"positive", "sentence":"beating estimates"})
training_data.append({"class":"positive", "sentence":"earnings and sales that topped Wall Street's expectations"})
training_data.append({"class":"positive", "sentence":"stock was climbing"})
training_data.append({"class":"positive", "sentence":"Earnings per share: $1.69, adjusted, vs. $1.61 expected"})
training_data.append({"class":"positive", "sentence":"Revenue: $23.9 billion vs. $23.7 billion expected"})
training_data.append({"class":"positive", "sentence":"Revenue climbed 7.5 percent from a year ago to $23.9 billion"})
training_data.append({"class":"positive", "sentence":"increased"})
training_data.append({"class":"positive", "sentence":"further boosted"})
training_data.append({"class":"positive", "sentence":"to grow even more"})
training_data.append({"class":"positive", "sentence":"continues to thrive "})
training_data.append({"class":"positive", "sentence":"Intel beat expectations "})
training_data.append({"class":"positive", "sentence":"stock rose more than"})
training_data.append({"class":"positive", "sentence":"was up 6 percent."})

training_data.append({"class":"negative", "sentence":"Its market cap slipped "})
training_data.append({"class":"negative", "sentence":"fallen short"})
training_data.append({"class":"negative", "sentence":"percent drop in quarterly profit, which was driven lower because of higher costs "})
training_data.append({"class":"negative", "sentence":"further dragged down"})
training_data.append({"class":"negative", "sentence":"total sales fell"})
training_data.append({"class":"negative", "sentence":"drop"})
training_data.append({"class":"negative", "sentence":"fell short of Wall Street projections."})
training_data.append({"class":"negative", "sentence":"Media and networks: $6.24 billion vs. $6.35 billion expected"})
training_data.append({"class":"negative", "sentence":"Studio: $2.50 billion vs. $2.75 billion expected"})
training_data.append({"class":"negative", "sentence":"Consumer and interactive: $1.45 billion vs. $1.52 billion"})
training_data.append({"class":"negative", "sentence":"fell far short of Wall Street estimates"})
training_data.append({"class":"negative", "sentence":"plunged"})
training_data.append({"class":"negative", "sentence":"unfavorable impacts"})
training_data.append({"class":"negative", "sentence":"turned negative."})
training_data.append({"class":"negative", "sentence":"lower"})
training_data.append({"class":"negative", "sentence":"decline"})
training_data.append({"class":"negative", "sentence":" stock fell to its lowest level"})
training_data.append({"class":"negative", "sentence":"Revenue of $8.026 billion vs. $8.446 billion expected by Thomson Reuters analysts' consensus."})
training_data.append({"class":"negative", "sentence":"Equities trading revenue fell 6 percent year over year."})
training_data.append({"class":"negative", "sentence":"Shares skidded"})
training_data.append({"class":"negative", "sentence":'''""significantly" lower net revenues"'''})
training_data.append({"class":"negative", "sentence":"stock go down more than 4.5 percent"})
training_data.append({"class":"negative", "sentence":"revenue fell"})
training_data.append({"class":"negative", "sentence":"turned negative"})
training_data.append({"class":"negative", "sentence":"disappointing"})
training_data.append({"class":"negative", "sentence":"net loss"})
training_data.append({"class":"negative", "sentence":"deteriorating"})
training_data.append({"class":"negative", "sentence":"lower"})
training_data.append({"class":"negative", "sentence":"McDonald's shares dropped 4.7 percent Friday after the report."})
training_data.append({"class":"negative", "sentence":"hurt by a strong dollar and declining sales."})
training_data.append({"class":"negative", "sentence":"stock price dropped more than"})
training_data.append({"class":"negative", "sentence":"Net income fell"})
training_data.append({"class":"negative", "sentence":"It missed estimates of $4.01 billion"})
training_data.append({"class":"negative", "sentence":"sales declined"})


print ("%s sentences in training data" % len(training_data))

words = []
classes = []
documents = []
ignore_words = ['?']
# loop through each sentence in our training data
for pattern in training_data:
    # tokenize each word in the sentence
    w = nltk.word_tokenize(pattern['sentence'])
    # add to our words list
    words.extend(w)
    # add to documents in our corpus
    documents.append((w, pattern['class']))
    # add to our classes list
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = list(set(words))

# remove duplicates
classes = list(set(classes))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)

# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    training.append(bag)
    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)

# sample training/output
i = 0
w = documents[i][0]
print ([stemmer.stem(word.lower()) for word in w])
print (training[i])
print (output[i])

import numpy as np
import time

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)
 
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

def think(sentence, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # input layer is our bag of words
    l0 = x
    # matrix multiplication of input and hidden layer
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2

def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5):

    print ("Training with %s neurons, alpha:%s, dropout:%s %s" % (hidden_neurons, str(alpha), dropout, dropout_percent if dropout else '') )
    print ("Input matrix: %sx%s    Output matrix: %sx%s" % (len(X),len(X[0]),1, len(classes)) )
    np.random.seed(1)

    last_mean_error = 1
    # randomly initialize our weights with mean 0
    synapse_0 = 2*np.random.random((len(X[0]), hidden_neurons)) - 1
    synapse_1 = 2*np.random.random((hidden_neurons, len(classes))) - 1

    prev_synapse_0_weight_update = np.zeros_like(synapse_0)
    prev_synapse_1_weight_update = np.zeros_like(synapse_1)

    synapse_0_direction_count = np.zeros_like(synapse_0)
    synapse_1_direction_count = np.zeros_like(synapse_1)
        
    for j in iter(range(epochs+1)):

        # Feed forward through layers 0, 1, and 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))
                
        if(dropout):
            layer_1 *= np.random.binomial([np.ones((len(X),hidden_neurons))],1-dropout_percent)[0] * (1.0/(1-dropout_percent))

        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # how much did we miss the target value?
        layer_2_error = y - layer_2

        if (j% 10000) == 0 and j > 5000:
            # if this 10k iteration's error is greater than the last iteration, break out
            if np.mean(np.abs(layer_2_error)) < last_mean_error:
                print ("delta after "+str(j)+" iterations:" + str(np.mean(np.abs(layer_2_error))) )
                last_mean_error = np.mean(np.abs(layer_2_error))
            else:
                print ("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error )
                break
                
        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
        
        synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
        synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))
        
        if(j > 0):
            synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0)+0) - ((prev_synapse_0_weight_update > 0) + 0))
            synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0)+0) - ((prev_synapse_1_weight_update > 0) + 0))        
        
        synapse_1 += alpha * synapse_1_weight_update
        synapse_0 += alpha * synapse_0_weight_update
        
        prev_synapse_0_weight_update = synapse_0_weight_update
        prev_synapse_1_weight_update = synapse_1_weight_update

    now = datetime.datetime.now()

    # persist synapses
    synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
               'datetime': now.strftime("%Y-%m-%d %H:%M"),
               'words': words,
               'classes': classes
              }
    synapse_file = "synapses.json"

    with open(synapse_file, 'w') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)
    print ("saved synapses to:", synapse_file)

X = np.array(training)
y = np.array(output)

start_time = time.time()

train(X, y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)

elapsed_time = time.time() - start_time
print ("processing time:", elapsed_time, "seconds")

# probability threshold
ERROR_THRESHOLD = 0.2
# load our calculated synapse values
synapse_file = 'synapses.json' 
with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])

def classify(sentence, show_details=False):
    results = think(sentence, show_details)

    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_results =[[classes[r[0]],r[1]] for r in results]
    print ("%s \n classification: %s" % (sentence, return_results))
    return return_results

'''classify("Coach's profit jumps 8.6% topping Street Views, on less discounting")
classify("Amazon surges on big earnings and sales beat")
classify("Apple sells Iphones")
classify("who are you?")
classify("make me some lunch")
classify("how was your lunch today?")'''
print()
classify('''"U.S. chemicals producer DowDuPoint reported a 14 percent rise in net sales for the fourth quarter and beat Wall Street profit estimates as a strong global economy led to robust demand and higher prices for its products.

The newly-combined company, formed by the merger of chemical giants Dow Chemical and DuPont four months ago, said its net sales came in at $20.1 billion versus comparable net sales — which the company terms "proforma" sales — of $17.7 billion a year earlier.

It also said it planned to move ahead with plans to split the new company into three separate parts, starting with the Materials Science unit by the end of the first quarter of 2019. Agriculture and Specialty Products are expected to follow by June 1, 2019.

The chemicals giant saw prices rise by about 5 percent across markets in the fourth quarter, while volumes — a proxy for demand — rose 6 percent.

"In developed economies in particular, such as the United States, Germany, France, Canada and the U.K., we continue to see strong leading indicators of broad-based growth," executive chairman Andrew Liveris said in the results statement.

"Furthermore, early signs from the business community point to U.S. tax reform as a catalyst for further domestic capital investments."

Currently trading at a market value of about $176.9 billion, Dow and DuPont completed the $130 billion mega-merger in September. That created the world's largest chemical maker, until the company goes through with a plan to split into three companies.

DowDuPont's merger was welcomed by investors as a way to streamline the companies' sprawling operations by combining overlapping businesses.

The company said on Thursday it was now planning to save $3.3 billion in costs on the back of the merger — slightly more than the $3 billion it expected to save earlier.

For the reported quarter DowDuPont saw a $1.1 billion benefit from lower U.S corporate taxes, but still posted a net loss of $1.2 billion from continuing operations — substantially the result of merger-related costs.

Adjusted for those and other one-time effects, the company said it earned 83 cents on a share. Ahead of the numbers, Wall Street was expecting it to make 67 cents a share, according to Thomson Reuters I/B/E/S numbers.

Shares of the company dipped to $75 in premarket trading on Thursday compared to the previous close of $75.58."''', show_details=True)
'''
import mysql.connector

cnx = mysql.connector.connect(user='root',password='Jumeirah198', database='articles')
cursor = cnx.cursor()

query = ("SELECT * FROM articles.Article")

cursor.execute(query) 
'''