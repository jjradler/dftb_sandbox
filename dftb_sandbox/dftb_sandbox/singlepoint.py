#singlepoint.py
"""
moleculeSpec.py contains classes that perform the SCC calculation
and return a parameterized Fock matrix and its associated eigenvalues (energies)
in the Tight-Binding Orbital (TBO) basis.

Written:    03/21/18
Appended:   03/21/18

"""
__author__ = "Joseph J. Radler"

#import numpy as np
#import scipy as sp
#from sys import argv
#from numpy import linalg
from .buildsystem import make_atoms
from .buildsystem import make_atompairs
#from .buildsystem import make_molecule

class SinglePoint(object):
    """SinglePoint parses and  runs a single-point calculation, calls functions
    to create instances of atoms, atompairs, and molecules, and stores the
    output to member objects.

        Attributes:
            atoms_list          (object list) all atoms in the system
            atompairs_list      (object list) all atom pairs
            molecule            (member object) molecular system containing
                                    initial quantities for scc calculation
            focktot_0               (float array) 9M X 9M total Fock matrix for
                                    M atoms containing initial values.
            focktot_k               (float array) 9M X 9M output Fock matrix after
                                    SCC calculation to compute g.s. energy.
            cvector_k                  (float array) 9M X 1 coefficient matrix for
                                    Atomic Orbitals (AOs)
            """

    def __init__(self):
        ## TODO: write parser that opens file
        ## Initializations for the single point calculation go here

        # instantiation statements
        self.molname = "H_2"
        self.atoms_list = make_atoms()
        self.atompairs_list = make_atompairs(self.atoms_list)
        #self.molecule = make_molecule(self.molname)
        #test print statements
        # TODO: set up appropriate block builder in matrixbuilder
        self.focktot_0 = None   #computed from matrixbuilder
        self.focktot_k = None   #computed from matrixbuilder
        self.cvector_k = None   #computed from matrixbuilder
#       def solve_KSeqns(self, molecule):
#           """solve the KS equations for the SCC-solution for Fk_tot"""
#            pass
