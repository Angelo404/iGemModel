"""
iGemModel
Author: Angelo
File: hamming_dist
Date: 06/07/17
Environment: PyCharm Community Edition
"""

from utils import *

def exctrat(entry):
    pos = int(entry[0])
    if entry[1] == '-':
        sequence = genome[pos:pos + 33]
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
    elif entry[1] == '+':
        new_string = genome[pos - 30:pos + 3]
    return new_string


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        pass
        #raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

def compare(data):
    new_data = []
    for idx in range(len(data)):
        for idx2 in range(len(data[idx+1:])):
            hd = hamming_distance(data[idx+1][0], data[idx2][0])
            new_data.append([data[idx+1][0], data[idx2][0], hd,
                             abs(int(data[idx+1][2]) - int(data[idx2][2]))])
    return new_data

if __name__ == '__main__':
    genome = open_file()

    data = read_csv()

    new_data = []

    for entry in data:
        seq_str = exctrat(entry)
        new_data.append([seq_str, entry[1], entry[3]])
    print new_data
    print len(new_data)
    d2_to_csv(new_data)
    # new_new_data = compare(new_data)
    # len(new_new_data)
    # for i in new_new_data:
    #     print i


