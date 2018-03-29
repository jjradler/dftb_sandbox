# atompair_properties.py
"""
docstring for atompair_properties.py
"""

__author__ = "Joseph J. Radler"

import numpy as np
from numpy import linalg as lg
from numpy import sqrt as sqrt
#import scipy
from scipy import special as sp
#from .atom_properties import Atom
from helpers import get_f1_mn

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
        set_n_elecs(atom_a, atom_b)       Returns _number of valence electrons
        calc_r(atom_a, atom_b)            Returns inter_nuclear distance R_ab
        pair_type(atom_a, atom_b)         Returns the type of interaction
                                           (e.g. hetero/homo_nuclear or same atom)
        bond_types()                      Returns bond-type indicator
        set_gamma(pairtype, u_a, u_b, r_ab)
                                          Returns the A-B polarization
                                            interaction parameter gamma_ab
        build_F0ab()
        build_F1ab()
        build_Sab()
    """

    def __init__(self, atom_a, atom_b):
        """Instantiate and initialize (currently hardcoded) parameters"""
        self.atom_a = atom_a
        self.atom_b = atom_b
        self.name = None
        self._f_occ = [2.0, 0.0, 0.0]        # orbital populations {fs, fp, fd}
        self._u_a = atom_a.u_atom
        self._u_b = atom_b.u_atom
        self.eks_a = atom_a.eks
        self.eks_b = atom_b.eks
        self.r_ab = None                # calculate with AtomPair.calc_R
        self._pair_type = 0
        self._bond_type = 0       # Default to s, set with a method later
        self.n_elecs = None
        self._gamma_ab = None            # Set with set_gamma() method
        self._sss0 = 0.6254181971844   # Overlap ss-sigma, hardcoded for now
        self._fss0 = -5.8560358804                # Hartree, hardcoded for now F, ss-sigma
        self._sab_params = np.zeros(10)
        self._sab_params[0] = self._sss0   # hardcoded for now
        self._f0ab_params = np.zeros(10)
        self._f0ab_params[0] = self._fss0

        # Private Methods
        def _set_pairname(self, atom_a, atom_b):
            """ Sets the pair name from the atom indices"""
            self.name = atom_a.name + atom_b.name

        def _set_n_elecs(self, atom_a, atom_b):
            """docstring"""
            self.n_elecs = atom_a.n_elecs + atom_b.n_elecs

        def _pair_type(self, atom_a, atom_b):
            """determines type (same atom =0 ,homo_nuclear = 1,hetero_nuclear = 2)
            of pairwise interaction."""
            if atom_a is not atom_b:
                if atom_a.element is not atom_b.element:
                    self._pair_type = 2
                else:
                    self._pair_type = 1
            else:
                self._pair_type = 0

        def _bond_types(self, atom_a, atom_b):
            """determines the bond types (sigma = 0, pi = 1, delta = 2) from the
            lmax of each Atom object local copy."""
            lmax_a = atom_a.lmax
            lmax_b = atom_b.lmax

            if lmax_a == 0 and lmax_b != 0 or lmax_a != 0 and lmax_b == 0:
                self._bond_type = np.array(0)
            elif lmax_a == lmax_b and lmax_a != 0:
                self._bond_type = np.range(lmax_a)
            elif lmax_a != 0 and lmax_a < lmax_b:
                self._bond_type = np.range(lmax_a)
            elif lmax_b != 0 and lmax_a > lmax_b:
                self._bond_type = np.range(lmax_b)
            else:
                self._bond_type = np.array(0)   # default.


        # Public Methods
        def calc_r(self, atom_a, atom_b):
            """calculates the bond pair interatomic distance r_ab"""
            r_a = atom_a.r
            r_b = atom_b.r
            self.r_ab = lg.norm(r_a - r_b)

        def set_gamma(self):
            """sets the value of self.gamma_ab based on interaction type."""
            uatom_a = self._uatom_a
            uatom_b = self._uatom_b
            r_ab = self.r_ab
            if self._pair_type != 0:
                # Case where  both electrons are NOT on the same atom (atom A)
                d_ab = sqrt((1.56*(uatom_a**2)*(uatom_b**2)) / ((uatom_a**2)\
                        +(uatom_b**2)))
                self._gamma_ab = (1 / r_ab) * sp.erf(r_ab * d_ab)

            else:
                # Case where both electrons are on the same atom (atom A).
                self._gamma_ab = uatom_a      # gamma_aa = u_a


        def build_f0ab(self, atom_a, atom_b):
            """constructs AB block of F_0 from tabulated parameters"""
            _mu = 0
            _nu = 0
            f0ab_block = np.zeros((9, 9))

            for _nu in enumerate(self.f0ab_params):
                # assume _mu in atom_a
                for _mu in enumerate(self.f0ab_params):
                    if _mu <= _nu:
                        # assume _nu in atom_b
                        if atom_a is not atom_b and self.f0ab_params[_nu] != 0:
                            f0ab_block[_mu, _nu] = self.f0ab_params[_nu]
                            f0ab_block[_nu, _mu] = self.f0ab_params[_nu]
                        elif atom_a is not atom_b and self.f0ab_params[_nu] == 0:
                            pass
                            #f0ab_block[_mu, _nu] = 0.00
                            #f0ab_block[_nu, _mu] = 0.00
                        elif atom_a is atom_b and self.bond_type == 0:
                            # diagonal s-orbital KS energy
                            f0ab_block[_mu, _nu] = self.eks_a[0]
                        elif atom_a is atom_b and self.bond_type == 1:
                            # diagonal p-orbital KS energy
                            f0ab_block[_mu, _nu] = self.eks_a[1]
                        elif atom_a is atom_b and self.bond_type == 2:
                            # diagonal d-orbital KS energy
                            f0ab_block[_mu, _nu] = self.eks_a[2]
                        else:
                            pass
                            #f0ab_block[_mu, _nu] = 0.00
                    else:
                        pass

            return f0ab_block


        def build_f1ab(self, atom_a, atom_b):
            """Constructs the F1ab matrix from parameters and r_ab"""
            _mu = 0
            _nu = 0
            f1ab_block = np.zeros((9, 9))

            for _nu in range(10):
                for _mu in range(10):
                    if _mu <= _nu:
                        if atom_a is not atom_b and _mu < _nu:
                            f1_mn = get_f1_mn(atom_a, atom_b, self._gamma_ab)
                            f1ab_block[_mu, _nu] = f1_mn
                            f1ab_block[_nu, _mu] = f1_mn
                        elif atom_a is atom_b and _mu == _nu:
                            f1ab_block[_mu, _nu] = \
                                    0.5 * self._uatom_a * atom_a.dq0_guess
                    else:
                        break

            return f1ab_block

        def build_sab(self, atom_a, atom_b):
            """Constructs the overlap matrix from tabulated parameters"""
            _mu = 0
            _nu = 0
            sab_block = np.zeros((9, 9))

            for _nu in enumerate(self._sab_params):
                # assume _mu in atom_a
                for _mu in enumerate(self._sab_params):
                    # assume _nu in atom_b
                    if _mu <= _nu:
                        if atom_a is not atom_b:
                            sab_block[_mu, _nu] = self._sab_params[_nu]
                            sab_block[_nu, _mu] = self._sab_params[_nu]
                        #elif atom_a is not atom_b and self._sab_params[_nu] == 0:
                            #sab_block[_mu, _nu] = 0.00
                            #sab_block[_nu, _mu] = 0.00
                        elif atom_a is atom_b and _mu == _nu:
                            sab_block[_mu, _nu] = 1.00
                        else:
                            break
                            #sab_block[_mu, _nu] = 0.00
                    else:
                        break

            return sab_block

        # Class instantiation value assignments
        _set_pairname(self, atom_a, atom_b)
        _pair_type(self, atom_a, atom_b)
        _bond_types(self, atom_a, atom_b)
        _set_n_elecs(self, atom_a, atom_b)
        calc_r(self, atom_a, atom_b)
        set_gamma(self)

        # Generate pairwise interaction matrix blocks
        self.f0ab_block = build_f0ab(self, atom_a, atom_b)
        self.f1ab_block = build_f1ab(self, atom_a, atom_b)
        self.sab_block = build_sab(self, atom_a, atom_b)
