"""
iGemModel
Author: Angelo
File: Genome
Date: 15/06/17
Environment: PyCharm Community Edition
"""


class Genome(object):
    def __init__(self, sequence, pam):
        self.__seq = sequence
        self.__pam = pam

    @property
    def DNA(self):
        pass

    @DNA.getter
    def DNA(self):
        return self.__seq

    @property
    def __list__(self):
        pass

    @__list__.getter
    def __list__(self):
        return [self.__seq, self.__pam]

    def __str__(self):
        return str(self.__list__)


class VirusGenome(Genome):
    def __init__(self, sequence, pam, pos):
        Genome.__init__(self, sequence, pam)
        self.__pos = pos

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
