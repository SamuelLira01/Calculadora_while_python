#           CALCULADORA WHILE
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')

    print("""
+ Adição
- Subtração
/ Divisão
* Multiplicação
** Potenciação
""")

    operador = input('Digite o operador (+, -, /, *, **): ')

    num_valido = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        num_valido = True

    except ValueError:
        num_valido = None

    if num_valido is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_validos = '+', '-', '/', '*', '**'

    if operador not in operadores_validos:
        print('O operador é inválido.')
        continue

    print('Confira o resultado da sua conta abaixo.')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')

    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')

    elif operador == '/':
        if num_2_float == 0:
            print('Não é possível dividir por zero.')
            continue

        print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float:.2f}')

    elif operador == '**':
        print(f'{num_1_float} ** {num_2_float} = {num_1_float ** num_2_float}')

    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float:.2f}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break
