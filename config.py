xr = ""
boll = "False"
import json

with open("tree.json", "r") as o:
    data = json.load(o)
print(data["AKIT"][1].keys()[0])