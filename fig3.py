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
        Rt = Resistor(C=src.C, xoff=100, name='Rt', orient='v')
        Vt = Source(p=Rt.n, kind='vdc', yoff=-15, name='Vt', orient='v')
        Ground(C=Vt.n)
        out = Pin(C=Rt.p, xoff=50, name='Vctrl', w=3)
        Wire([src.n, out.C])

except Error as e:
    e.report()
except OSError as e:
    error(os_error(e))
