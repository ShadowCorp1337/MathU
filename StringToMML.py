import latex2mathml.converter
latex_input = "{x+2}^{2}+\\frac{1}{x^{2}}"
mathml_output = latex2mathml.converter.convert(latex_input)
#print(mathml_output)
def arrToMML(arrStrings):
    arrMathml = []
    for i in arrStrings:
      arrMathml.append(latex2mathml.converter.convert(i))
    return arrMathml

