"""
iGemModel
Author: Angelo
File: utils
Date: 05/07/17
Environment: PyCharm Community Edition
"""
import csv
from time import time


def write_to_file(genome, f='allAvirus4'):
    with open(f, 'w') as data:
        data.write(genome)

def open_file(f='seq'):
    s = ''
    with open(f, 'r') as data:
        for l in data.readlines():
            s += l.rstrip()
    return s


def d2_to_csv(d2_data):
    with open('data_'+str(time())+'.csv', 'wb') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        for d in d2_data:
            w.writerow([d[0], d[1], d[2]])


def read_csv(f='main.csv'):
    with open(f, 'r') as csvfile:
        reader = csv.reader(csvfile)
        your_list = list(reader)
        return your_list[1:]

def crop_seq(seq,start=10,end=-3):
    return seq[len(seq)-start+end:end]

def write_to_fasta(file_name, id, seq):
    with open(file_name, "a") as f:
        f.write('>{}\n'.format(id))
        f.write('{}\n'.format(seq))


def reverse_file(file_name):
    s = ''
    with open(file_name, "r") as f_in:

        for l in f_in.readlines():
            s += l.rstrip()

    with open(file_name+'neg', "w") as f_out:
        f_out.write(s[::-1])

def complement(file_name):
    s = ''
    new_string = ''
    with open(file_name, "r") as f_in:
        for l in f_in.readlines():
            s += l.rstrip()

    with open(file_name + 'compl', "w") as f_out:
        for c in s:
            if c == 'G':
                new_string += 'C'
            elif c == 'C':
                new_string += 'G'
            elif c == 'A':
                new_string += 'T'
            elif c == 'T':
                new_string += 'A'
        f_out.write(new_string)

if __name__ == '__main__':
    complement('jj50neg')
    complement('SK1neg')