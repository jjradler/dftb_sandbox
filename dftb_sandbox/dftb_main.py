#!/usr/bin/env python
"""
tbAtoms.py
This module instantiates Class objects for Atoms, AtomPairs, and
(TODO) Applied Fields. Also it calls the parser to tabulate
and compute all Slater-Koster and derived parameters in the 
Hamiltonian used in scc.py

Date Written:  02/15/2018
Date Appended: 02/15/2018
"""

__author__ = "Joseph J. Radler"
__version__= "0.0.1"
__email__= "jjradler@uw.edu"
__status__ = "Test"

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
Class Atom(object):
    """An Atom object contains parsed data from two sources: molecular specifications
    (hard-coded in at this time) and an associated .skf (Slater-Koster parameter) file

    Attributes:
        name:           String containing the atom identity abbreviation
        identifier:     String distinguishing the atom from others of its name
        coords:         Object containing x, y, z cartesian coordinates (Angstrom)
        mass:           Float value for atomic mass (amu)
        n_electrons:    Integer total number of electrons in valence (default set)
        U:              Float Hubbard atomic hardness potential (parsed)
        E_ks:           Float Kohn-Sham energy for isolated atom (Hartree)(parsed)
        Z_valence:      Float (hard-coded) valence charge (Coulomb)
    """

    def __init__(self, name, idx)
        """ Return an Atom object with appropriate parsed data"""
        # Initialize data
        self.name           = name
        self.identifier     = name+idx    # TODO figure out how to increment the name + idx (integer) for the assignment
        self.coords.x       = None
        self.coords.y       = None
        self.coords.z       = None
        self.mass           = None
        self.n_electrons    = None
        self.U              = None
        self.E_ks           = None
        self.Z_valence      = None

Class AtomPair(object):
    """An AtomPair object contains parsed data from a nearest-neighbor pair of Atoms 
    and constants as well as computed constants derived from the data and interatomic 
    distances

    Attributes:
        name:           String containing the names of each atom ("e.g. H-H, N-H, O-H, etc.)
        identifier:     String containing the index for the atom pair (e.g. "H1-H2")
        TODO: ADD IN THE REST OF THE ATTRIBUTES HERE.... 
    """
        
        
        
         

                




