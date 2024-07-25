import pandas as pd
import sympy as sp

m = pd.read_csv(
    "day24input.txt", sep=r", | @ ", engine="python", header=None
).to_numpy()

x, y, z, vx, vy, vz, nano1, nano2, nano3 = sp.symbols(
    "x y z vx vy vz nano1 nano2 nano3"
)

eq1 = sp.Eq(x + (vx * nano1), m[0, 0] + (m[0, 3] * nano1))
eq2 = sp.Eq(y + (vy * nano1), m[0, 1] + (m[0, 4] * nano1))
eq3 = sp.Eq(z + (vz * nano1), m[0, 2] + (m[0, 5] * nano1))
eq4 = sp.Eq(x + (vx * nano2), m[1, 0] + (m[1, 3] * nano2))
eq5 = sp.Eq(y + (vy * nano2), m[1, 1] + (m[1, 4] * nano2))
eq6 = sp.Eq(z + (vz * nano2), m[1, 2] + (m[1, 5] * nano2))
eq7 = sp.Eq(x + (vx * nano3), m[2, 0] + (m[2, 3] * nano3))
eq8 = sp.Eq(y + (vy * nano3), m[2, 1] + (m[2, 4] * nano3))
eq9 = sp.Eq(z + (vz * nano3), m[2, 2] + (m[2, 5] * nano3))

solution = sp.solve(
    [eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9],
    (x, y, z, vx, vy, vz, nano1, nano2, nano3),
)

print(sum(solution[0][:3]))
