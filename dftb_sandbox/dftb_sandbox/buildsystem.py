# buildsystem.py
""" Docstring """

__author__ = "Joseph J. Radler"

import numpy as np
#from helpers import get_rab
from .atom_properties import Atom
from .atompair_properties import AtomPair
#from .moleculeproperties import Molecule

def make_atoms():
    """Instantiate a list of Atom class objects given input parameters."""
    # TODO: parser will go here for .skf and .inp NOT in SinglePoint
    # the following will be handled with the parser later.
    r_atoms = np.array([[0.00, 0.00, 0.375], [0.00, 0.00, -0.375]]) # coordinates
    u_atoms = np.array(0.4195, 0.4195)              # array of Hubbard parameters
    eks = np.array([-0.23860040, 0.0, 0.0])           # Hartree, [E_s, E_p, E_d]
    elements = ['H', 'H']                                     # list of elements
    z_atoms = [1, 1]                     # atom valence charges
    lmax = 0                         # maximum occupied orbital angular momentum
    atoms_list = []
    idx = 0

    for idx in enumerate(elements):
        element = elements[idx]
        r_atom = r_atoms[idx]
        u_atom = u_atoms[idx]
        z_atom = z_atoms[idx]
        atoms_list[idx] = Atom(element, idx, r_atom, u_atom, z_atom, eks, lmax)
    return atoms_list


def make_atompairs(atoms_list):
    """Instantiate an AtomPair class object given input Atom class objects"""
    atompairs_list = []
    idx = 0
    jdx = 0

    for idx in enumerate(atoms_list):
        for jdx in enumerate(atoms_list):
            if idx <= jdx:
                atompairs_list[jdx] = AtomPair(atoms_list[idx], atoms_list[jdx])
                # TODO: insert nearest neighbors here?
                # TODO: assign R_ab in this loop rather than in class inst.?
            else:
                pass

    return atompairs_list

def make_molecule(mol_name):
    """Instantiate the Molecule object from the other Atom and Atompair objects.
    This operation also creates matrices from matrixbuilder functions called by
    the Molecule initializer method"""
    pass
