expressao = input('digite uma expressao:')
abertos = expressao.count("(")
fechados = expressao.count(")")

if abertos == fechados :
    print("essa expressão está certa !")
else:
    print("está expressão não está certa")
