# matbuild.py
"""matbuild.py constructs the intial Molecule class matrix members
and also contains functions for updating the Fock matrix during SCC
iterations based on the Molecule and AtomPair class object member
parameters."""

__author__ = "Joseph J. Radler"

import numpy as np
from numpy import linalg as lg
from numpy import dot
#import scipy as sp
from .molecule import *
#from .dftbscc import *

def buildfock0_i(self, atoms_list):
    """builds the zeroth-order Fock matrix for iteration 1 assuming
    l_max = 0 (sigma bonds only for now, with H_2)"""
    M = len(atoms_list)
    fock0_i = np.empty((M, M), dtype=float)
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
    """updates the Fock^1 matrix from updated dQ_list and Molecule params."""
    pass

    return fock1_k

def buildfock1_i(self, atoms_list):
    """builds initial Fock^1 matrix from dqGuess_list and Molecule params."""
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

def buildoverlap(self, atoms_list):
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


#def build_c_i(self, atoms_list):
    #"""docstring"""
    #pass
    # return cvec_i


#def dQ_rebuild(self, c_vec, overlap):
#    """docstring"""
#    pass

#    return dQ_k
