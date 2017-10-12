"""
iGemModel
Author: Angelo
File: genetic_algo
Date: 28/07/17
Environment: PyCharm Community Edition
"""
import random

from math import sqrt

import CRISPER
import utils
from utils import *


class Agent():
    def __init__(self, spacers, mode = 1):
        """
        Model: [['spacer', {'virus1': ham_dist, 'virus2': ham_dist, ...}], ['spacer', {'virus1': ham_dist, ...}], ...]
        :param virus_name:
        :param spacers:
        """
        self.__spacers = []
        if mode == 1:
            for spacer in spacers:
                self.__spacers.append([spacer])
        else:
            for spacer in spacers:
                self.__spacers.append(spacer)

        self.__total_fitness = 0

    @property
    def fitness(self):
        return self.__total_fitness

    def add_virus(self, virus_name):
        for native_spacer in self.__spacers:
            if len(native_spacer) > 1:
                native_spacer[1][virus_name] = 0
            else:
                native_spacer.append({virus_name: 0})

    def get_random_spacers(self, num_of_spacers):
        return random.sample(self.__spacers, num_of_spacers)

    def compute_similarity(self, other_spacers):
        similarity = []
        self.__total_fitness = 0
        for spacer in self.__spacers:
            min_dist = 100
            for s in other_spacers:
                d = hamming_distance(spacer[0].get_dna(), s.get_dna())
                if d < min_dist:
                    min_dist = d
            similarity.append(min_dist)

        virus_names = self.__spacers[0][1].keys()
        virus_vectors = []

        for virus_name in virus_names:
            tmp_vctr = []
            for spacer in self.__spacers:
                tmp_vctr.append(spacer[1][virus_name])
            virus_vectors.append(tmp_vctr)

        # print similarity
        for v_vector in virus_vectors:
            total = 0
            for idx in range(len(v_vector)):
                total += (v_vector[idx] + similarity[idx])**2
            self.__total_fitness += sqrt(total)
            # print sqrt(total)
        # print virus_vectors

    def cmp(self, viruses):
        for spacer in self.__spacers:
            for virus in viruses:
                min_dist = 100
                for s in viruses[virus]:
                    if len(s.get_dna()) < 1:
                        continue
                    dist = spacer[0].cmp(s)
                    if dist < min_dist:
                        min_dist = dist
                spacer[1][virus] = min_dist


    def __str__(self):
        string = ''
        for native_spacer in self.__spacers:
            string += 'Spacer: {} - Dict: {} \n'.format(native_spacer[0], str(native_spacer[1]))
        string += 'agent fitness: {}'.format(self.fitness)
        return string

    def __cmp__(self, other):
        return self.fitness > other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

class Virus:
    def __init__(self, name, spacers):
        self.__name = name
        self.__spacers = spacers

    def get_name(self):
        return self.__name

    def get_spacers(self):
        return self.__spacers


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        pass
        # raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))


def multiply(agents, times):
    for t in range(times):
        tmp_agents = random.sample(agents, 2)
        agent_spcr1 = tmp_agents[0].get_random_spacers(4)
        agent_spcr2 = tmp_agents[1].get_random_spacers(4)
        joined_spcr = agent_spcr1 + agent_spcr2
        agents.append(Agent(joined_spcr, 2))
    return agents

def population_init(t, population_size, virus_name, data):
    """

    :param virus_name: str
    :param population_size: integer
    :param data: ['spacer1','spacer2',...]
    :return: list(agent)
    """
    entities = []
    for i in range(population_size):
        entities.append(t(virus_name, data[i]))

    return entities

def selection(population):
    return population[:4]


if __name__ == '__main__':

    for test in range(10):
        print 'Test No: {}'.format(test)
        sk1_raw = open_file('SK1')
        jj50_raw = open_file('jj50')
        sk1_raw_neg = open_file('SK1negcompl')
        jj50_raw_neg = open_file('jj50negcompl')

        c = CRISPER.CRISPER(['AGG', 'TGG', 'CGG', 'GGG'], 20)

        c.break_genomes([sk1_raw, sk1_raw_neg])
        sk1_spacers = c.get_data()
        c.clear_data()

        c.break_genomes([jj50_raw, jj50_raw_neg])
        jj50_spacers = c.get_data()
        c.clear_data()

        c.break_genomes([utils.open_file('fake_virus'), utils.open_file('fake_viruscompl')])
        rnd_spacers = c.get_data()
        c.clear_data()

        c.break_genomes([utils.open_file('fake_virus2'), utils.open_file('fake_virus2compl')])
        rnd_spacers2 = c.get_data()
        c.clear_data()

        all_spacers = [sk1_spacers, jj50_spacers, rnd_spacers, rnd_spacers2]
        all_spacers_dict = {'sk1': sk1_spacers, 'jj50':jj50_spacers, 'rnd': rnd_spacers, 'rnd2': rnd_spacers2}

        # c.break_genomes([utils.open_file('allAvirus'), utils.open_file('allAviruscompl')])
        # rnda1 = c.get_data()
        # c.clear_data()
        #
        # c.break_genomes([utils.open_file('allAvirus2'), utils.open_file('allAvirus2compl')])
        # rnda2 = c.get_data()
        # c.clear_data()
        #
        # c.break_genomes([utils.open_file('allAvirus3'), utils.open_file('allAvirus3compl')])
        # rnda3 = c.get_data()
        # c.clear_data()
        #
        # c.break_genomes([utils.open_file('allAvirus4'), utils.open_file('allAvirus4compl')])
        # rnda4 = c.get_data()
        # c.clear_data()
        #
        # all_spacers = [rnda1, rnda2, rnda3, rnda4]
        # all_spacers_dict = {'rnda1': rnda1, 'rnda2':rnda2, 'rnda3': rnda3, 'rnda4': rnda4}

        agents = []

        for i in range(8):
            tmp_virus_spacers = []
            for s in all_spacers:
                tmp_virus_spacers.extend(random.sample(s, 2))
            tmp_a = Agent(tmp_virus_spacers)
            tmp_a.add_virus('sk1')
            tmp_a.add_virus('jj50')
            tmp_a.add_virus('rnd')
            tmp_a.add_virus('rnd2')
            agents.append(tmp_a)

        for epoch in range(10):
            print 'generation number: {}'.format(epoch)
            for agent in agents:
                agent.cmp(all_spacers_dict)
                for s in all_spacers:
                    agent.compute_similarity(s)
            agents.sort()
            agents = selection(agents)
            agents = multiply(agents, 4)
            if epoch ==1:
                print agents[0]

        for agent in agents[:4]:
            print agent