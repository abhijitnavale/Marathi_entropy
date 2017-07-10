# -*- coding: utf-8 -*-
import re, random, math, textwrap, codecs
from collections import defaultdict, deque, Counter

import codecs, collections, sys, unicodedata, string, numpy as np, pylab as pl
import sys
import pickle


with open('lets_7.pickle','rb') as f:
    let60, let65, let70, let75, let80, let85, let90, let95 = pickle.load(f)

def replace_box(filename, frac = 0.6):
    """Reads file 'filename', seperates characters, returns a list of separated L_r U \u2610 (box) characters in the text. Does not return Roman letters, numbers, punctuation marks, spaces etc. frac = 0.6 is the default r value used.

    A small part of is this function from a Stackoverflow answer https://stackoverflow.com/a/6806203/3638137 and then modified."""
    try:
        accepted_chars = globals()['let{0:02d}'.format(int(frac*100))]
    except KeyError:

        print 'Fraction should be one of 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95'
        exit() 

    with codecs.open(filename, 'r', 'utf-8') as f:
        s = f.read()
    virama = u'\N{DEVANAGARI SIGN VIRAMA}'
    cluster = u'' 
    last = None
    oplist = []
    for i,c in enumerate(s):
        cat = unicodedata.category(c)[0]
        if cat == 'M' or cat == 'L' and last == virama:    
        # Adding this character to previous character as a letter, if this character is a vowel OR this character is a consonant and previous character was halanta

            cluster += c
        else:
            if cluster:
                try:
                    if unicodedata.name(cluster[0])[0] == 'D':
                    # Ensuring that only Devanagari characters are counted.
                        if cluster in accepted_chars:
                            oplist.append(cluster)
                        else:
                            oplist.append(u'\u2610')
                        
                    #else:
                    #    oplist.append(cluster) 
                except ValueError:
                # Using this because 'unicodedata' is not complete and some characters don't have their info in that module.
                   #oplist.append(cluster) 
                   pass
            cluster = c 
        last = c 
    if cluster:
        try:
            if unicodedata.name(cluster[0])[0] == 'D':
                if cluster in accepted_chars:
                    oplist.append(cluster)
                else:
                    oplist.append(u'\u2610')
            #else:
            #    oplist.append(cluster) 
        except ValueError:
           #oplist.append(cluster) 
           pass
    #opstring = "".join(oplist)
    return oplist

#def tokenize(file_path, tokenizer):
#    with codecs.open(file_path, mode="r", encoding="utf-8") as file:
#        for line in file:
#            for token in tokenizer(line.lower().strip()):
#	        yield token
				
#def chars(file_path):
#	return tokenize(file_path, lambda s: s + " ")
#	
#def words(file_path):
#	return tokenize(file_path, lambda s: re.findall(r"[a-zA-Z']+", s))

def markov_model(stream, model_order):
    """Stream is a list of character and model_order is n, when you want to calculate conditional entropy of having x_{n+1} as next character when you are given x_1, x_2, ..., x_n.
    This function returns model and stats. stats is a dictionary counter giving counts of occurences of each n-character group. model is a dictionary which gives number of occurences of n+1th character for given n character group in variable stats."""
    model, stats = defaultdict(Counter), Counter()
    circular_buffer = deque(maxlen = model_order)
    for token in stream:
        #print 'token',token
        prefix = tuple(circular_buffer)
        circular_buffer.append(token)
        #print 'prefix', prefix
        #print 'circular_buffer', circular_buffer
        if len(prefix) == model_order:
            #print 'adding to stats and model'
            stats[prefix] += 1
            model[prefix][token] += 1
    return model, stats

def entropy(stats, normalization_factor):
    """Mainly used as an internal fuction."""
    return -sum(float(proba) / normalization_factor * np.log2(float(proba) / normalization_factor) for proba in stats.values())

def entropy_rate(model, stats):
    """Returns entropy rate when model and stats are provided as inputs."""
    return sum(stats[prefix] * entropy(model[prefix], stats[prefix]) for prefix in stats) / sum(stats.values())

def entropy_from_file(filename,fraction = 0.6, model_order = 1):
    """Calculates entropy for a given filename, r and model_order."""
    model, stats = markov_model(replace_box(filename, fraction), model_order)
    er = entropy_rate(model, stats)
    print er
    return er 

#model, stats = markov_model(replace_box('ed.txt',0.8), 2)
#print("Entropy rate:", entropy_rate(model, stats))

def pick(counter):
    sample, accumulator = None, 0
    for key, count in counter.items():
        accumulator += count
        if random.randint(0, accumulator - 1) < count:
            sample = key
    return sample
	
def generate(model, state, length):
    for token_id in range(0, length):
        yield state[0]
        state = state[1:] + (pick(model[state]), ) 

#print(textwrap.fill("".join(generate(model, pick(stats), 300))))

# Copyright (C) 2013, Clément Pit--Claudel (http://pit-claudel.fr/clement/blog)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of 
# this software and associated documentation files (the "Software"), to deal in 
# the Software without restriction, including without limitation the rights to 
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<<<<<<< Updated upstream
# Updated by Mihir Kulkarni.
=======
#
>>>>>>> Stashed changes
