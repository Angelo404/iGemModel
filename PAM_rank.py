"""
iGemModel
Author: Angelo
File: PAM_rank
Date: 05/07/17
Environment: PyCharm Community Edition
"""
import re
from utils import *


class PAM_rank:
    def __init__(self, PAMS):
        self.__ranks = {}
        self.__pams = PAMS

    def scanner(self, genome_seq):
        for pam in self.__pams:
            pam_pos = [_.start() for _ in re.finditer(pam, genome_seq)]
            for possition in pam_pos:
                self.add_to_ranks(genome_seq[possition:possition + 3])
        self.rank()
        print self.__ranks

    def add_to_ranks(self, pam):
        if pam in self.__ranks:
            self.__ranks[pam] = self.__ranks.get(pam)+1
        else:
            self.__ranks[pam] = 1

    def rank(self):
        total = 0
        for entry in self.__ranks:
            total += self.__ranks[entry]
        for entry in self.__ranks:
            self.__ranks[entry] = (self.__ranks.get(entry)*1.0)/(total*1.0)

if __name__ == '__main__':
    data = open_file()
    pam_scanner = PAM_rank(['AGG', 'CGG', 'TGG', 'GGG'])
    pam_scanner.scanner(data)

