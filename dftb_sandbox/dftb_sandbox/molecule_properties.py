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
from numpy import size as size
from numpy import sqrt as sqrt

class Molecule(object):
    """Molecule objects contain information about the Atom objects and
    the interactions between AtomPair objects in the DFTB method to
    initialize the self-consistent charge (SCC) calculation.

    Attributes:
        atoms_list
        atompairs_list
        name
        _m_atoms
        _n_electrons
        _p_pairs
        __rowcol_size
        overlap
        fock0_0
        fock1_0
        focktot_0
        cvector_0

    Methods:
        num_atoms()
        num_electrons()
        num_pairs()
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
        # TODO: Construct the matrices below with buildmatrix calls from singlepoint
        self.overlap = np.zeros((self.__rowcol_size, self.__rowcol_size))
        self.fock0_0 = np.zeros((self.__rowcol_size, self.__rowcol_size))
        self.fock1_0 = np.zeros((self.__rowcol_size, self.__rowcol_size))
        self.focktot_0 = np.zeros((self.__rowcol_size, self.__rowcol_size))
        self.cvector_0 = np.ones(self.__rowcol_size)

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
