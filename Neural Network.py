import json
import sys
import numpy

with open("data.json") as json_file:
    data = json.load(json_file)

collection=[]
for i in data:
    print(data[i]["weights"])
    for j in data[i]["weights"]:
        print(j)
