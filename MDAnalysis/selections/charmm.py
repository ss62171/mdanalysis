# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# MDAnalysis --- http://mdanalysis.googlecode.com
# Copyright (c) 2006-2011 Naveen Michaud-Agrawal,
#               Elizabeth J. Denning, Oliver Beckstein,
#               and contributors (see website for details)
# Released under the GNU Public Licence, v2 or any higher version
#
# Please cite your use of MDAnalysis in published work:
#
#     N. Michaud-Agrawal, E. J. Denning, T. B. Woolf, and
#     O. Beckstein. MDAnalysis: A Toolkit for the Analysis of
#     Molecular Dynamics Simulations. J. Comput. Chem. (2011),
#     in press.
#

"""
CHARMM selections
=================

Write :class:`MDAnalysis.AtomGroup.AtomGroup` selection to a str file
that defines a CHARMM selection. To be used in CHARMM like this::

  stream macro.str

The selection is name *mdanalysis001*.
"""
import base

class SelectionWriter(base.SelectionWriter):
    format = "CHARMM"
    ext = "str"
    continuation = '-'
    commentfmt = "! %s"
    default_numterms = 4  # be conservative because CHARMM only reads 72 columns

    def _translate(self, atoms, **kwargs):
        # CHARMM index is 1-based
        def _index(atom):
            return "BYNUM %d" % (atom.number + 1)
        return base.join(atoms, ' .or.', _index)

    def _write_head(self, out, **kwargs):
        out.write(self.comment("MDAnalysis CHARMM selection"))
        out.write("DEFINE %(name)s SELECT " % kwargs + self.continuation + '\n')

    def _write_tail(self, out, **kwargs):
        out.write("END")


