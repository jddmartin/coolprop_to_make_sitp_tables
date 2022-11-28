"""Reproduce Table 4.3 of SITP"""

import numpy as np
import CoolProp

# R134a is also known as HFC-134a
# see: https://en.wikipedia.org/wiki/1,1,1,2-Tetrafluoroethane
fluid = "R134a"

# according to:
# http://www.coolprop.org/coolprop/HighLevelAPI.html#reference-states
# "ASHRAE: h = 0, s = 0 @ -40C saturated liquid"
# which corresponds to reference state mentioned in Table caption of SITP
CoolProp.CoolProp.set_reference_state(fluid,'ASHRAE')

ps = 1e5 * np.array([1,1.4,2.0,4.0,6.0,8.0,10.0,12.0])

print(r"\begin{tabular}{rrrrrr} ")
print(r"$P$ & $T$ & $H_{\text{liquid}}$ & $H_{\text{gas}}$ & ")
print(r"$S_{\text{liquid}}$ & $S_{\text{gas}}$ \\ ")
print(r"(\SI{}{bar}) & (\SI{}{\degreeCelsius}) & (\SI{}{kJ}) & (\SI{}{kJ}) ")
print(r" & (\SI{}{kJ/K}) & (\SI{}{kJ/K})\\ \hline ")

for p in ps:
    print("%.1f" % (p / 1e5), end=" & ")
    print("%.1f" %
          (-273.15 +
           CoolProp.CoolProp.PropsSI('T','P', p, 'Q',0,fluid)), end=" & ")
    print("%.0f" %
          (CoolProp.CoolProp.PropsSI('H','P', p, 'Q',0,fluid)
           /1000), end=" & ")
    print("%.0f" %
        (CoolProp.CoolProp.PropsSI('H','P', p, 'Q',1,fluid)
         /1000), end=" & ")
    print("%.3f" %
        (CoolProp.CoolProp.PropsSI('S','P', p, 'Q', 0,fluid)
         /1000), end=" & ")
    print("%.3f" %
        (CoolProp.CoolProp.PropsSI('S','P', p, 'Q', 1,fluid)
         /1000), end=" \\\\")
    print()

print(r"\end{tabular}")
