# helpers.py
""" Set of helper functions for initializing and running the program."""
__author__ = "Joseph J. Radler"

import numpy
from numpy import linalg as lg

def is_nearest(atoms_list):
    """determines the nearest neighbors for each atom in atoms_list"""
    pass

def compute_scc(**kwargs):
    """computes the SCC values internally from initial values in Molecule object"""
    pass

def totalEnergy(**kwargs):
    """ computes the total energy from the SCC-generated Fock matrix at a
    given point."""
    pass

def setE_rep(molecule):
    """uses spline array from parser to construct the repulsive energy term"""
    pass
