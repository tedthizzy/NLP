import string
from collections import Counter
textfile = '/Users/frederickthayer/Documents/NLP/hw2_training_sets_new.txt'
text = open(textfile, 'r')

#remove punctuation, capitalization, excess spaces, and split into list of words for counting
token_text = text.read().lower().split() #list of all tokens
token_count = range(len(token_text))
# vocab_text = list(Counter(token_text).keys())
vocab_counter = Counter(token_text)  #frequency of each token before UNK
vocab_keys = list(vocab_counter.keys())     #vocab list
vocab_keys.append('<UNK>')          #add UNK
vocab_size = len(vocab_keys)        #vocab size
vocab_range = range(vocab_size)
token_range = range(len(token_text)-1)
bigram_frequency = {}

for i in vocab_range:
    for j in vocab_range:
        bigram_frequency[(vocab_keys[i],vocab_keys[j])]=1. #start with 1


for i in token_range:
    bigram_frequency[(token_text[i], token_text[i+1])] += 1


for i in vocab_range:
    for j in vocab_range:
        bigram_frequency[(vocab_keys[i],vocab_keys[j])]=bigram_frequency[(vocab_keys[i],vocab_keys[j])]/(vocab_counter[vocab_keys[i]]+vocab_size) #divide by unigram frequency + vocab size
    print(i)

print("DONE!")
print(len(bigram_frequency))


for i in range(len(bigram_frequency)):
    bigram_frequency[(token_text[i], token_text[i+1])] = bigram_frequency[(token_text[i], token_text[i+1])]








prob_arr = [[0 for n in vocab_range] for m in vocab_range]

i_word = ""
j_word = ""

#probability of word given previous word by counting # of times they occur together divided by the number of times only the previous word occurs

for i in vocab_range:
    print("======================================")
    print(i)
    print("======================================")
    i_word = vocab_text[i]
    for j in vocab_range:
        print(j)
        j_word = vocab_text[j]
        for k in token_count:
            if token_text[k] == i_word:
                if token_text[k+1] == j_word:
                    prob_arr[i][j] = prob_arr[i][j] + 1

#find most common element in array, count instances of that element
# mode1 = max(set(cleaned_text.split()), key=cleaned_text.split().count)
# freq1 = Counter(cleaned_text.split())[mode1]
#
# #find the next most common element in array, count instances of that element x4
# mode2_text = cleaned_text.replace( "the", "" )
# mode2 = max(set(mode2_text.split()), key=mode2_text.split().count)
# freq2 = Counter(cleaned_text.split())[mode2]

#write output
# output_file = open('/Users/frederickthayer/Documents/NLP/output2.txt','w+')
# output_file.write(str(token_count)+'\n')
# output_file.close()
