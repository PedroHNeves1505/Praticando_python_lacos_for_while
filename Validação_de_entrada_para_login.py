'''Analisa e garente que o usuario e a senha esteja de acordo com a pedida de segurança'''

print('Cadastro do Buscante')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')
usuario_valido = False
senha_valida = False


while usuario_valido == False:
	if len(usuario) < 5:
		print('O nome de usuário deve conter pelo menos 5 caracteres.')
		usuario = input('Digite seu nome de usuário: ')
	else:
		usuario_valido = True

while senha_valida == False:
	if len(senha) < 8:
		print('A senha deve conter pelo menos 8 caracteres.')
		senha = input('Digite sua senha: ')
	else:
		senha_valida = True
		
print('Cadastro realizado com sucesso!')