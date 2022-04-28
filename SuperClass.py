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
    NumMisc = 0,
    NumLog = 0
    def __init__(self,NumVars = 0,NumQuad = 0,NumCube = 0,NumOtherPow = 0,NumSin = 0,NumCos = 0,NumTan = 0,NumCosec = 0,
    NumSec = 0,NumCot = 0,NumPlus = 0,NumMinus = 0,NumMulti = 0,NumDiv = 0,NumFact = 0,NumSqrt = 0,NumRootCube = 0,NumRootOther = 0,
    NumSigma = 0,NumTheta = 0,NumPI = 0,NumMisc = 0,NumLog = 0):
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
        self.NumLog = NumLog
    def HasTrigOps(self):
        return bool(self.NumSin  + self.NumCos + self.NumTan + self.NumCosec + self.NumSec + self.NumCot)
    
    #def SumOfTrigOps(self):
        #return int(self.NumSin  + self.NumCos + self.NumTan + self.NumCosec + self.NumSec + self.NumCot)

    def SumOfCalcOps(self):
        return int (self.NumPlus  + self.NumMinus + self.NumMulti + self.NumDiv)

def CompairObject(objFirst,objSecond):
    probability = 1
    if objFirst.HasTrigOps() != objSecond.HasTrigOps():
        return 0
    if objFirst.NumSigma - objSecond.NumSigma != 0:
        return 0
    if objFirst.NumLog - objSecond.NumLog != 0:
        return 0
    if objFirst.NumTheta - objSecond.NumTheta != 0:
        return 0
    if objFirst.NumPI - objSecond.NumPI != 0:
        return 0
    if objFirst.NumFact - objSecond.NumFact != 0:
        return 0
    OpsWeigth = abs(objFirst.SumOfCalcOps() - objSecond.SumOfCalcOps()) * 0.05
    SqrtWeight = abs(objFirst.NumSqrt - objSecond.NumSqrt) * 0.3
    CubeRootWeight = abs(objFirst.NumRootCube - objSecond.NumRootCube) * 0.35
    OtherRootWeight = abs(objFirst.NumRootOther - objSecond.NumRootOther) * 0.35
    OtherPowerWeight = abs(objFirst.NumOtherPow - objSecond.NumOtherPow) * 0.1
    VarsWeigth = 0
    QuadWeight = 0
    CubeWeight = 0
    if objFirst.NumCube == 0 and objSecond.NumCube == 0:
        if objFirst.NumQuad == 0 and objSecond.NumQuad == 0:
            VarsWeigth = abs(objFirst.NumVars - objSecond.NumVars) * 0.15
        else:
            QuadWeight = abs(objFirst.NumQuad - objSecond.NumQuad) * 0.25
            VarsWeigth = abs(objFirst.NumVars - objSecond.NumVars) * 0.08
    else:
        CubeWeight = abs(objFirst.NumCube - objSecond.NumCube) * 0.4
        QuadWeight = abs(objFirst.NumQuad - objSecond.NumQuad) * 0.15
        VarsWeigth = abs(objFirst.NumVars - objSecond.NumVars) * 0.08
    probability = probability - OpsWeigth - SqrtWeight - CubeRootWeight - OtherRootWeight - OtherPowerWeight - VarsWeigth - QuadWeight - CubeWeight
    return probability
            
testObj = CatMathObj(1,2,3,0,0,0,0,0,0,0,0,2,3,4,5,6,7,8,9,10,1,1)
testObj2 = CatMathObj(1,2,3,0,0,0,1,0,0,0,0,2,3,4,5,6,7,8,9,10,1,1)
testObj3 = CatMathObj(1,2,3,0,0,1,0,0,0,0,0,2,3,4,5,6,7,8,9,10,1,1)
testObj4 = CatMathObj(0,0,3,0,0,1,0,0,0,0,0,2,3,4,5,6,7,8,9,10,1,1)
print(CompairObject(testObj2,testObj4))
