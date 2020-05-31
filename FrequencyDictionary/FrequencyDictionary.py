'''
The task:
1. To remove all the stop-words and punctuation from a text file
2. To find the frequency of each word
3. To sort the disctionary of key=a word and value=a frequency in the descending order
4. To find all the capital letters in a text file.
'''

import re

#global files
f_stop_w = 'stop_words.txt' #stop words according to google
#essay samples
essay_1 = 'EssayEx_1.txt'
essay_2 = 'EssayEx_2.txt'

def read_stop_words(l_stopwords=None):

    with open(f_stop_w, 'r') as f:
        l_stopwords = [line.strip() for line in f]

    return l_stopwords

def clean_payload(txt_file, stop_words):
    words = []
    with open(txt_file, 'r') as essay:

        for line in essay:
            for word in line.split(' '):
                if word not in str(stop_words):
                    #removes all the punctuation signs
                    w = re.sub(r'[^\w\s]','',word)
                    w = re.sub(r'\_','',w)
                    words.append(w)

        return words

def highest_frequency_dict(words):
    frequency_dict = dict()

    for word in words:
        #finds the frequence of each word in a text
        frequency_dict.update({word : words.count(word)})

    i = 0
    #sort the dictionary by its values and reverses it, so its descending
    sorted_dict = {k: v for k, v in sorted(frequency_dict.items(),
                    key=lambda item: item[1], reverse=True)}
    print("5 most frequent words are:")
    for key, value in sorted_dict.items():
        print(key)
        i+=1
        if i == 5:
            break

    return sorted_dict

def create_words_frequency_file(file):
    try:
        with open("words_frequency", "w+") as f:
            #stores the frequency of each word in a file
            for key, value in file.items():
                f.write(key + ':' + str(value))
                f.write('\n')
    except IOError as e :
        print(f'The error {e.errno} has occurred')

#should search for the capital words in a text
def find_all_names(text):
    matches = []
    lines = []
    with open(text, 'r') as f:
        lines = [line.split(" ") for line in f]
        for line in lines:
            for word in range(len(line)-1):
                if line[word][0].isupper():
                    matches.append(line[word])

    return matches

def main():
    #returns the list of stop-words
    processor = read_stop_words()
    #returns a list of words from a text file
    text = clean_payload(essay_2, processor)
    #finds the frequency of each word
    frequency_data = highest_frequency_dict(text)
    #creates a file with the frequency of each word
    frequency_file = create_words_frequency_file(frequency_data)
    #finds all the capital letters
    all_capitals = find_all_names(essay_2)
    #5 most frequent words


if __name__ == "__main__":
    main()
