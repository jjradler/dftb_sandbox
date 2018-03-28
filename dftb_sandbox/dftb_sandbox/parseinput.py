#parseinput.py
"""
parser_inputs.py acts as an interface to load the parameters and molecular
specifications from .skf and .inp files. Note:  For now this will have all
parameters hard-coded in to ensure the remainder of the code performs as
expected.

Date Written:   03/22/18
Date Appended:  03/22/18
"""
__author__ = "Joseph J. Radler"

import numpy as np
#from numpy import linalg as lg
from .moleculebuild import Atom
from .moleculebuild import AtomPair
from .moleculebuild import Molecule

# TODO: Perhaps write a whole other function to handle the file opening
#       and array slicing necessary...

def parse_atom(self, MoleculeBuild):
    """Parses data for single Atom objects only from .inp files.
    """

    # TODO: Add a call to open the file and chop up the array output into
    # useful chunks the parser can make sense of.

    # TODO: generalize this with a loop for more than one atom as read off \
    #       input files.

    # These values are hardcoded, but will end up in a parser loop eventually
    # which will add them to a list of atom objects that can be sorted into
    # nearest_neighbors by the nearest_neighbors function. The
    # nearest_neighbors will then instantiate AtomPairs as another list which
    # will be appended to Molecule class objects.

    # Instantiate atom_1 objects
    self.Atom = MoleculeBuild.Atom
    if self.Atom.name is 'H_1':
        print('H_1.name = %s' % self.Atom.name)         # diagnostic print
        #self.H_1.r = np.array(0.0, 0.0, 0.375)      # Hard-coded coords (Angstroms)
        r_1 = np.array(0.0, 0.0, 0.375)
        # self.H_1.dq0_guess = H_1.set_dqguess()      # Initial charge density guess
        #dq0_guess_1 = Atom.set_dqguess()_
        #self.H_1.u = 0.4195                         # Hubbard parameter for H
        u_1 = 0.4195
        #self.H_1.l_max = 0                          # S-type
        l_max_1 = 0
        #self.H_1.n_elec = 1
        n_elec_1 = 1
        #self.H_1.z = 1
        z_1 = 1                                     # atomic charge
        e_ks_1 = 0.23860040
        #self.H_1.e_ks = -0.23860040                 # Hartrees
        print('H_1.dq0_guess = %d' % self.Atom.dq0_guess)   # diagnostic print

        # set atom member object values
        self.H_1 = MoleculeBuild.Atom_1
        self.H_1.name = Molecule.Atom_1.name
        self.H_1.r = r_1
        self.H_1.dq0_guess = Molecule.Atom_1.dq0_guess
        self.H_1.u = u_1
        self.H_1.l_max = l_max_1
        self.H_1.n_elec = n_elec_1
        self.H_1.z = z_1
        self.H_1.e_ks = e_ks_1

    elif self.Atom.name is 'H_2':
        # Instantiate atom_2 objects
        r_2 = np.array(0.0, 0.0, -0.375)
        print('H_2.name = %s' % self.Atom.name)         # diagnostic print
        #H_2.dq0_guess = H_2.set_dqguess()
        u_2 = 0.4195                         # Hubbard parameter for H
        l_max_2 = 0                          # S-type
        n_elec_2 = 1
        z_2 = 1                             # Coulombs
        e_ks_2 = -0.23860040                 # Hartrees
        print('H_2.dq0_guess = %d' % self.Atom.dq0_guess)   # diagnostic print

        # Save to Objects
        self.H_2.name = self.Atom.name
        self.H_2.r = r_2
        self.H_2.dq0_guess = self.Atom.dq0_guess
        self.H_2.u = u_2
        self.H_2.l_max = l_max_2
        self.H_2.n_elec = n_elec_2
        self.H_2.z = z_2
        self.H_2.e_ks = e_ks_2

    return None

def parse_atompair(self):
    """parses the parameters for each AtomPair object."""

    return None

def make_atomlist(self):

    return None

def make_atompairlist(self):

    return None
