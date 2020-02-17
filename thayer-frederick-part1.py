import numpy as np
from collections import Counter
textfile = '/Users/frederickthayer/Documents/NLP/hw2_training_sets_new.txt'
testfile = '/Users/frederickthayer/Documents/NLP/test_set.txt' #mountain, typo fixed
text = open(textfile, 'r')
test = open(testfile, 'r')

print("processing...")

#remove punctuation, capitalization, excess spaces, and split into list of words for counting
token_text = text.read().lower().split() #list of all tokens
token_test = test.read().lower().split()

token_text.insert(0,'<s>')  # append <s> and </s> to sentences

for i in range(len(token_text)*2):
    if i == len(token_text):
        break
    if token_text[i] == '.':
        token_text.insert(i+1,'</s>')
        i = i+2
        token_text.insert(i,'<s>')

token_text.pop(len(token_text)-1)

token_test.insert(0,'<s>')  # append <s> and </s> to sentences

for i in range(len(token_test)*2):
    if i == len(token_test):
        break
    if token_test[i] == '.':
        token_test.insert(i+1,'</s>')
        i = i+2
        token_test.insert(i,'<s>')

token_test.pop(len(token_test)-1)

test_counter = Counter(token_test)   #frequency of each test token
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
print("running test set...")

prob = []
norm = []
perp = []
sentence_break = 0
for i in range(test_counter['</s>']):
    prob.append(1) #probability
    norm.append(1) #probability normalized by sentence length
    perp.append(1) #perplexity
    for j in range(sentence_break,len(token_test)-1):
        first_word = token_test[j]
        second_word = token_test[j+1]
        if vocab_counter[first_word] == 0:
            first_word = '<UNK>'
        if vocab_counter[second_word] == 0:
            second_word = '<UNK>'
        prob[i] = prob[i]*bigram_model[(first_word, second_word)]
        if token_test[j+1] == '</s>':
            norm[i] = prob[i] / len(Counter(token_test[sentence_break:j+1]).keys())
            perp[i] = np.exp(np.log(prob[i])*(1./float(j+1-sentence_break)))
            sentence_break = j+1
            break

#write output
output_file = open('/Users/frederickthayer/Documents/NLP/output.txt','w+')
output_file.write(str(prob[0])+', '+str(norm[0])+', '+str(perp[0])+'\n')
output_file.write(str(prob[1])+', '+str(norm[1])+', '+str(perp[1])+'\n')
output_file.write(str(prob[2])+', '+str(norm[2])+', '+str(perp[2])+'\n')
output_file.write(str(prob[3])+', '+str(norm[3])+', '+str(perp[3])+'\n')
output_file.write(str(prob[4])+', '+str(norm[4])+', '+str(perp[4]))
output_file.close()

print("output file generated")
