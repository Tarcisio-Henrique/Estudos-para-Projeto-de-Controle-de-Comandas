print('================================= \n| COD |     PRODUTO     | VALOR | \n| 100 | Coca Lata       | 4,00R$| \n'
      '| 101 | Coca Zero Lata  | 4,00R$|\n| 102 | Guaraná Lata    | 4,00R$|\n| 103 | Hamburguer      | 1,20R$| \n'
      '| 104 | Chessburguer    | 1,70R$|\n| 105 | Suco            | 2,20R$| \n| 106 | Refrigerante    | 1,00R$|\n'
      '=================================\n Para sair digite 0')


refri = {

    '100': ['Coca Lata'],
    '101': ['Coca Zero Lata'],
    '102': ['Guaraná Lata'],
    '103': ['Hamburguer', 1.20],
    '104': ['Chessburguer', 1.70],
    '105': ['Suco', 2.20],
    '106': ['Refrigerante', 1.00]
}    

pedido = {}
while True:
    codigo = input('Informe o número do pedido: ')
    if (codigo == 0):
        break
    if codigo in refri:
        quantidade = int(input('Informe a quantidade: '))
        if quantidade > 0:
            valorItem = refri.get(codigo)
            pedido.update({codigo: (valorItem, quantidade)})

valorDoPedido = 0

for linha in pedido.items():
    valorDoPedido += linha[1][0][1] * linha[1][1]  # Preço * Quantidade

print('\nSEU PEDIDO: ')

for linha in pedido.items():
    print(str(linha[1][1]) + ' x ' + 'R$ ' + str(round(linha[1][0][1], 2)) + ' --- ' + str(linha[1][0][0]))

print('\nTOTAL DO PEDIDO: R$ ' + str(round(valorDoPedido, 2)))