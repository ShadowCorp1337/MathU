
#"(2y^{6} + 3y^{5})(-5y - 12)"
def NumberOfPowers(Latex):
    Count = 0
    Latex.replace(" ","")
    if (Latex.find("^{")):
        indexOfUp = Latex.find("^")
        NextCharBrack = Latex[indexOfUp+1] == "{"
        while (NextCharBrack):
            Latex = Latex[indexOfUp + 1:]
            indexOfUp = Latex.find("^")
            NextCharBrack = Latex[indexOfUp+1] == "{"
            Count += 1
        
    else:
        indexOfUp = Latex.find("^")
        while (indexOfUp > 0):
            Count += 1
            Latex = Latex[indexOfUp+1:]
            indexOfUp = Latex.find("^")
    return Count

def NumberOfPowersTo(Latex,Power):
    Count = 0
    indexOfUp = Latex.find("^")
    Latex = Latex[indexOfUp:]
    indexOfBrack = Latex.find("{")

    indexOfCloseBrack = Latex.find("}")
    HasRoot = indexOfUp < indexOfBrack
