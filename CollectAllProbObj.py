import json
from types import SimpleNamespace

data = open("Data.json","r")
x = json.loads(data.read(), object_hook=lambda d: SimpleNamespace(**d))

Problems = []
for i in x.problems:
    Problems.append(i.problem.en.latex)
    
for i in x.childProblems:
    Problems.append(i.problem.en.latex)

print(Problems)
