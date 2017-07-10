# -*- coding: utf-8 -*-
import codecs, collections, sys, unicodedata, string, numpy as np, pylab as pl
import sys
import pickle

reload(sys)
sys.setdefaultencoding('utf-8')

with open('lets_7.pickle','rb') as f:
    let60, let65, let70, let75, let80, let85, let90, let95 = pickle.load(f)

#accepted_chars = [u'भ',u'त', u'र',u'कु']


def replace_box(s, frac = 0.6):
    """Generate the grapheme clusters for the string s. (Not the full
    Unicode text segmentation algorithm, but probably good enough for
    Devanagari.)

    Copied this function from a Stackoverflow answer https://stackoverflow.com/a/6806203/3638137 and modified a bit.

    """
    try:
        accepted_chars = globals()['let{0:02d}'.format(int(frac*100))]
    except KeyError:

        print 'Fraction should be one of 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95'
        exit() 
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
                        
                    else:
                        oplist.append(cluster) 
                except ValueError:
                # Using this because 'unicodedata' is not complete and some characters don't have their info in that module.
                   oplist.append(cluster) 
            cluster = c 
        last = c 
    if cluster:
        try:
            if unicodedata.name(cluster[0])[0] == 'D':
                if cluster in accepted_chars:
                    oplist.append(cluster)
                else:
                    oplist.append(u'\u2610')
            else:
                oplist.append(cluster) 
        except ValueError:
           oplist.append(cluster) 
    opstring = "".join(oplist)
    return opstring


f = codecs.open(sys.argv[1], 'r', 'utf-8')
text = f.read()
f.close()
optext = replace_box(text, frac = float(sys.argv[2]))
f = codecs.open('box_'+sys.argv[2]+'_'+sys.argv[1], 'w', 'utf-8')
f.write(optext)
f.close()

