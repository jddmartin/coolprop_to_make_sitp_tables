"""Reproduce Table 4.2 of SITP"""

import numpy as np
import CoolProp

fluid = "H2O"

ps = 1e5 * np.array([1.0, 3.0, 10.0, 30.0, 100.0, 300.0,])
ts = np.array([200.0, 300.0, 400.0, 500.0, 600.0,])

print("\\begin{tabular}{" + ((2 + len(ts)) * "r") + "}")
print(r"& & \multicolumn{" + str(len(ts))
      + r"}{c}{Temperature (\SI{}{\degreeCelsius})} \\ $P$ (\SI{}{bar}) & & ")
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
                'P', p, fluid)
            # see information on "iphase" at:
            # http://www.coolprop.org/coolprop/LowLevelAPI.html?highlight=iphase#imposing-the-phase-optional
            if (phase == CoolProp.iphase_gas or
                phase == CoolProp.iphase_supercritical_gas or
                phase == CoolProp.iphase_supercritical):
                v = CoolProp.CoolProp.PropsSI(
                    quantity,'T', 273.15 + t, 'P', p, fluid) / 1000
                line.append((format % v))
            else:
                line.append(" ")
        print(" & ".join(line) + " \\\\")

print(r"\end{tabular}")
