def dobro_tri_quadr(n1):
    d1 = n1 * 2
    d2 = n1 * 3
    d3 = n1 * n1
    print(f'O dobro do número informado é: {d1}.')
    print(f'O triplo do número informado é: {d2}.')
    print(f'O quadrado do número informado é: {d3}.')


n1 = float(input('Informe o número: '))

dobro_tri_quadr(n1)