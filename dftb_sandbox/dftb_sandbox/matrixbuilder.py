# matrixbuilder.py
"""matbuild.py constructs the intial Molecule class matrix members
and also contains functions for updating the Fock matrix during SCC
iterations based on the Molecule and AtomPair class object member
parameters."""

__author__ = "Joseph J. Radler"

import numpy as np
#from numpy import linalg as lg
#from numpy import dot
#from .atompair_properties import AtomPair
#from .atom_properties import Atom
#from .molecule_properties import Molecule
#from .helpers import *

def buildfock0_i(self, atoms_list):
    """builds the zeroth-order Fock matrix for iteration 1 assuming
    l_max = 0 (sigma bonds only for now, with H_2)"""
    # TODO: fix the calls and the way the matrices are constructed between this\
    #        and molecule properties
    m_atoms = len(atoms_list)
    fock0_i = np.empty((m_atoms, m_atoms), dtype=float)
    idx = 0
    jdx = 0

    for idx in enumerate(atoms_list):
        for jdx in enumerate(atoms_list):
            if idx is jdx:
                fock0_i[idx,jdx] = atoms_list[idx].e_ks
            elif idx < jdx:
                fock0_i[idx,jdx] = atoms_list[idx].hss
                fock0_i[jdx,idx] = atoms_list[idx].hss
            else:
                fock0_i[jdx,idx] = 0.00

    return fock0_i

def fock1_update(self, fock1_i):
    # TODO: add in the update expressions for H[mu, nu]
    """updates the Fock^1 matrix from updated dQ_list and Molecule params."""
    pass


def buildfock1_i(self, atoms_list, atompairs_list):
    """builds initial Fock^1 matrix from dqGuess_list and Molecule params."""
    # TODO: write this in terms of the matrix blocks from AtomPairs
    dq = 0
    idx = 0
    jdx = 0
    M = len(atoms_list)
    fock1_i = np.empty((M, M), dtype=float)
    for idx in enumerate(atoms_list):
        for jdx in enumerate(atoms_list):
            if idx is jdx:
                fock1_i = 0.0
            elif idx < jdx:
                fock1_i[idx, jdx] = atompairs_list[idx].fock1_ab
                fock1_i[jdx, idx] = fock1_i[idx, jdx]

    return fock1_i

def buildoverlap(self, atoms_list, atompairs_list):
    # TODO: Write this in terms of the AtomPair overlap blocks
    M = len(atoms_list)
    idx = 0
    jdx = 0
    overlap = np.empty((M, M), dtype=float)

    for idx in enumerate(atoms_list):
        for jdx in enumerate(atoms_list):
            if idx is jdx:
                overlap[idx,jdx] = 1.0
            elif idx < jdx:
                overlap[idx, jdx] = atompairs_list[idx].overlap_ab
                overlap[jdx, idx] = overlap[idx, jdx]

    return overlap

def buildtotalfock_i(self, fock0_i, fock1_i, overlap):
    """builds the total Fock matrix from fock0 and fock1"""
    totalfock_i = fock0_i + fock1_i.dot(overlap)

    return totalfock_i


def build_cvec(self, atoms_list):
   """docstring"""
   # TODO: add a docstring and figure out expressions to generate c_vec from dQ
   pass


def dQ_rebuild(self, c_vec, overlap):
    """docstring"""
    # TODO: how do I extract the updated dQ from the c_vector?
    pass

