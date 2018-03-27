#molecule.py
"""
moleculeSpec.py defines classes for:
Molecule objects that contain calculated molecular total energy
expectation value, the parameterized molecular zeroth-order
Fock and Overlap matrices, Mullekin charges, and all other
necessary parameters for performing a single-point energy calculation
using the DFTB method.

NOTE: THIS MODULE IS BASICALLY USELESS BUT I'M KEEPING IT AROUND
FOR NOW IN A SUBDIRECTORY JUST IN CASE...

Also the AtomPair subclass objects are contained within, as well as
Atom subclasses which contain pairwise interaction parameters and
parameterized Atomic properties, respectively.

By:         Joseph J. Radler, University of Washington
Written:    03/20/18
Appended:   03/21/18
"""

from sys import argv
import numpy as np
from numpy import linalg as lg
from numpy import random as rand
#import scipy
from .atoms import Atom
from

__AUTHOR__ = "Joseph J. Radler"

class Molecule(object):
    """Contains molecular specifications and methods for calculating the total
    energy expectation value of the molecule.

    Attributes:
        m_atoms                      (integer) Number of atoms
        n_elecs                      (integer) Total number of valence electrons
        Z_vec                           (m X 1 array integer) Atomic valence charges
        dQ_vec                          (m X 1 array float) Mullekin charge
                                        fluctuation vector
        C_vec                           (m x 1 array float) TBO coefficient vector
        Emat                           (long float) Total molecular energy (Hartree)
        Fmat                           (m X m array float) Fock matrix
        Smat                           (m X m array float) Overlap matrix

    Methods:
        nearest_neigh()
        overlapBuild()
        fockBuild()
        cBuild()
        dQBuild()
        UBuild()
        energySCC()

    Subclass Objects:
        AtomPair
        Atom
    """

    def __init__(self):
        """
        Instantiation of Molecule object, load parameter file, set constants
        """
        # Create the member attributes but initialze to None
        self.atom_1 = Atom("H", 1)
        self.atom_2 = Atom("H", 2)
        self.Emat = None
        self.Fmat = None
        self.Smat = None
        self.Z_vec = None
        self.C_vec = None
        self.dQ_vec = None

        # TODO: Write an iterator to access the parsed data array object
        self.m_atoms = 2  #Put this in a __dict__ iterator?
        self.n_elecs = self.atom_1.n_elec + self.atom_2.n_elec

        self.pairlist = self.nearest_neigh()            ## Determines nearest neighbors for all atoms
        self.Smat = self.overlap_build()              ## Constructs the Molecule.S matrix
        self.Fmat = self.fock_build()                 ## Constructs the Molecule.F matrix
        self.C_vec = self.C_build()               ## Constructs the Molecule.c vector fpr SCC
        self.dQ_vec = self.dQ_rebuild()

    def nearest_neigh(self):
        """ Determine nearest neighbor pairs to instantiate AtomPairs
            (future)"""
        pass

    def overlap_build(self):
        """ Build Overlap matrix from .skf parameters"""
        pass

    def C_build(self):
        """ Build eigenvector from density"""
        pass

    def fock_build(self):
        """ Build Fock matrix for SCC iteration k from AtomPair and
        Mullekin charge difference vector dQ"""
        pass

    def dQ_rebuild(self):
        """ rebuild next iteration of dQ vector from c vectors  """
        pass

    def fock_scc(self):
        """ Calculate eigenvector c and eigenvalue matrix E
        from constructed F and S """
        pass
        ## compute eigensolver()

