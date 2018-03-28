# atom_properties.py
"""
    atomproperties.py contains the class Atom which defines the
    attributes, sets parameters, and calculates derived attributes
    for Atom class objects in DFTB.

    Date Written: 03/28/2018
"""

from numpy import random as rand

__author__ = "Joseph J. Radler"

class Atom(object):
    """Contains atomic specifications and methods for calculating the total
    energy expectation value of the molecule.

    NOTE:  For this simple prototype, only hydrogen atoms in H2 molecules are
           considered. Parameters are hard-coded in at instantiation for now...

    Attributes:
        element         (string) Element name
        tag             (int) Tag atom with a distinct number
        name            (string) contcatenated element + tag
        r_atom          (array float) coordinates of the atom
        z_atom          (integer) Atomic valence charge (C)
        lmax            (int) Angular momentum of highest occ TBO
        q_guess         (float) Guess Mullekin charge (randomly generated)
        dq0_guess       (float) Mullekin charge fluctuation on Atom
        u_atom          (float) Hubbard hardness parameter
        eks             (float) 1-electron noninteracting KS energy
        f0_params       (array float) F_0 parameters from .skf
    """

    def __init__(self, element, idx, r_atom, z_atom, lmax, u_atom, eks):
        """Instantiation of Atom class object.
        Methods:
            _set_name()      Takes element and tag and generates a unique atom name
            _set_dqguess()   Computes a random initial Mullekin charge fluctuation
        """

        ## The electrons can be set to a default from a __dict__ for the
        ##      various elements available in external/slako

        # Declare and Initialize attributes
        self.name = None
        self.element = element
        self.idx = idx
        self.r_atom = r_atom                   # Instantiated in main module for each instance
        self._z_atom = z_atom                      # Hard-coded in for our H2 example.
        self.lmax = lmax                  # Max angular momentum (s is default)
        self.u_atom = u_atom         # Hubbard parameters for Hydrogen
        self.eks = eks     # Single atom, single particle KS energy (Hydrogen)

        # Atom Object instance Methods
        def _set_name(self):
            """Set atom name from input arg strings "element" and "tag"""
            self.name = self._element + str(self._tag)

        def _set_dqguess(self):
            """Sets a random initial dq between Z * (0, 1]"""
            self._q_guess = abs(self._z_atom * rand.random())
            self.dq0_guess = self._q_guess - self._z_atom


        # Run upon instance of Atom
        _set_name(self)
        print("Atom name is %s\n" % self.name)
        _set_dqguess(self)
