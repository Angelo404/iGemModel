"""
iGemModel
Author: Angelo
File: find
Date: 05/07/17
Environment: PyCharm Community Edition
"""

import re
from utils import *
import itertools

positions = []

g = open_file()

p1 = re.compile('.GG')
p2 = re.compile('.G.')
p3 = re.compile('..G')


for idx_p1, idx_p2, idx_p3 in itertools.izip(p1.finditer(g),
                                             p2.finditer(g),
                                             p3.finditer(g)):
    positions.append([idx_p1.start(), idx_p1.group()])
    positions.append([idx_p2.start(), idx_p2.group()])
    positions.append([idx_p3.start(), idx_p3.group()])

for idx in positions:
    print idx

d2_to_csv(positions)
