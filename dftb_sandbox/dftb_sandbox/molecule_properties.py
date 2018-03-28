#moleculeproperties.py
"""
    atomSpec.py defines classes for:
        Atom objects that contain calculated molecular total energy


        By:         Joseph J. Radler, University of Washington
        Written:    03/20/18
        Appended:   03/21/18

"""

__author__ = "Joseph J. Radler"

import numpy as np
from numpy import linalg as lg
from .singlepoint import SinglePoint
from .atomproperties import Atom
from .atompairproperties import AtomPair
from matrixbuilder import fock0
from matrixbuilder import fock1
from matrixbuilder import fock_tot
from matrixbuilder import C_vec
from helpers import *

class Molecule(object):
    """Molecule objects contain information about the Atom objects and
    the interactions between AtomPair objects in the DFTB method to
    initialize the self-consistent charge (SCC) calculation.

    Attributes:
        name
        atom
        atompair
        ntot_elec
        mtot_atoms
        ptot_pairs
        c_vec
        totalfock_i
        fock0_i
        fock1_i
        overlap
    """
    self.atoms_list = atoms_list
    self.atompairs_list = atompairs_list

    def __init__(self, name, atoms_list, atompairs_list):
        """Instantiate members of Molecule object"""
        self.name = name    # Generate a formula ``name`` from atom list
        self.ntot_elec = None   # Compute from sum over all AtomPairs
        self.M = len(atoms_list)
        #self.ptot_pairs = None
        self.c_vec = None
        self.Ftot_i = None
        self.F0_i = None
        self.F1_i = None
        self.S = np.empty((2 * M, 2 * M), dtype=float)

        # Member instantiation statements

        self.ntot_elec = set_ntot_elec(self, atoms_list)
        self.mtot_atoms = len(atoms_list)
        self.S = buildmatrix.overlap(atoms_list)
        self.F0_i = fock0(atompairs_list)
        self.F1_i = fock1(atompairs_list)
        self.Ftot_i = fock_tot(self.F0_i, self.F1_i,\
                self.S)
        self.c_vec = cvec_i(atoms_list)
