"""
iGemModel
Author: Angelo
File: utils
Date: 05/07/17
Environment: PyCharm Community Edition
"""
import csv
from time import time


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

if __name__ == '__main__':
    test = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    print crop_seq(test)