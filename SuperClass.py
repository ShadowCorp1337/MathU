class CatMathObj:
    NumVars = 0,
    NumQuad = 0,
    NumCube = 0,
    NumOtherPow = 0,
    NumSin = 0,
    NumCos = 0,
    NumTan = 0,
    NumCosec = 0,
    NumSec = 0,
    NumCot = 0,
    NumPlus = 0,
    NumMinus = 0,
    NumMulti = 0,
    NumDiv = 0,
    NumFact = 0,
    NumSqrt = 0,
    NumRootCube = 0,
    NumRootOther = 0,
    NumSigma = 0,
    NumTheta = 0,
    NumPI = 0,
    NumMisc = 0
    def __init__(self,NumVars,NumQuad,NumCube,NumOtherPow,NumSin,NumCos,NumTan,NumCosec,NumSec,NumCot,NumPlus,NumMinus,NumMulti,NumDiv,NumFact,NumSqrt,NumRootCube,NumRootOther,NumSigma,NumTheta,NumPI,NumMisc):
        self.NumVars = NumVars
        self.NumQuad = NumQuad
        self.NumCube = NumCube
        self.NumOtherPow = NumOtherPow
        self.NumSin = NumSin
        self.NumCos = NumCos
        self.NumTan = NumTan
        self.NumCosec = NumCosec
        self.NumSec = NumSec
        self.NumCot = NumCot
        self.NumPlus = NumPlus
        self.NumMinus = NumMinus
        self.NumMulti = NumMulti
        self.NumDiv = NumDiv
        self.NumFact = NumFact
        self.NumSqrt = NumSqrt
        self.NumRootCube = NumRootCube
        self.NumRootOther = NumRootOther
        self.NumSigma = NumSigma
        self.NumTheta = NumTheta
        self.NumPI = NumPI
        self.NumMisc = NumMisc
    def HasTrigOps(self):
        return bool(self.NumSin  + self.NumCos + self.NumTan + self.NumCosec + self.NumSec + self.NumCot)
    
    
##testObj = CatMathObj(
##    1,2,3,0,0,0,0,0,0,0,0,2,3,4,5,6,7,8,9,10,1,1
##    )
##print(testObj.NumVars)
##print(testObj.HasTrigOps())
