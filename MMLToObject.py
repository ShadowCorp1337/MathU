from GrabValueFromMML import *
from SuperClass import *

def GetObjectFromMML(MMLInput):
    OutObj = CatMathObj()
    

import latex2mathml.converter
latex_input = "y ^ 6"
#latex_input = "(2y^{6} + 3y^{5})(-5y - 12)"
#latex_input = "x^2+\\frac{1}{x^{2}}"
#latex_input = "3x^{2} + 19x + 6"
mathml_output = latex2mathml.converter.convert(latex_input)
print(mathml_output)
#GetObjectFromMML(mathml_output)