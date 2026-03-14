'''Controla o estoque do Buscante, se for afetivado a compra o estoque é diminuido

Inputs:
	- Deseja comprar (bool)

Outputs:
	- Quantidade em estoque (int)
'''

print('Controle de estoque')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

qnt_em_estoque = 5
while qnt_em_estoque != 0:
	deseja_comprar = (input('Deseja comprar (sim ou não): '))
	deseja_comprar = True if deseja_comprar == 'sim' else deseja_comprar == False
	if deseja_comprar:
		qnt_em_estoque = qnt_em_estoque - 1
		print(f'Venda realizada! Estoque restante: {qnt_em_estoque}')
	else:
		print(f'Estoque restante: {qnt_em_estoque}')

print('Estoque esgotado')
