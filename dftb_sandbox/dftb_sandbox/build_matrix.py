# build_matrix.py
"""matbuild.py constructs the intial Molecule class matrix members
and also contains functions for updating the Fock matrix during SCC
iterations based on the Molecule and AtomPair class object member
parameters."""

__author__ = "Joseph J. Radler"

import numpy as np

def buildfock0_0(molecule_0):
    """builds the zeroth-order Fock matrix for iteration 1 assuming
    l_max = 0 (sigma bonds only for now, with H_2)"""
    idx = 0
    jdx = 0

    _ap_list = molecule_0.atompairs_list

    for idx in enumerate(_ap_list):
        for jdx in enumerate(_ap_list):
            if idx < jdx and _ap_list[jdx].atom_a is not _ap_list[jdx].atom_b:
                molecule_0.fock0_0[idx, jdx] = _ap_list[idx].f0ab_block
                molecule_0.fock0_0[jdx, idx] = \
                        np.transpose(_ap_list[idx].f0ab_block)
            elif idx == jdx and _ap_list[jdx].atom_a is _ap_list[jdx].atom_b:
                molecule_0.fock0_0[idx, jdx] = _ap_list[idx].f0ab_block
            else:
                break


def buildfock1_0(molecule_0):
    """builds initial Fock^1 matrix from dqGuess_list and Molecule params."""
    idx = 0
    jdx = 0

    _ap_list = molecule_0.atompairs_list

    for idx in enumerate(_ap_list):
        for jdx in enumerate(_ap_list):
            if idx < jdx and _ap_list[jdx].atom_a is not _ap_list[jdx].atom_b:
                molecule_0.fock1_0[idx, jdx] = _ap_list[idx].f1ab_block
                molecule_0.fock1_0[jdx, idx] = \
                        np.transpose(_ap_list[idx].f1ab_block)
            elif idx == jdx and _ap_list[jdx].atom_a is _ap_list[jdx].atom_b:
                molecule_0.fock1_0[idx, jdx] = _ap_list[idx].f1ab_block
            else:
                break


def buildoverlap(molecule_0):
    """constructs the total molecular overlap matrix"""
    idx = 0
    jdx = 0

    _ap_list = molecule_0.atompairs_list

    for idx in enumerate(_ap_list):
        for jdx in enumerate(_ap_list):
            if idx < jdx and _ap_list[jdx].atom_a is not _ap_list[jdx].atom_b:
                molecule_0.overlap[idx, jdx] = _ap_list[idx].sab_block
                molecule_0.overlap[jdx, idx] = \
                        np.transpose(_ap_list[idx].sab_block)
            elif idx == jdx and _ap_list[jdx].atom_a is _ap_list[jdx].atom_b:
                molecule_0.overlap[idx, jdx] = _ap_list[idx].sab_block
            else:
                break


def buildtotalfock_0(molecule_0):
    """builds the total Fock matrix from fock0 and fock1"""
    fock0_0 = molecule_0.fock0_0
    fock1_0 = molecule_0.fock1_0
    overlap = molecule_0.overlap

    molecule_0.focktot_0 = fock0_0 + fock1_0.dot(overlap)


#def build_cvector0(molecule_0):
#    """Constructs the C vector from SCC"""
#    pass
#
#
#
#def dq_rebuild(molecule_0):
#    """rebuilds the dq values from cvector_0 for the next iteration of SCC"""
#    pass
#
#def fock1_update():
#    """updates the Fock1 matrix from updated dQ_list and Molecule params."""
#    pass
