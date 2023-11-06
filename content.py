import json


with open("tree.json", "r") as o:
    data = json.load(o)



def spec():
    all_spec = [] 
    specialization = data["спеціальності"]
    for i in range(0, len(specialization)):
        x = specialization[i]["назва"]
        all_spec.append(x)
    return all_spec


def sub(speci):
    all_sub = []
    specialization = spec()
    index = specialization.index(speci)
    for i in range(0, len(data["спеціальності"][index]["предмети"])):
        x = data["спеціальності"][index]["предмети"][i]["назва"]
        all_sub.append(x)
    return all_sub



def lab(speci , subj):
    all_labs = []
    specializations = spec()
    spec_index = specializations.index(speci)
    subjects = sub(speci)
    sub_index = subjects.index(subj)
    for i in range(0, len(data["спеціальності"][spec_index]["предмети"][sub_index]["лабораторні"])):
        x = data["спеціальності"][spec_index]["предмети"][sub_index]["лабораторні"][i]["номер"]
        all_labs.append(x)
    return all_labs
      
def var(speci , subj , labo):
    all_variants = []
    specializations = spec()
    spec_index = specializations.index(speci)
    subjects = sub(speci)
    sub_index = subjects.index(subj)
    labs = lab(speci, subj)
    lab_index = labs.index(int(labo))
    for i in range(0, len(data["спеціальності"][spec_index]["предмети"][sub_index]["лабораторні"][lab_index]["варіанти"])):
        x = data["спеціальності"][spec_index]["предмети"][sub_index]["лабораторні"][lab_index]["варіанти"][i]
        all_variants.append(x)
    return all_variants
 