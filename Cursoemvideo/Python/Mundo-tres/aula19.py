## Dicionários

## Um dicionário pode ser criado com dict() ou {}
dicionario = dict()
dicionario = {}

## adicionando elementos ao dicionario
dicionario = {"nome": "Jose" , "Idade": 30}

## adicionando uma nova key
dicionario['cidade'] = "Tokyo"

## deletando uma key
del dicionario["nome"]

## mostrando todos os valores do dicionário
print(dicionario)

## mostrando só as chaves
print(dicionario.keys())

## mostrando apenas os valores
print(dicionario.values())

## mostrando tanto os valores quanto as chaves
print(dicionario.items())

## percorrendo um dicionario
for i in dicionario.values():
    print(i)

## criando uma cópia do dicionário
dicionario.copy()

## teste

print(dicionario["Idade"])




