# buildsystem.py
""" Docstring """

__author__ = "Joseph J. Radler"

from .atomproperties import Atom
from .atompairproperties import AtomPair
from .moleculeproperties import Molecule

def make_atoms():
    """Instantiate a list of Atom class objects given input parameters."""
    # TODO: parser will go here for .skf and .inp NOT in SinglePoint
    # the following will be handled with the parser later.
    #rx = None                   # list of x-coordinates
    #ry = None                   # list of y-coordinates
    rz = [0.375, -0.375]        # list of z-coordinates
    u = [0.4195, 0.4195]        # list of Hubbard parameters
    e_ks = [-0.23860040, 0.0, 0.0]  # Hartree, [E_s, E_p, E_d]
    elements = ['H', 'H']       # list of elements
    z = [1, 1]
    atoms_list = []
    idx = 0

    for idx in enumerate(elements):
        element = elements[idx]
                         # only s valence orbital occupied.
        r = [0.00, 0.00, rz[idx]]
        u = u[idx]
        z = z[idx]
        atoms_list[idx] = Atom(element, idx, r, u, z, e_ks)

    return atoms_list

def make_atompairs(atoms_list):
    """Instantiate an AtomPair class object given input Atom class objects"""
    # TODO:  IS this even necessary?
    atompairs_list = []
    return atompairs_list

def make_molecule(name, atoms_list):
    """Instantiate the Molecule object from the other Atom and Atompair objects.
    This operation also creates matrices from matrixbuilder functions called by
    the Molecule initializer method"""
    pass
