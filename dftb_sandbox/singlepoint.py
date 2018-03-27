#singlepoint.py
"""
moleculeSpec.py contains classes that perform the SCC calculation
and return a parameterized Fock matrix and its associated eigenvalues (energies)
in the Tight-Binding Orbital (TBO) basis.

Written:    03/21/18
Appended:   03/21/18

"""
__author__ = "Joseph J. Radler"

import numpy as np
import scipy as sp
from sys import argv
from numpy import linalg
from .molecule import Atom
from .molecule import AtomPair
from .molecule import Molecule
#from parseinput import parseatom
#from parseinput import parse_atompair
#from helpers import nearest_neighbors
from buildsystem import make_atoms
from buildsystem import make_atompairs
from buildsystem import make_molecule


def __init__():
    ## TODO: write parser that opens file
    ## Initializations for the single point calculation go here
    m_atoms = 2
    #rx = None                   # list of x-coordinates
    #ry = None                   # list of y-coordinates
    rz = [0.375, -0.375]        # list of z-coordinates
    u = [0.4195, 0.4195]        # list of Hubbard parameters
    elements = ['H', 'H']       # list of elements

    atoms_list = make_atoms(elements, rz)
    #atompairs_list = buildmolecule.make_atompairs(atoms_list)
    #molecule = make_molecule(atoms_list)


def setE_rep():
    # TODO: Use parsed input (.skf) for spline coefficients to compute
    # repulsive energy (E_rep)
    pass

def totalEnergy():
    # TODO: Include the eigenvalue matrix E and E_rep from parsed input
    pass
