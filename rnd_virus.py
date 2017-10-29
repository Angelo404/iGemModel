"""
iGemModel
Author: Angelo
File: rnd_virus
Date: 14/09/17
Environment: PyCharm Community Edition
"""
from random import choice

import CRISPER
import utils


def create_random_virus(size):
    let = 'GCAT'
    seq = ''

    for i in range(size):
        seq += 'A'#choice(let)

    return seq


if __name__ == '__main__':
    utils.write_to_file(create_random_virus(48420))
    utils.complement('allAvirus4')

