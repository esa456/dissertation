# This Python file uses the following encoding: utf-8
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords

example_text = """Shares of sports retailers soared on Friday after Foot Locker, Shoe Carnival, and Hibbett Sports reported better-than-expected quarterly profits. 
Foot Locker, up 22 percent, was the most actively traded among stocks listed on the New York Stock Exchange. Brokerages including Jefferies and Wedbush raised their price targets on Shoe Carnivals shares by $2 to $22 and $27,  
respectively, as they expect improved performance in 2018. It is clear to us the SCVL team is managing its business exceptionally well. 
SCVLs willingness to plan purchases appropriately (boots are planned down 10 percent for the season) resulted in inventory levels down 4.3 percent on a per-store basis at 3Q17-end, Susquehanna analyst Sam Poser said. 
The strong results come as bankruptcies of peers such as Sports Authority, Sports Chalet and changing shopping habits of consumers in favor of e-commerce websites have forced sporting goods retailers to slash prices to clear out the excess stockpile of inventory. 
Further, sporting goods makers such as Nike are also entering direct partnerships with Amazon that might further pressure the brick and mortar retailers to mark down the prices of its products. Shoe Carnival and Hibbett raised their full-year comparable store sales forecasts. 
Shoe Carnivals third-quarter same-store sales jumped 4.4 percent, much higher than the 0.4 percent increase in the second quarter."""

stop_words = set(stopwords.words("english")) #stop words are filler words which are no use within the text in terms of NLP
words = word_tokenize(example_text)
filtered_text = [w for w in words if not w in stop_words]
print(example_text)

#all_words = []
#for w in example_text.words():
#    all_words.append(w.lower())


