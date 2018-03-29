# build_system.py
"""
    Builds the atomic, pairwise interactions, and the molecular system
    initial parameters and populates the objects and matrices used in SCC and
    KS-DFT single-point calculation using the SCC-generated Fock matrix.

    Written: 03/28/2018
"""

__author__ = "Joseph J. Radler"

import numpy as np
#from helpers import get_rab

from build_matrix import buildfock0_0
from build_matrix import buildfock1_0
from build_matrix import buildoverlap
from build_matrix import buildtotalfock_0
from .atom_properties import Atom
from .atompair_properties import AtomPair
#from .atompair_properties import build_f0ab
#from .atompair_properties import build_f1ab
#from .atompair_properties import build_sab
from .molecule_properties import Molecule

def make_atoms():
    """Instantiate a list of Atom class objects given input parameters."""
    # parser will go here for .skf and .inp NOT in SinglePoint
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

        # Test prints
        print("Atom %s has been instantiated!" % atoms_list[idx].name)
        print("The coordinates of Atom %s are %s" % (atoms_list[idx].name, \
                atoms_list[idx].r_atom))
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
                #atompairs_list[jdx].calc_r()
                #atompairs_list[jdx].set_gamma()
                #atompairs_list[jdx].f0ab_block = \
                #        build_f0ab(atoms_list[idx], atoms_list[jdx])
                #atompairs_list[jdx].f1ab_block = \
                #        build_f1ab(atoms_list[idx], atoms_list[jdx])
                #atompairs_list[jdx].sab_block = \
                #        build_sab(atoms_list[idx], atoms_list[jdx])
                # insert nearest neighbors here?
                # assign R_ab in this loop rather than in class inst.?
            else:
                break

    return atompairs_list

def make_molecule(molname, atompairs_list, atoms_list):
    """Instantiate the Molecule object from the other Atom and Atompair objects.
    This operation also creates matrices from matrixbuilder functions called by
    the Molecule initializer method"""

    # Instantiate the molecule
    molecule_0 = Molecule(molname, atompairs_list, atoms_list)

    # Call object population Molecule class methods
    molecule_0.num_atoms()
    molecule_0.num_electrons()
    molecule_0.num_pairs()

    # Call initial matrix population methods.
    buildfock0_0(molecule_0)
    buildfock1_0(molecule_0)
    buildoverlap(molecule_0)
    buildtotalfock_0(molecule_0)

    # Test prints
    print("F_0 is %s\n" % molecule_0.fock0_0)
    print("S matrix is %s\n" % molecule_0.overlap)
    print("F_1 is %s\n" % molecule_0.fock1_0)
    print("F_1 is %s\n" % molecule_0.focktot_0)

    return molecule_0
