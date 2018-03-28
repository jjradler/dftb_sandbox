#atom_pairs.py
__AUTHOR__="Joseph J. Radler"
"""
    atomPairs.py defines classes for:
        Atom objects that contain calculated molecular total energy

        Also the AtomPair objects are inlcuded here.

        By:         Joseph J. Radler, University of Washington
        Written:    03/20/18
        Appended:   03/21/18

"""

import numpy as np
import scipy
from sys import argv
from numpy import linalg
from molecule_spec import Molecule
from atom_spec import Atom

class AtomPair:
    """Contains atomic specifications and methods for calculating the total
    energy expectation value of the molecule.

    NOTE:  For this simple prototype, only hydrogen atoms in H2 molecules are
           considered. Parameters are hard-coded in at instantiation for now...

    Attributes:
        atomID                      (string) contcatenated element + tag
        nElecs                      ((integer) Total number of valence electrons
        Coord                      array float) coordinates of the atom
        dq                          (float) Mullekin charge
                                        fluctuation vector
        U                           (float) Hubbard hardness parameter
        eKS                         (float) 1-electron noninteracting KS energy

    Methods:
        At some point I will include functions that will parse an input .inp
        file and create different instances of Atoms with identifier labels.

    """


    def __init__(self, name):
        """Instantiation of AtomPair class object. Opens parameter files .inp
           and .skf. Identifies pair of atoms by atomIDs and
        """
        self.inpFile = None

        self.name = self.atomPairName()
        ## The electrons can be set to a default from a __dict__ for the
        ##      various elements available in external/slako

        I = atom1.tag
        J = atom2.tag

        R_I = atom1.coord
        R_J = atom2.coord

        self.name = self.atomPairName(I, J)
        self.R_IJ = self.bondLength(R_I, R_J)
        self.gamma_IJ = self.setGamma(self.R_IJ)


    ## METHOD DEFINITIONS
    def atomPairName(I, J):
           I = inttostr(I)
           J = inttostr(J)
           self.name = atom1.element + "-" + atom2.element + "_" + I + J

    def bondLength():
            pass

    def setOverlapElement():
            pass
            ## set Molecule.S[i, j]

    def setFockElement():
            pass

    def setGamma():
            pass


