def DegreeOfRoot(Latex):
    Latex.replace(" ","")
    Latex.replace("\\","")
    Open = Latex.find("[")
    Close = Latex.find("]")
    if Open > 0:
        return Latex[Open+1:Close]
    return 2

#print(DegreeOfRoot("\\sqrt[3]{123}"))#Test string



