#!/usr/bin/env python
"""
dftb_main.py
Script for calling the various modules of DFTB calculation
for an H2 molecule. This is a testing sandbox only and is 
not intended for production calculations.

Date Written:  02/15/2018
Date Appended: 02/15/2018
"""

__author__ = "Joseph J. Radler"
__version__= "0.0.1"
__email__= "jjradler@uw.edu"
__status__ = "Test"

"""
Module Import
"""

import numpy as np
import sys
import time
from scipy.linalg import solve
from __future__ import division

"""
 Molecular Specifications
"""
# molecule ID dihydrogen (H2) in ground state
#Rab = 0.75         # equilibrium bond distance (Ångströms)


"""
 Construct Parameter Arrays (E, H, S)
"""



#f = open('dftb_sandbox/slako/3ob-hhmod/3ob:hhmod-1-1/H-H.skf')
#lines = f.readlines()

class Parameters(object):
    """A Parameters object contains parsed Slater-Koster Parameters
    from a 

