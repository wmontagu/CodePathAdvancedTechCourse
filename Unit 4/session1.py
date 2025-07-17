def filter_sustainable_brands(brands, criterion):
    ret = []
    for elem in brands:
        if criterion in elem["criteria"]:
            ret.append(elem["name"])
    return ret
from collections import defaultdict
def count_material_usage(brands):
    D = defaultdict(int)

    for elem in brands:
        for mat in elem["materials"]:
            D[mat] += 1
    return dict(D)

