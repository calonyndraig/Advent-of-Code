import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(5,2025)

id_ranges_raw, ids = input.split("\n\n")

id_ranges_parsed = [(int(x), int(y)) for x,y in (line.split("-") for line in id_ranges_raw.splitlines())]

ids = [int(x) for x in ids.splitlines()]

id_ranges_parsed.sort()

def total_ids(id_ranges):
    if not id_ranges:
        return 0

    merged_ranges = []
    current_start, current_end = id_ranges[0]

    for start, end in id_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = start, end

    merged_ranges.append((current_start, current_end))

    total = sum(end - start + 1 for start, end in merged_ranges)
    return total

print(total_ids(id_ranges_parsed))