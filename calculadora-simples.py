# Calculadora usando while

while True:
    # Solicitando dados para operação
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+, -, *, /): ')

    # Verificar se os números são válidos
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)  
    except ValueError:
        print('Um ou ambos os números digitados são inválidos. Tente novamente.')
        continue

    # Verificar se o operador é válido
    if operador not in ['+', '-', '*', '/']:
        print('Operador inválido. Tente novamente')
        continue

    # Verificar se não é uma divisão por zero
    if operador == '/' and num_2_float == 0:
        print('Erro: não é possível dividir por zero.')
        continue

    # Realizando a operação de acordo com o operador
    if operador == '+':
        resultado = num_1_float + num_2_float
    elif operador == '-':
        resultado = num_1_float - num_2_float
    elif operador == '*':
        resultado = num_1_float * num_2_float
    elif operador == '/':
        resultado = num_1_float / num_2_float

    # Exibindo o resultado
    print(f'O resultado de {num_1_float} {operador} {num_2_float} é: {resultado}')

    # Perguntando ao usuário se deseja sair ou continuar
    sair = input('Deseja sair? [s]im ou [n]ão: ').lower()
    if sair == 's':
        break