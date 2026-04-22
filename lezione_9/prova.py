import numpy as np
import matplotlib.pyplot as plt
import time 
import sys 
from numba import jit 
from sympy import *
import linalg as lin


n = 10


H = lin.Hermite_coeff(n)
print(H)

