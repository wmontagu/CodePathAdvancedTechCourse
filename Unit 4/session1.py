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
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))