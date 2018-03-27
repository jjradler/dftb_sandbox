# buildsystem.py
""" Docstring """

__author__ = "Joseph J. Radler"

from .molecule import Atom
from .molecule import AtomPair
from .molecule import Molecule
#from helpers import nearest_neighbors as nearest_neighbors
#from parseinput import parse_atom
#from parseinput import parse_atompair

def make_atoms(elements, rz):
    """Instantiate a list of Atom class objects given input parameters."""
    atoms_list = []
    idx = 0

    for idx in len(elements):
        element = elements[idx]
        r = [0.00, 0.00, rz]
        atoms_list[idx] = Atom(element, idx, r)

    return atoms_list

def make_atompairs(atoms_list):
    """Instantiate an AtomPair class object given input Atom class objects"""
    # TODO:  IS this even necessary?
    pass
    return atompairs_list

def make_molecule(name, atoms_list):
    """Instantiate the Molecule object from the other Atom and Atompair objects.
    This operation also creates matrices from matrixbuilder functions called by
    the Molecule initializer method"""
    pass
