"""
iGemModel
Author: Angelo
File: new_comp
Date: 25/07/17
Environment: PyCharm Community Edition
"""
from copy import copy

from Genome import VirusGenome
from utils import *
import time
import CRISPER
from hamming_dist import hamming_distance

c = CRISPER.CRISPER(['AGG', 'TGG', 'CGG', 'GGG'], 33)

sk1_raw = open_file('SK1')
jj50_raw = open_file('jj50')
sk1_raw_neg_comp = open_file('SK1negcompl')
jj50_raw_neg_comp = open_file('jj50negcompl')
lactis = open_file('lactoccocus lactis')
heler_raw = read_csv('data_1501235993.46.csv')
#'TTAAAAAGCCTTTAATATCAGTTGTTACAAAGG', '39', '+', 'AGG', '2']


c.break_genomes([sk1_raw, sk1_raw_neg_comp])
sk1_spacers = c.get_data()
c.clear_data()

c.break_genomes([jj50_raw, jj50_raw_neg_comp])
jj50_spacers = c.get_data()
c.clear_data()

c.break_genomes([lactis])
lactis_spacers = c.get_data()
c.clear_data()

outcsv = open('SK1_heller.csv', 'wb')
writer = csv.writer(outcsv)
writer.writerow(["v_spacer", "heler_spacer", "dist", "v_pos", "h_pos",
                 "hits", "strand", "reads"])

print 'SK1'

for s in sk1_spacers:
    min_dist = 100
    min_seq = ''
    min_heler_seq = ''
    seq_2 = s.get_dna(17,-3)
    for heler_spacer in heler_raw:
        seq_1 = heler_spacer[0][14:-3]
        # print 'heler: ', seq_1
        # print 'virus: ', seq_2
        # time.sleep(0.5)
        heler_to_dist = hamming_distance(seq_1, seq_2)
        if heler_to_dist < min_dist:
            min_h_pos = heler_spacer[1]
            min_pos = s.get_pos()
            min_seq = seq_2
            min_heler_seq = seq_1
            # print 'min heler: ', min_heler_seq
            min_dist = heler_to_dist
            heler_reads = heler_spacer[4]
            heler_str = heler_spacer[2]
    hits = 0
    for l in lactis_spacers:
        lactis_seq = copy(l.get_dna(17,-3))
        if lactis_seq == '': continue
        if hamming_distance(l.get_dna(17,-3), s.get_dna(17,-3)) <= 5:
            hits += 1

    # print 'virus: {} - heler: {} - virus_heler_dist: {} - virus pos: {} - heler pos: {} - hits: {} - stand: {} - reads: {}'.format(
    #         min_seq, min_heler_seq, min_dist, min_pos, min_h_pos, hits, heler_str, heler_reads)
    writer.writerow([min_seq, min_heler_seq, min_dist, min_pos, min_h_pos, hits, heler_str, heler_reads])

outcsv.close()
print 'JJ'
outcsv = open('jj50_heller.csv', 'wb')
writer = csv.writer(outcsv)
writer.writerow(["v_spacer", "heler_spacer", "dist", "v_pos", "h_pos",
                 "hits", "strand", "reads"])

for s in jj50_spacers:
    min_dist = 100
    min_seq = ''
    min_heler_seq = ''
    seq_2 = s.get_dna(17,-3)
    for heler_spacer in heler_raw:
        seq_1 = heler_spacer[0][14:-3]
        heler_to_dist = hamming_distance(seq_1, seq_2)
        if heler_to_dist < min_dist:
            min_h_pos = heler_spacer[1]
            min_pos = s.get_pos()
            min_seq = seq_2
            min_heler_seq = seq_1
            # print 'min heler: ', min_heler_seq
            min_dist = heler_to_dist
            heler_reads = heler_spacer[4]
            heler_str = heler_spacer[2]
    hits = 0
    for l in lactis_spacers:
        lactis_seq = copy(l.get_dna(17, -3))
        if lactis_seq == '': continue

        if hamming_distance(l.get_dna(17,-3), s.get_dna(17,-3)) <= 5:
            hits += 1

    # print 'virus: {} - heler: {} - virus_heler_dist: {} - virus pos: {} - heler pos: {} - hits: {} - stand: {} - reads: {}'.format(
    #         min_seq, min_heler_seq, min_dist, min_pos, min_h_pos, hits, heler_str, heler_reads)
    writer.writerow([min_seq, min_heler_seq, min_dist, min_pos, min_h_pos, hits, heler_str, heler_reads])
if __name__ == '__main__':
    pass

