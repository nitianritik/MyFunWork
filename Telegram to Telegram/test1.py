#import libraries
import nltk
import re
import numpy as np

#define tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

#define function to preprocess the text
def preprocess_text(text):
    text = text.lower() 			# convert to lowercase
    text = re.sub(r'[^\w\s]','',text) # remove punctuation
    word_tokens = tokenizer.tokenize(text) # tokenize
    return word_tokens

#define function to build language model
def build_language_model(data, n=3):
    ngrams = {}
    for sentence in data:
        tokens = preprocess_text(sentence)
        for i in range(len(tokens)-n+1):
            key = ' '.join(tokens[i:i+n])
            if key not in ngrams:
                ngrams[key] = []
            ngrams[key].append(tokens[i+n])
    return ngrams

#define function to generate chatgpt like responses
def generate_chatgpt_response(model, text, n=3):
    tokens = preprocess_text(text)
    output_words = tokens[:]
    for i in range(20):
        key = ' '.join(tokens[-n:])
        if key in model:
            next_word = np.random.choice(model[key])
            output_words.append(next_word)
            tokens.append(next_word)
        else:
            break
    response = ' '.join(output_words)
    return response