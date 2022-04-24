import json
from types import SimpleNamespace

data = open("Data.json","r")
x = json.loads(data.read(), object_hook=lambda d: SimpleNamespace(**d))
for i in x.childProblems:
    print(i.problem.en.latex)
