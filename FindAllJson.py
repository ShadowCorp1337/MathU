import os
import sys

def GetFileLocations(path):
    AllFiles = []
    for x in os.walk(path):
        AllFiles.append(x)
    
    jsonFiles = []
    for x in AllFiles:
        for z in x[2]:
            if (".json" in z):
                jsonFiles.append(f"{x[0]}\\{z}")
    return jsonFiles
