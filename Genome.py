"""
iGemModel
Author: Angelo
File: Genome
Date: 15/06/17
Environment: PyCharm Community Edition
"""
from hamming_dist import hamming_distance

class Genome(object):
    def __init__(self, sequence, pam):
        self.__seq = sequence
        self.__pam = pam

    def get_dna(self, start=0, end=-1):
        return self.__seq[start:end]

    def get_spacer_wout_pam(self):
        return self.__seq[:-3]

    @property
    def __list__(self):
        pass

    @__list__.getter
    def __list__(self):
        return [self.__seq, self.__pam]

    def __str__(self):
        return str(self.__list__)

    def cmp(self, other):
        return hamming_distance(self.get_dna(), other.get_dna())

class VirusGenome(Genome):
    def __init__(self, sequence, pam, pos):
        Genome.__init__(self, sequence, pam)
        self.__pos = pos
        self.__pam = pam

    def get_pos(self):
        return self.__pos

    def get_pam(self):
        return self.__pam

    def __str__(self):
        l = self.__list__
        l.append(self.__pos)
        return str(l)


if __name__ == '__main__':
    g = VirusGenome('asdf')
    print g.DNA
    print g.DNA
    print g.length
    print g.__list__
