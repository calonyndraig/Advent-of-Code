import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

package_list = get_source.download_input(2,2015)
packages = get_source.string_convert_to_list(package_list)

def split_string(string):
    """
    Splits a string into three integer variables.
    """
    sides = string.split('x')
    l = int(sides[0])
    w = int(sides[1])
    h = int(sides[2])
    return l, w, h

def package_requires(l,w,h):
    """
    Calculates the amount of ribbon required for a package
    """
    sides = [l, w, h]
    sides.sort()
    volume = l * w * h
    
    total_ribbon = 2 * (sides[0] + sides[1]) + volume    
    
    return total_ribbon
    

total_needed = 0

for package in packages:
    print(package)
    l, w, h = split_string(package)
    package_needs = package_requires(l,w,h)
    total_needed += package_needs

print(total_needed)