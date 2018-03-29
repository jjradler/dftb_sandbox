#molecule_properties.py
"""
    atomSpec.py defines classes for:
        Atom objects that contain calculated molecular total energy


        By:         Joseph J. Radler, University of Washington
        Written:    03/20/18
        Appended:   03/21/18

"""

__author__ = "Joseph J. Radler"

import numpy as np
#from numpy import linalg as lg
from numpy import size as size
from numpy import sqrt as sqrt
#from matrixbuilder import buildfock0_i
#from matrixbuilder import buildfock1_i
#from matrixbuilder import buildfocktotal_i
#from matrixbuilder import build_cvec
#from .singlepoint import SinglePoint
#from .atom_properties import Atom
#from .atompair_properties import AtomPair
#from helpers import *

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

    def __init__(self, name, atoms_list, atompairs_list):
        """Instantiate members of Molecule object"""
        self.atoms_list = atoms_list
        self.atompairs_list = atompairs_list
        self.name = name    # Generate a formula ``name`` from atom list
        self._m_atoms = None
        self._n_electrons = None
        self._p_pairs = None
        self.__rowcol_size = np.int(sqrt(size(atoms_list[0].sab_block)))
        self.overlap = np.zeros((self.__rowcol_size, self.__rowcol_size))
        self.fock0_i = np.zeros((self.__rowcol_size, self.__rowcol_size))
        self.fock1_i = np.zeros((self.__rowcol_size, self.__rowcol_size))
        self.focktot_i = np.zeros((self.__rowcol_size, self.__rowcol_size))
        self.c_vec = np.ones(self.__rowcol_size)

    def num_atoms(self):
        """computes the number of atoms in the molecule class object"""
        self._m_atoms = len(self.atoms_list)

    def num_electrons(self):
        """sums the number of total electrons in the molecule valence."""
        self._n_electrons = 0        #default
        idx = 0                     # initialize loop index

        for idx in enumerate(self.atoms_list):
            self._n_electrons += self.atoms_list[idx].n_elec

    def num_pairs(self):
        """sums the number of atom pairs in the molecule from atom_pairlist"""
        self._p_pairs = 0
        idx = 0

        for idx in enumerate(self.atompairs_list):
            self._p_pairs += self.atompairs_list[idx].n_elec

    # Member instantiation statements
    #num_atoms(self)
    #num_electrons(self)
    #num_pairs(self)
    #self.ntot_elec = set_ntot_elec(self.atoms_list)
    #self.mtot_atoms = len(self.atoms_list)
    #self.S = buildoverlap(self.atoms_list)
    #self.F0_i = buildfock0_i(self.atompairs_list)
    #self.F1_i = buildfock1_i(self.atompairs_list)
    #self.Ftot_i = buildtotalfock_i(self.F0_i, self.F1_i,\
    #        self.S)
    #self.c_vec = cvec_i(self.atoms_list)
