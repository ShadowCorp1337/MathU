def GetValue(MMLInput,Tag):
    StartTag = f"<{Tag}>"
    EndTag = f"</{Tag}>"
    Out = MMLInput[MMLInput.find(StartTag)+len(StartTag):MMLInput.find(EndTag)]
    return Out

def GetCountOf(MMLInput,Tag):
    StartTag = f"<{Tag}>"
    StartAt = MMLInput.find(StartTag)
    Count = 0
    while (StartAt > 0):
        Count += 1
        MMLInput = MMLInput[StartAt+len(StartTag):]
        StartAt = MMLInput.find(StartTag)
    return Count
