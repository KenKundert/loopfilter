#!/usr/bin/env python3

from svg_schematic import Schematic, Source, Capacitor, Resistor, Wire, Ground, Pin
from inform import Error, error, os_error
from pathlib import Path

me = Path(__file__)
output_file = me.with_suffix('.svg')

try:
    with Schematic(filename=output_file, line_width=2):

        src = Source(kind='idc', name='Icp', orient='v-')
        Ground(C=src.p)
        Ra = Resistor(C=src.C, xoff=100, name='Ra', orient='v')
        Va = Source(p=Ra.n, kind='vdc', yoff=-15, name='Va', orient='v')
        Ground(C=Va.n)
        Rb = Resistor(C=Ra.C, xoff=100, name='Rb', orient='v')
        Vb = Source(p=Rb.n, kind='vdc', yoff=-15, name='Vb')
        Ground(C=Vb.n)
        out = Pin(C=Rb.p, xoff=50, name='Verr', w=2)
        Wire([src.n, out.C])

except Error as e:
    e.report()
except OSError as e:
    error(os_error(e))
