import os
#Loop
while True:
    nome = input('Informe seu nome: ')
    peso = str(input('Informe seu peso em KG: ')).replace(',', '.')
    altura = str(input('Informe sua altura em M: ')).replace(',', '.')

    #converter para float
    peso = float(peso)
    altura = float(altura)

     #limpar console
    os.system('cls')

    #calcula o IMC
    imc = peso / (altura ** 2)
    #mostra o valor do imc
    print(f'IMC de {nome}: {imc:,.2f}.')

    #diagóstico
    if imc <= 16.9: 
        print(f'{nome} está muito abaixo do peso.')
        print('Favor procurar um médico urgente')
    elif imc < 18.5:
        print(f'{nome} está abaixo do peso.')
    elif imc < 25:
        print(f'{nome} está no seu peso ideal.')
        print('Parabéns!')
    elif imc < 30:
        print (f'{nome} está acima do seu peso ideal.')
    elif imc < 35:
        print (f'{nome} está obeso.')
    elif imc < 40:
        print (f'{nome} está com obesidade nível II.')
    else:
        print (f'{nome} está com obseidade mórbida.')
        print('Favor procurar um médico urgentemente!')

   
    #verifica se o usuário deseja contiuar
    continuar = input('Deseja continuar (s/n)? ').lower()

    #verifica a opção esoclhida pelo usuário
    if continuar == 's':
        continue
    else:
        break