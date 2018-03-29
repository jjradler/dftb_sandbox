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
from .build_system import make_atoms
from .build_system import make_atompairs
from .build_system import make_molecule

class SinglePoint(object):
    """SinglePoint parses and  runs a single-point calculation, calls functions
    to create instances of atoms, atompairs, and molecules, and stores the
    output to member objects.

        Attributes:
            _molname        (string) name of the molecule under study
            molecule_0      (member object) molecular system containing
                                initial quantities for scc calculation
            overlap         (float array) 9M X 9M total molecular ovelrap matrix
            focktot_0       (float array) 9M X 9M total Fock matrix for
                                M atoms containing initial values.
            cvector_0       (float array) 9M X 1 initial TBO coeffs array
            focktot_k       (float array) 9M X 9M output Fock matrix after
                                SCC calculation to compute g.s. energy.
            cvector_k       (float array) 9M X 1 coefficient matrix for
                                total molecular wavefunctions
            cvector_out     (float array) 9M X 1 coefficient array from KS eqns
            eigenvalues     (float array) Sparse, diagonal 9M X 9M eigenval array
            molecule_out    Class object containing output observables

        Methods:
            molecule_init() Instantiates Atom, AtomPair, and Molecule objects
            scc_solver()    Solves the SCC problem to obtain focktot_out matrix
            """

    def __init__(self):
        # write parser that opens file
        # call parser in generalized build
        self._molname = "H_2"
        self.molecule_0 = None
        self.overlap = None
        self.focktot_0 = None
        self.cvector_0 = None
        self.focktot_k = None
        self.cvector_k = None
        self.cvector_out = None
        self.focktot_out = None
        self.molecule_out = None
        self.eigenvalues_out = None

    def molecule_inst(self):
        """initialize the atoms, pairs list, molecule, and molecule name"""
        _molname = self._molname
        _atoms_list = make_atoms()
        _atompairs_list = make_atompairs(_atoms_list)
        self.molecule_0 = make_molecule(_molname, _atompairs_list, _atoms_list)

        # test print statements (remove before deployment)
        print("Molecule_0's NAME is %s\n" % self.molecule_0.name)
        print("Molecule_0 contains the atoms %s\n" % self.molecule_0.atoms_list)
        print("Molecule_0 contains the pairs %s\n" % \
                self.molecule_0.atompairs_list)
        print("The overlap matrix for molecule_0 is %s\n" % \
                self.molecule_0.overlap)

    def scc_solver(self):
        """solve the SCC iteratively to converge on the Fock matrix focktot_k"""
        pass

    def kohnsham_solver(self):
        """Solve the Kohn-Sham equations for the converged Hamiltonian to output
            the energy eigenvalues and density."""
        pass
