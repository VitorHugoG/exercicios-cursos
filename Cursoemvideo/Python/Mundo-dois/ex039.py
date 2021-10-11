from datetime import date

anoNascimento = int(input('digite o ano que você nasceu: '))

idade = date.today().year - anoNascimento

if idade < 18:
    falta = 18 - idade
    print(F'ainda faltam {falta} ano/s para você poder se alistar no exercito ')
elif idade == 18:
    print(F'Você já pode se alistar!')
else:
    passou = idade - 18
    print(F'Você passou {passou} anos para se alistar, resolva isso logo mano uasuha')



