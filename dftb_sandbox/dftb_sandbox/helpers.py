# helpers.py
"""
Set of helper functions for initializing and running the program.
Written: 03/28/2018
"""
__author__ = "Joseph J. Radler"

#import numpy
from numpy import linalg as lg

def calc_r(atom_a, atom_b):
    """calculates the bond pair interatomic distance r_ab"""
    r_a = atom_a.r
    r_b = atom_b.r
    r_ab = lg.norm(r_a - r_b)
    return r_ab
def is_nearest(atoms_list):
    """determines the nearest neighbors for each atom in atoms_list"""
    for idx in enumerate(atoms_list):
        for jdx in enumerate(atoms_list):
            if atoms_list[idx].r_ab > atoms_list[jdx].r_ab:
                pass

def get_f1_mn(atom_a, atom_b, _gamma_ab):
    """ Calculates the Fock1 matrix element for mu, nu"""
    # TODO: remmeber that this should be a sum over all pairs...
    dq0a = atom_a.dq0_guess
    dq0b = atom_b.dq0_guess
    gamma_ab = _gamma_ab
    f1_mn = 1.0

    return f1_mn

#def compute_scc(**kwargs):
#    """computes the SCC values internally from initial values in Molecule object"""
#    pass
#
#def totalEnergy(**kwargs):
#    """ computes the total energy from the SCC-generated Fock matrix at a
#    given point."""
#    pass
#
#def setE_rep(molecule):
#    """uses spline array from parser to construct the repulsive energy term"""
#    pass
