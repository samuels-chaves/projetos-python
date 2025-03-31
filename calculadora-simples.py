from time import sleep #impotanto a biblioteca

print('Bem-vindo(a) à calculadora simples! 🧮')
print('Digite o número da operação que deseja fazer:')
print('[1] Somar\n[2] Multiplicar\n[3] Subtrair\n[4] Dividir')

# Pegando a opção do usuário
op = float(input('Digite o número desejado: '))
print('\033[32mAguarde um momento...\033[m') #Estou definindo a cor verde na mensagem
sleep(2) #Pausa de 2 segundos

# Verificando se a opção é válida
if op not in [1, 2, 3, 4]:
    print('Opção inválida! Tente novamente.')
else:
    # Pegando os números para a operação
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    # Executando a opção escolhida
    if op == 1:
        resultado = num1 + num2
        operacao = "soma"
    elif op == 2:
        resultado = num1 * num2
        operacao = "multiplicação"
    elif op == 3:
        resultado = num1 - num2
        operacao = "subtração"
    elif op == 4:
        if num2 == 0:
            print('Erro: Divisão por zero não é permitida!')
            exit()
        resultado = num1 / num2
        operacao = "divisão"

    # Exibindo o resultado
    print(f'Resultado da {operacao}: {resultado}')


