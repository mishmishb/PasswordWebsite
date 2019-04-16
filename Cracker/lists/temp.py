import os
import itertools


print(len(list(itertools.permutations(os.listdir('.')))))
