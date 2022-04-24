import latex2mathml.converter
latex_input = "3x^{2} + 19x + 6"
mathml_output = latex2mathml.converter.convert(latex_input)
print(mathml_output)
