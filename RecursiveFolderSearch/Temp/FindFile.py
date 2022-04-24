import os
import sys

print(sys.argv[0])

FilePath = sys.argv[0]

path = os.path.dirname(FilePath)
print(path)

AllFiles =[]
for x in os.walk(path):
    AllFiles.append(x)

print(len( AllFiles))
print(f"len( AllFiles) {len( AllFiles)}")

jsonFiles = []
print(AllFiles[1][2])
for x in AllFiles:
#    print(x[0])
    if (".json" in x[0]):
        jsonFiles.append(x)
print(f"len(jsonFiles) {len(jsonFiles)}")
