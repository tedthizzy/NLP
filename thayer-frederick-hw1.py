import string
from collections import Counter
textfile = '/Users/frederickthayer/Documents/NLP/hw1_training_sets.txt'
text = open(textfile, 'r')

#remove punctuation, capitalization, excess spaces, and split into list of words for counting
cleaned_text = text.read().replace( ",", "" ).replace( ".", "" ).replace( "/", "" ).replace( "@", "" ).replace( "-", "" ).replace( "(", "" ).replace( ")", "" ).replace( ":", "" ).replace( ";", "" ).replace( "!", "" ).replace( "$", "" ).replace( ".", "" ).replace( "%", "" ).replace( "  ", " ").lower()
token_count = len(cleaned_text.split())
type_count = len(Counter(cleaned_text.split()).keys())

#find most common element in array, count instances of that element
mode1 = max(set(cleaned_text.split()), key=cleaned_text.split().count)
freq1 = Counter(cleaned_text.split())[mode1]

#find the next most common element in array, count instances of that element x4
mode2_text = cleaned_text.replace( "the", "" )
mode2 = max(set(mode2_text.split()), key=mode2_text.split().count)
freq2 = Counter(cleaned_text.split())[mode2]

mode3_text = mode2_text.replace( "to", "" )
mode3 = max(set(mode3_text.split()), key=mode3_text.split().count)
freq3 = Counter(cleaned_text.split())[mode3]

mode4_text = mode3_text.replace( "and", "" )
mode4 = max(set(mode4_text.split()), key=mode4_text.split().count)
freq4 = Counter(cleaned_text.split())[mode4]

mode5_text = mode4_text.replace( "he", "" )
mode5 = max(set(mode5_text.split()), key=mode5_text.split().count)
freq5 = Counter(cleaned_text.split())[mode5]

#write output
output_file = open('/Users/frederickthayer/Documents/NLP/output.txt','w+')
output_file.write(str(token_count)+'\n')
output_file.write(str(type_count)+'\n')
output_file.write('\n')
output_file.write(str(mode1) + " " + str(freq1) + '\n')
output_file.write(str(mode2) + " " + str(freq2) + '\n')
output_file.write(str(mode3) + " " + str(freq3) + '\n')
output_file.write(str(mode4) + " " + str(freq4) + '\n')
output_file.write(str(mode5) + " " + str(freq5))
output_file.close()
