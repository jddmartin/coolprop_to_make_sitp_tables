"""Reproduce Table 4.4 of SITP"""

import numpy as np
import CoolProp

CoolProp.CoolProp.set_reference_state('R134a','ASHRAE')

ps = 1e5 * np.array([8.0, 10.0, 12.0,])
ts = np.array([40.0, 50.0, 60.0,])

print("\\begin{tabular}{" + ((2 + len(ts)) * "r") + "}")
print(r"& & \multicolumn{" + str(len(ts))
      + r"}{r}{Temperature (\SI{}{\degreeCelsius})} \\ $P$ (\SI{}{bar}) & & ")
temp_line = []
for t in ts:
    temp_line.append("%.0f" % t)
print(" & ".join(temp_line) + r"\\ \hline ")

for p in ps:
    for quantity, label, format in [("H", "$H$ (\\SI{}{kJ})", "%.0f"),
                                    ("S", "$S$ (\\SI{}{kJ/K})", "%.3f")]:
        line = []
        if quantity == "H":
            line.append("%.1f" % (p / 1e5))
        else:
            line.append(" ")
        line.append(label)
        for t in ts:
            phase = CoolProp.CoolProp.PropsSI('Phase', 'T', 273.15 + t,
                'P', p, 'R134a')
            if phase == CoolProp.iphase_gas:
                v = CoolProp.CoolProp.PropsSI(
                    quantity,'T', 273.15 + t, 'P', p, 'R134a') / 1000
                line.append((format % v))
            else:
                line.append(" ")
        print(" & ".join(line) + " \\\\")

print(r"\end{tabular}")
