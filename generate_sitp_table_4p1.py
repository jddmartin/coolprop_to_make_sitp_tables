"""Reproduce Table 4.1 of SITP"""

import numpy as np
import CoolProp

fluid = "H2O"

ts = np.array([0.0, 10.0, 20.0, 30.0, 50.0, 100.0])

print(r"\begin{tabular}{rrrrrr} ")
print(r"$T$ & $P$ & $H_{\text{water}}$ & $H_{\text{steam}}$ & ")
print(r"$S_{\text{water}}$ & $S_{\text{steam}}$ \\ ")
print(r"(\SI{}{\degreeCelsius}) & (\SI{}{bar}) & (\SI{}{kJ}) & (\SI{}{kJ}) ")
print(r" & (\SI{}{kJ/K}) & (\SI{}{kJ/K})\\ \hline ")

for t in ts:
    at = t + 273.15
    print("%.1f" % t, end=" & ")
    print("%.3f" % (1e-5 * CoolProp.CoolProp.PropsSI('P','T', at,
                                                'Q',0,fluid)), end=" & ")
    print("%.0f" %
          (CoolProp.CoolProp.PropsSI('H','T', at, 'Q',0,fluid)
           /1000), end=" & ")
    print("%.0f" %
        (CoolProp.CoolProp.PropsSI('H','T', at, 'Q',1,fluid)
         /1000), end=" & ")
    print("%.3f" %
        (CoolProp.CoolProp.PropsSI('S','T', at, 'Q', 0,fluid)
         /1000), end=" & ")
    print("%.3f" %
        (CoolProp.CoolProp.PropsSI('S','T', at, 'Q', 1,fluid)
         /1000), end=" \\\\")
    print()

print(r"\end{tabular}")
