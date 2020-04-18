#!/bin/python3

import os
from sys import *

expr = ""
argc = len(argv)

if(argc == 1): 
    print("math: missing expression\n\tusage: math [expression]\n\tFor multiplication, use \'x\' instead of \'*\'.")
    exit(1)

for v in argv[1:]:
    expr += v + " "

expr = expr.replace("x","*")

os.system("python3 -c \'print(" + expr + ") \'")
