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
        C1 = Capacitor(C=src.C, xoff=100, name='C1')
        Ground(C=C1.n)
        R2 = Resistor(C=C1.C, xoff=100, name='R2', orient='v')
        C2 = Capacitor(p=R2.n, yoff=-15, name='C2')
        Ground(C=C2.n)
        out = Pin(C=R2.p, xoff=50, name='Verr', w=2)
        Wire([src.n, out.C])

except Error as e:
    e.report()
except OSError as e:
    error(os_error(e))
