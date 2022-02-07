from datetime import datetime

def voto (ano_nasc):
 
 ano_atual = datetime.now().year
 idade = ano_atual - ano_nasc

 if (idade >= 16 & idade < 18) | idade > 65 :
   return f'com {idade} anos : seu voto é opcional'
 elif idade >= 18:
   return f'com {idade} anos : seu voto é obrigatório'
 else:
   return f'com {idade} anos : você não vota'


ano_nascimento = int(input('digite o ano do seu nascimento: '))
print(voto(ano_nascimento))

