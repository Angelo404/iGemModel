"""
iGemModel
Author: Angelo
File: CRISPER
Date: 15/06/17
Environment: PyCharm Community Edition
"""

import re
from Genome import VirusGenome
from utils import *


class CRISPER():
    def __init__(self, break_points, seq_len):
        """

        :param break_points: list(str)
        :param seq_len: (int)
        """
        self.__bps = break_points
        self.__sl = seq_len

    def break_genome(self, genome_seq):
        """
        This will take a genome sequence and break it down where the spacers are.
        :param genome_seq: str
        :return: list(object)
        """
        genomes = []
        for bp in self.__bps:
            separators = [_.start() for _ in re.finditer(bp, genome_seq)]
            for separator in separators:
                spacer = genome_seq[separator - self.__sl:separator + len(bp)]
                genomes.append(VirusGenome(spacer, bp, separator))

        return genomes

    def break_genomes(self, genome_seq):
        """
        This will take as input all the genomes available and pass them to the break down function to extract
        all the necessary parts.
        :param genomes: list(str)
        :return: list(list(object))
        """
        for g in genome_seq:
            tmp_genome = self.break_genome(g)
            for s in tmp_genome:
                print s


if __name__ == '__main__':
    c = CRISPER(['AGG', 'TGG', 'CGG', 'GGG',
                 'AGA', 'AGC', 'AGT'], 33)
    data = open_file()
    print data
    c.break_genomes([data])
