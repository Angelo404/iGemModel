"""
iGemModel
Author: Angelo
File: count_hits
Date: 25/07/17
Environment: PyCharm Community Edition
"""

from utils import *
import CRISPER
from hamming_dist import hamming_distance

def create_neg(sequence):
    sequence = sequence[::-1]
    new_string = ''
    for c in sequence:
        if c == 'G':
            new_string += 'C'
        elif c == 'C':
            new_string += 'G'
        elif c == 'A':
            new_string += 'T'
        elif c == 'T':
            new_string += 'A'
    return new_string

c = CRISPER.CRISPER(['AGG', 'TGG', 'CGG', 'GGG'], 33)

lib = ['lactoccocus lactis']
v_lib = ['SK1', 'jj50']
spacers = []
v_spacers = []


for _ in lib:
    raw_source = open_file(_)
    c.break_genomes([raw_source])
    tmp_spacers = c.get_data()
    c.clear_data()
    negative_spacers = []
    for spacer in tmp_spacers:
        spacers.append(spacer.DNA[17:-3])
        spacers.append(create_neg(spacer.DNA[17:-3]))


tmp_spacers= []
for _ in v_lib:
    raw_source = open_file(_)
    c.break_genomes([raw_source])
    tmp_spacers = c.get_data()
    c.clear_data()
    negative_spacers = []
    for spacer in tmp_spacers:
        v_spacers.append(spacer.DNA[17:-3])
        v_spacers.append(create_neg(spacer.DNA[17:-3]))

virus = []
rest = []
for spacer in spacers:
    hits = 0
    for v_spacer in v_spacers:
        if hamming_distance(spacer, v_spacer) <= 3:
            hits += 1
    print 'spacer: {}, hits: {}'.format(spacer, hits)