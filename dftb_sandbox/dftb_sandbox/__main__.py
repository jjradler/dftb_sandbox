#dftb_run.py
"""Main DFTB module calling all other modules."""

__author__ = "Joseph J. Radler"

import sys
from sys import argv
#import numpy as np
#from numpy import linalg as lg
from .singlepoint import SinglePoint



def dftb_run():
    """Main program for running a DFTB job in our ``toy implementation``"""
    # Currently the jobtype is hardcoded as ``singlepoint``
    jobtype = argv[1]

    if jobtype == "singlepoint":
        output = SinglePoint()
        #TODO: rewrite singlepoint as SinglePoint class with the output values as member objects..
        print("The atoms_list is %s" % output.atoms_list)
        print("The atompairs_list is %s " % output.atompairs_list)
    else:
        sys.exit("This package does not yet have that functionality. Apologies.")
