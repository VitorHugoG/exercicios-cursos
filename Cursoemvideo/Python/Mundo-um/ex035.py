a = int(input('lado A:'))
b = int(input('lado B:'))
c = int(input('lado C:'))

if (a < b + c) and (b < a + c) and (c < b + a):
    print('existe')
else:
    print('não existe')