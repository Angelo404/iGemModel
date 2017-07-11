"""
iGemModel
Author: Angelo
File: extract_info_from_xl
Date: 06/07/17
Environment: PyCharm Community Edition
"""

from utils import *

genome = open_file()

data = read_csv()

for entry in data:
    pos = int(entry[0])
    if entry[1] == '-':
        sequence = genome[pos:pos+33]
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
        print new_string
        print entry
    elif entry[1] == '+':
        sequence = genome[pos-30:pos+3]
        print sequence
        print entry

if __name__ == '__main__':
    pass

