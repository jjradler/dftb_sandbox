# atompairproperties.py
"""
docstring for atompairproperties.py
"""

__author__ = "Joseph J. Radler"

import numpy as np
from numpy import linalg as lg
from numpy import sqrt as sqrt
import scipy
from scipy import special as sp
from atomproperties import Atom
from matrixbuilder import *
from helpers import *

class AtomPair(object):
    """Contains atomic pairwise interaction parameters as member objects.

    Attributes:
        name                (str)
        atom_a              (object)
        atom_b              (object)
        u_a                 (float)
        u_b                 (float)
        r_a                 (array)
        r_b                 (array)
        r_ab                (float)
        pairtype            (int)
        sameatom            (bool)
        pair_bondtypes      (int)
        pair_n_elecs        (int)
        d_ab                (float)
        gamma_ab            (float)
    Methods:
        set_pairname(atom_a, atom_b)      Returns member object.name
        set_n_elecs(atom_a, atom_b)       Returns number of valence electrons
        calc_r(atom_a, atom_b)            Returns internuclear distance R_ab
        pair_type(atom_a, atom_b)         Returns the type of interaction
                                           (e.g. hetero/homonuclear or same atom)
        bond_types()                      Returns bond-type indicator
        set_gamma(pairtype, u_a, u_b, r_ab)
                                          Returns the A-B polarization
                                            interaction parameter gamma_ab
    """

    def __init__(self, atom_a, atom_b):
        """Instantiate and initialize (currently hardcoded) parameters"""
        # TODO: place most of the methods into a "helper functions" module
        # rather than listing them all here, then use them as calls to
        # set the object values upon instantiation of molecule, not atompairs.
        self.u_a = None
        self.u_b = None
        self.name = None
        self.r_ab = None                # calculate with AtomPair.calc_R
        self.pairtype = None
        self.pair_bondtypes = None       # Set with an AtomPair method later
        self.pair_n_elecs = None
        self.gamma_ab = None            # Set with set_gamma() method

        def set_pairname(self, atom_a, atom_b):
            """docstring"""
            name = atom_a.name + atom_b.tag
            return name

        def set_n_elecs(self, atom_a, atom_b):
            """docstring"""
            n_elecs = atom_a.n_elecs + atom_b.n_elecs
            return n_elecs

        def calc_r(self, atom_a, atom_b):
            """calculates the bond pair interatomic distance r_ab"""
            r_a = atom_a.r
            r_b = atom_b.r
            r_ab = lg.norm(r_a - r_b)
            return r_ab

        def pair_type(self, atom_a, atom_b):
            """determines type (same atom =0 ,homonuclear = 1,heteronuclear = 2)
            of pairwise interaction."""
            if atom_a.name is not atom_b.name:
                if atom_a.element is not atom_b.element:
                    pairtype = 2
                else:
                    pairtype = 1
            else:
                pairtype = 0

            return pairtype

        def bond_types(self):
            """determines the bond types (sigma = 0, pi = 1, delta = 2) from the
            l_max of each Atom object local copy."""
            # TODO: write appropriate set of conditionals to generalize
            pair_bondtypes = 0
            return pair_bondtypes

        def set_gamma(self, pairtype, u_a, u_b, r_ab):
            """sets the value of self.gamma_ab based on interaction type."""
            if pairtype != 0:
                # Case where  both electrons are NOT on the same atom (atom A)
                d_ab = sqrt((1.56*(u_a**2)*(u_b**2)) / ((u_a**2)+(u_b**2)))
                gamma_ab = (1 / r_ab) * sp.erf(r_ab * d_ab)

            else:
                # Case where both electrons are on the same atom (atom A).
                gamma_ab = u_a      # gamma_aa = u_a
            return gamma_ab

        def build_F0ab(self, atom_a, atom_b):
            """constructs AB block of F_0"""
            if atom_a is atom_b:
                mu = 0
                nu = 0
                Lmax_a = atom_a.Lmax
                Lmax_a = atom_b.Lmax

                for mu in enumerate():
                    for nu in enumerate(Ylb):


        def build_F1ab(self, atom_a, atom_b):
            """docstring"""
            return F1ab_block

        def build_Sab(self, atom_a, atom_b):
            """docstring"""
            return Sab_block

        # Class instantiation value assignments

        self.u_a = atom_a.u
        self.u_b = atom_b.u
        self.r_a = atom_a.r
        self.r_b = atom_b.r
        self.name = set_pairname(self, atom_a, atom_b)
        self.r_ab = calc_r(self, atom_a.r, atom_b.r)
        self.pairtype = pair_type(self, atom_a, atom_b)
        self.pair_bondtypes = bond_types(self)
        self.pair_n_elecs = set_n_elecs(self, atom_a, atom_b)
        self.gamma_ab = set_gamma(self, self.pairtype, self.u_a, self.u_b,\
                self.r_ab)
        self.F0ab_block = build_F0ab(self, atom_a, atom_b)
        self.F1ab_block = build_F1ab(self, atom_a, atom_b)
        self.Sab_block = build_Sab(self, atom_a, atom_b)
