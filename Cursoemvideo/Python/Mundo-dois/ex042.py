a = int(input('lado A:'))
b = int(input('lado B:'))
c = int(input('lado C:'))

if (a < b + c) and (b < a + c) and (c < b + a):
    if a == b == c:
        print('equilatero')
    elif a == b or b == c or a == c:
        print('isoceles')
    else:
        print('todos os lados diferentes')
else:
    print('não existe')