# use natural language toolkit
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
stemmer = LancasterStemmer()

# 2 classes of training data
training_data = []
training_data.append({"class":"positive", "sentence":"3M, the maker of Scotch tape and Post-it notes, reported on Tuesday better-than-expected quarterly profit, as the company kept a tight lid on costs."})
training_data.append({"class":"positive", "sentence":"Net income attributable to the company rose to $1.15 billion, or $1.88 per share, in the quarter, from $1.04 billion, or $1.66 per share, a year earlier."})
training_data.append({"class":"positive", "sentence":"Net sales increased 0.4 percent to $7.33 billion."})
training_data.append({"class":"positive", "sentence":"Apple hit an all-time high before posting earnings that disappointed Wall Street."})
training_data.append({"class":"positive", "sentence":"Earns per share were higher than expected at $2.10, compared to $2.02."})
training_data.append({"class":"positive", "sentence":"Apple's iPhone sales have rebounded thanks to better-than-expected demand for the iPhone 7 Plus, executives say."})
training_data.append({"class":"positive", "sentence":"Boosted by the rising tide of record highs in the U.S. markets, Apple hit a record intraday share price Tuesday ahead of its quarterly earnings report after the bell."})
training_data.append({"class":"positive", "sentence":"Boeing shares surged 6 percent Wednesday after it posted fourth-quarter results that solidly beat analyst expectations, with strong performance across the board."})
training_data.append({"class":"positive", "sentence":"The defense and aerospace company gave an upbeat forecast for 2018. Boeing expects to deliver 810 to 815 commercial aircraft this year. That's an increase of at least 47 from last year, when it set a company record of 763."})
training_data.append({"class":"positive", "sentence":"In the quarter ended Dec. 31, Boeing said, its net income nearly doubled to $3.13 billion, or $5.18 per share, from $1.63 billion, or $2.59 per share, a year ago."})
training_data.append({"class":"positive", "sentence":"Fourth-quarter revenue grew to $25.37 billion in 2017, a 9 percent increase from the same period last year."})
training_data.append({"class":"positive", "sentence":"The company says it expects the business is worth at least $2.6 trillion over the next decade as maintenance and parts demand continues to rise for Boeing aircraft."})
training_data.append({"class":"positive", "sentence":"The company's stock has risen 109 percent in the last 12 months, as of Monday's closing price of $340.82 per share."})
training_data.append({"class":"positive", "sentence":"Caterpillar reported first-quarter earnings and revenue on Tuesday that smashed Wall Street's expectations, sending shares sharply higher."})
training_data.append({"class":"positive", "sentence":"Caterpillar's stock was up more than 6 percent in premarket trading following the news."})
training_data.append({"class":"positive", "sentence":" Caterpillar alone will add 40 points to the Dow Jones industrial index for the day."})
training_data.append({"class":"positive", "sentence":"Caterpillar also raised its guidance for full-year earnings to $3.75 per share from $2.90 per share."})
training_data.append({"class":"positive", "sentence":"Parks and resorts: $5.15 billion vs. $4.86 billion expected"})
training_data.append({"class":"positive", "sentence":'''For the studio segment, Iger said during a Tuesday earnings call that ticket presales for "Black Panther" are "outpacing every other superhero movie ever made, driven in part to the phenomenal reaction to the premier last week."'''})
training_data.append({"class":"positive", "sentence":"Iger said Tuesday that the acquisition would help Disney deliver more content, enhance its direct-to-consumer initiatives and diversify the business geographically."})
training_data.append({"class":"positive", "sentence":"Chemicals and seeds producer DuPont, which is merging with Dow Chemical, reported a better-than-expected profit for the seventh straight quarter, helped by a rise in seed sales."})
training_data.append({"class":"positive", "sentence":"Operating earnings at DuPont's agriculture business rose 12 percent to $1.24 billion in the first quarter ended March 31."})
training_data.append({"class":"positive", "sentence":"Net sales rose 4.6 percent to $7.74 billion, beating estimates of $7.50 billion."})
training_data.append({"class":"positive", "sentence":"Home Depot on Tuesday reported fourth-quarter earnings and sales that topped Wall Street's expectations, as more shoppers flocked to its stores and spent more per trip."})
training_data.append({"class":"positive", "sentence":"The home improvement retailer's stock was climbing around 1 percent Tuesday morning on the news."})
training_data.append({"class":"positive", "sentence":"Earnings per share: $1.69, adjusted, vs. $1.61 expected"})
training_data.append({"class":"positive", "sentence":"Revenue: $23.9 billion vs. $23.7 billion expected"})
training_data.append({"class":"positive", "sentence":"Revenue climbed 7.5 percent from a year ago to $23.9 billion"})
training_data.append({"class":"positive", "sentence":"The company said its customer transactions rose 2 percent, while the average ticket increased 5.5 percent (to $64 per person)."})
training_data.append({"class":"positive", "sentence":"Hurricane recovery efforts further boosted Home Depot's revenues, as consumers across the southern parts of the U.S. and Puerto Rico continued to invest in rebuilding homes that were destroyed toward the end of 2017."})
training_data.append({"class":"positive", "sentence":"Coming off a strong year, Home Depot is looking to grow even more in the coming months."})
training_data.append({"class":"positive", "sentence":"The home improvement retailer continues to thrive alongside its rival Lowe's, as their business models are much more difficult to replicate online."})
training_data.append({"class":"positive", "sentence":"Intel beat expectations amid scrutiny surrounding the Meltdown and Spectre security vulnerabilities."})
training_data.append({"class":"positive", "sentence":"Intel stock rose more than 5.5 percent after the company released better-than-expected earnings for the fourth quarter of 2017 on Thursday."})
training_data.append({"class":"positive", "sentence":"And for the full year revenue came in at $62.8 billion, which was up 6 percent."})

training_data.append({"class":"negative", "sentence":"Its market cap slipped to $765 billion during after hours trading due to the poor results."})
training_data.append({"class":"negative", "sentence":"But despite busting record-high share prices, Apple has until now fallen short of its all-time high market capitalization, since market value is determined by stock price multiplied by shares outstanding."})
training_data.append({"class":"negative", "sentence":"The company reported a 20 percent drop in quarterly profit, which was driven lower because of higher costs related to its refranchising efforts in Coca-Cola's North America bottling operations."})
training_data.append({"class":"negative", "sentence":"Aside from the expenses incurred from these efforts, Coke was further dragged down in the first quarter by weakness at its Latin American operations."})
training_data.append({"class":"negative", "sentence":"Coca-Cola's total sales fell 11.3 percent for the quarter, marking its eighth-consecutive quarterly decline in revenue."})
training_data.append({"class":"negative", "sentence":"Coke had warned earlier this year that its 2017 profit would drop as the company works to refranchise its bottling operations."})
training_data.append({"class":"negative", "sentence":"But Disney's other businesses reported revenue that fell short of Wall Street projections."})
training_data.append({"class":"negative", "sentence":"Media and networks: $6.24 billion vs. $6.35 billion expected"})
training_data.append({"class":"negative", "sentence":"Studio: $2.50 billion vs. $2.75 billion expected"})
training_data.append({"class":"negative", "sentence":"Consumer and interactive: $1.45 billion vs. $1.52 billion"})
training_data.append({"class":"negative", "sentence":"Exxon Mobil on Friday reported adjusted quarterly profits that fell far short of Wall Street estimates, though the oil giant posted its strongest annual earnings since 2014."})
training_data.append({"class":"negative", "sentence":"Shares of Exxon plunged about $5 a share, or nearly 6 percent, to below $84."})
training_data.append({"class":"negative", "sentence":'''The company saw corporate and financing expenses rise by $3 billion, mostly due to "unfavorable impacts" of $2.1 billion from U.S. tax reform."'''})
training_data.append({"class":"negative", "sentence":"The stock was up nearly 1 percent in the premarket immediately after the announcement, then turned negative."})
training_data.append({"class":"negative", "sentence":"The stock closed 2 percent lower on Friday."})
training_data.append({"class":"negative", "sentence":"The reported revenue represents a 1 percent decline from a year earlier, hurt by lower sales in its oil and gas and lighting businesses."})
training_data.append({"class":"negative", "sentence":"Goldman Sachs stock fell to its lowest level in nearly five months Tuesday after the premiere Wall Street firm reported first-quarter earnings that missed on the top and bottom lines."})
training_data.append({"class":"negative", "sentence":"Revenue of $8.026 billion vs. $8.446 billion expected by Thomson Reuters analysts' consensus."})
training_data.append({"class":"negative", "sentence":"Equities trading revenue fell 6 percent year over year."})
training_data.append({"class":"negative", "sentence":"Shares skidded 4.5 percent in the first hour of trading, falling to $216.02 at one point before regaining some lost ground"})
training_data.append({"class":"negative", "sentence":'''"Goldman said "significantly" lower net revenues from commodities and currencies offset "significantly" higher net revenues in mortgage products."'''})
training_data.append({"class":"negative", "sentence":"IBM saw its stock go down more than 4.5 percent after it reported better-than-expected earnings for the fourth quarter and full year of 2017 on Thursday."})
training_data.append({"class":"negative", "sentence":"IBM's Technology Services and Cloud Platforms revenue fell 1 percent with $9.2 billion in the quarter."})
training_data.append({"class":"negative", "sentence":"Shares of Johnson & Johnson turned negative as investors reacted to a lackluster sales growth outlook."})
training_data.append({"class":"negative", "sentence":'''"J.P. Morgan analyst Mike Weinstein called the guidance "disappointing" in a note to investors, saying it fell below his expectation of 3.5 percent to 4 percent heading into the release."'''})
training_data.append({"class":"negative", "sentence":"In the fourth quarter, the company reported a net loss of $10.7 billion, or $3.99 per share."})
training_data.append({"class":"negative", "sentence":"Operational sales of diabetes drug Invokana fell 29 percent to $267 million."})
training_data.append({"class":"negative", "sentence":'''""We significantly lower our [same-store sales] expectations due to deteriorating industry conditions and a disappointing early sales impact from the $1, $2, $3 value menu," the firm says."'''})
training_data.append({"class":"negative", "sentence":"McDonald's shares dropped 4.7 percent Friday after the report."})
training_data.append({"class":"negative", "sentence":"Merck on Wednesday reported a 2.5 percent fall in quarterly revenue, hurt by a strong dollar and declining sales of its Remicade arthritis treatment."})
training_data.append({"class":"negative", "sentence":"Merck's stock price dropped more then 2 percent in premarket trading after the release of the earnings report. "})
training_data.append({"class":"negative", "sentence":"Net income fell to $981 million, or 35 cents per share"})
training_data.append({"class":"negative", "sentence":"But the company's shares fell more than 6 percent in after-hours trading."})
training_data.append({"class":"negative", "sentence":"Nike's North America revenue of $3.74 billion was about flat from the prior-year quarter. It missed estimates of $4.01 billion, according to StreetAccount."})
training_data.append({"class":"negative", "sentence":"sales declined 8.2 percent to $1.15 billion,"})


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
classify('''"Snap is still growing faster than Facebook in North America, the most lucrative market for both companies. Snap said late Tuesday its daily average users in the region during the fourth quarter of 2017 rose 5 percent from the prior quarter to 80 million.
Facebook said last week its daily average users in the U.S. and Canada fell slightly from the third quarter, to 184 million. That was the first time Facebook reported such a drop. On a year-over-year basis, Snap grew much faster during the period, with North American DAUs surging 17.7 percent. Meanwhile Facebook's growth was just 2.2 percent on that basis.
The figures suggest that even though Facebook dented Snap's overall growth last year by copying many of its features, including its Stories, Snap finished the year strong.
Snap posted quarterly revenue above expectations, while its loss was less than expected, sending its shares soaring around 20 percent in after-hours trading.
Snap's average revenue per user in North America rose to $2.75 in the fourth quarter from $2.15 a year ago, while its overall ARPU grew even faster, to $1.53 from $1.05."''', show_details=True)
'''
import mysql.connector

cnx = mysql.connector.connect(user='root',password='Jumeirah198', database='articles')
cursor = cnx.cursor()

query = ("SELECT * FROM articles.Article")

cursor.execute(query) 
'''