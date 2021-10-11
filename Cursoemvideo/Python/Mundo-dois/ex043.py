print('==' * 5, 'IMC', '==' * 5)

peso = float(input('digite o seu peso: '))
altura = float(input('digite a sua altura em cm'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Parabéns você está na faixa de peso ideal')
elif 25 <= imc < 30:
    print('Você está em sobre peso')
elif 30 <= imc < 40:
    print('Você está em obesidade')
elif imc >= 40:
    print('Obesidade Mórbida, cuidado')





