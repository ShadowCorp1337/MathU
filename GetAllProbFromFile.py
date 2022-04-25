import json
from types import SimpleNamespace

def GetProblems(FilePath):
    data = open(FilePath,"r")
    x = json.loads(data.read(), object_hook=lambda d: SimpleNamespace(**d))

    Problems = []
    try:
        for i in x.problems:
            Problems.append(i)
        
        for i in x.childProblems:
            Problems.append(i)
    except:
        print("Eish")
    finally:
        return Problems
