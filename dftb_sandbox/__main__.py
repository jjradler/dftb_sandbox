#dftb_run.py
"""Main DFTB module calling all other modules."""

__author__ = "Joseph J. Radler"

#from sys import argv
#import numpy as np
#from numpy import linalg as lg
from singlepoint import *
#from matbuild import *
#from .dftbscc import *
from .molecule import *



def dftb_run(self):
    """Main program for running a DFTB job in our ``toy implementation``"""
    # TODO: determine jobtype
    # Currently the jobtype is hardcoded as ``singlepoint``

    if jobtype == "singlepoint":
        JobOutput = None
        #TODO: rewrite singlepoint as SinglePoint class with the output values as member objects...
    else:
        return None
