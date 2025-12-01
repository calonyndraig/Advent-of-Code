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
    if len(sides) != 3:
        raise ValueError("Input string is not in the correct format")
    l = int(sides[0])
    w = int(sides[1])
    h = int(sides[2])
    return l, w, h

def package_requires(l,w,h):
    """
    Calculates the amount of wrapping paper required for a package
    """
    sides = [l*w, w*h, h*l]
    total_paper = 2*sum(sides) + min(sides)
    
    return total_paper
    

total_needed = 0

for package in packages:
    print(package)
    l, w, h = split_string(package)
    package_needs = package_requires(l,w,h)
    total_needed += package_needs

print(total_needed)