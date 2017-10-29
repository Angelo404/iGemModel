"""
iGemModel
Author: Angelo
File: best_spacers_script
Date: 19/07/17
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


sequences = []

lib = ['SK1', 'jj50', 'lactoccocus lactis']

for _ in lib:
    raw_source = open_file(_)
    c.break_genomes([raw_source])
    tmp_spacers = c.get_data()
    c.clear_data()
    neg_spacers = []
    spacers = []
    for s in tmp_spacers:
        spacers.append(s.DNA[17:-3])
        neg_spacers.append(create_neg(s.DNA[17:-3]))
    sequences.append({'name': _, 'raw': raw_source, 'spacers': spacers, 'neg_spacers': neg_spacers})

print 'here'
# sk1_raw = open_file('SK1')
# jj50_raw = open_file('jj50')
# lactis = open_file('lactoccocus lactis')
heler_raw = open_file()
c.break_genomes([heler_raw])
heler_spacers = c.get_data()
c.clear_data()
#
# c.break_genomes([sk1_raw])
# sk1_spacers = c.get_data()
# c.clear_data()
#
# c.break_genomes([jj50_raw])
# jj50_spacers = c.get_data()
# c.clear_data()
#
print 'here'
#
# heler_sk1_dist = 0
# heler_jj50_dist = 0
#
# print 'heler len {}'.format(len(heler_spacers))
# print 'sk1 len {}'.format(len(sk1_spacers))
# print 'jj50 len {}'.format(len(jj50_spacers))

# heler_sk1_count = 0
# heler_jj50_count = 0

for seq in sequences:
    print seq['name']
    with open('{}.csv'.format(seq['name']), 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([seq['name'], 'heler', 'dist', '{}_pos'.format(seq['name']), 'heler_pos'])

        for spacer in seq['spacers']:
            min_dist = 100
            min_seq = ''
            min_heler_seq = ''
            seq_2 = spacer.DNA[17:-3]
            for heler_spacer in heler_spacers:
                seq_1 = heler_spacer.DNA[17:-3]
                heler_to_dist = hamming_distance(seq_1, seq_2)
                if heler_to_dist < min_dist:
                    min_h_pos = heler_spacer.get_pos()
                    min_pos = spacer.get_pos()
                    min_seq = seq_2
                    min_heler_seq = seq_1
                    min_dist = heler_to_dist
            writer.writerow([min_seq, min_heler_seq, min_dist, min_pos, min_h_pos])
                # print '{}: {} - heler: {} - dist: {} - heler_pos: {} - {}_pos: {}'.format(
                #     seq['name'], min_seq, min_heler_seq, min_dist, min_h_pos, seq['name'], min_pos)


print 'start neg'

for seq in sequences:
    print seq['name']
    with open('{}_negative.csv'.format(seq['name']), 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([seq['name'], 'heler', 'dist', '{}_pos'.format(seq['name']), 'heler_pos'])

        for spacer in seq['spacers']:
            min_dist = 100
            min_seq = ''
            min_heler_seq = ''
            seq_2 = create_neg(spacer.DNA[17:-3])
            for heler_spacer in heler_spacers:
                seq_1 = heler_spacer.DNA[17:-3]
                heler_to_dist = hamming_distance(seq_1, seq_2)
                if heler_to_dist < min_dist:
                    min_h_pos = heler_spacer.get_pos()
                    min_pos = spacer.get_pos()
                    min_seq = seq_2
                    min_heler_seq = seq_1
                    min_dist = heler_to_dist
            writer.writerow([min_seq, min_heler_seq, min_dist, min_pos, min_h_pos])
                # print '{}: {} - heler: {} - dist: {} - heler_pos: {} - {}_pos: {}'.format(
                #     seq['name'], min_seq, min_heler_seq, min_dist, min_h_pos, seq['name'], min_pos)


exit()
