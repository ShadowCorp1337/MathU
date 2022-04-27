import sys
import os
from GetAllProbFromFile import *
from FindAllJson import *

Path = input()
if not(bool(Path)):
    Path =sys.argv[0]
AllJson = GetFileLocations( os.path.dirname( Path))

AllProbs = []
for x in AllJson:
    Data = GetProblems(x)
    for z in Data:
        AllProbs.append(z)

#print(AllProbs[len(AllProbs)-1].code)
#print(f"len(AllProbs) {len(AllProbs)}")

nonWordStarters = []
for x in AllProbs:
    y = x.problem.en.latex
    #print(y)
    if str(y).find('\(')==0:
        nonWordStarters.append(y)
        #print(x.problem.en.latex)
    #else:
        #print('unlucky')

for a in nonWordStarters:
    print(a)
