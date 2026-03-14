'''Contagem regressiva personalozada'''

print('Contagem regressiva personalizada')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

segundos = 10

while segundos != 0:
	if segundos % 2 == 0:
		print(f'Faltam apenas {segundos} segundos - Não perca essa oportunidade!')
		segundos = segundos - 1
	else:
		print(f'A contagem continua: {segundos} segundos restantes.')
		segundos = segundos - 1

print('Aproveite a promoção agora!')
