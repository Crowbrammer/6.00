#!/usr/bin/env python3
"""
task: Fill a a gap complete with blind plates.
picture: http://www.koester-systemtechnik.de/images/Pr2.png
available plates: 5, 7, 12, 14, 24
"""
 
from itertools import product
 
def calc_plates(free, plates):
    """Returns the possible solutions of plates to fill the gap"""
    plen = len(plates)
    ranges = product(range(plen), repeat=plen)
    for row in ranges:
        ssum = sum(p * n for p, n in zip(plates, row))
        if ssum == free:
            yield row
 
plates = [5, 7, 12, 14, 24]
result = calc_plates(72, plates)
 
for n, quantity in enumerate(result, start=1):
    print('#=== Result {:>2} ====='.format(n))
    for p, q in zip(plates, quantity):
        if not q:
            continue
        print('#{}x Blindplatte {}'.format(q, p))
    print()