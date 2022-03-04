# Spectral forecast for signals in Python
# Author: Dr. Paul A. Gagniuc
# Date:   01/02/2022

A = "10.3,23.4,44.8,63.2,44.1,35.1,46.5,62.6,50.4,28.9,24.7"
B = "18.8,43.1,52.2,45.5,46.8,46.6,67.9,66.3,70.4,62,39.7"
M = ""

tA = list(map(float, A.split(",")))
tB = list(map(float, B.split(",")))

maxA = max(tA)
maxB = max(tB)
maxAB = max(maxA, maxB)

d = 33

for i in range(0, len(tA)):
    v = ((d / maxA) * tA[i]) + (((maxAB - d) / maxB) * tB[i])
    M += str(round(v,2))
    if i < (len(tA) - 1): M += ","

print(M)
