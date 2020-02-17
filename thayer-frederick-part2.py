import numpy as np
import random
from collections import Counter
textfile = '/Users/frederickthayer/Documents/NLP/hw2_training_sets_new.txt'
text = open(textfile, 'r')

print("processing...")

#remove punctuation, capitalization, excess spaces, and split into list of words for counting
token_text = text.read().lower().split() #list of all tokens
token_text.insert(0,'<s>')  # append <s> and </s> to sentences

for i in range(len(token_text)*2):
    if i == len(token_text):
        break
    if token_text[i] == '.':
        token_text.insert(i+1,'</s>')
        i = i+2
        token_text.insert(i,'<s>')

token_text.pop(len(token_text)-1)

vocab_counter = Counter(token_text)  #frequency of each token before UNK
vocab_keys = list(vocab_counter.keys())     #vocab list
vocab_keys.append('<UNK>')          #add UNK
vocab_size = len(vocab_keys)        #vocab size
vocab_range = range(vocab_size)
token_range = range(len(token_text)-1)
bigram_frequency = {}
bigram_model = {}

print("generating language model...")

for i in vocab_range:
    for j in vocab_range:
        bigram_frequency[(vocab_keys[i],vocab_keys[j])]=1. #start with 1 for smoothing
        bigram_model[(vocab_keys[i],vocab_keys[j])]=0

for i in token_range:
    bigram_frequency[(token_text[i], token_text[i+1])] += 1 #add 1 for every found instance

for i in vocab_range:
    for j in vocab_range:
        bigram_model[(vocab_keys[i],vocab_keys[j])]=bigram_frequency[(vocab_keys[i],vocab_keys[j])]/(vocab_counter[vocab_keys[i]]+vocab_size) #divide by unigram frequency + vocab size

print("language model complete")
print("sampling language model...")

weights = []
sentence = ['<s>']
for i in range(len(bigram_model)):
    print(sentence)
    weights = []
    words = list({k[1] for k, v in bigram_model.items() if k[0]==sentence[i]})
    for j in range(len(words)):
        weights.append(bigram_frequency[(sentence[i],words[j])])
    sentence.append(random.choices(words,weights)[0])
    if random.choices(words,weights) == '</s>':
        break

sample_test = sentence
prob = 1
for j in range(len(sample_test)-1):
    first_word = sample_test[j]
    second_word = sample_test[j+1]
    if vocab_counter[first_word] == 0:
        first_word = '<UNK>'
    if vocab_counter[second_word] == 0:
        second_word = '<UNK>'
    prob = prob*bigram_model[(first_word, second_word)]
    if sample_test[j+1] == '</s>':
        perp = np.exp(np.log(prob)*(1./float(len(sample_test))))
        break

print("final result:")
print(sample_test)
print(perp)
