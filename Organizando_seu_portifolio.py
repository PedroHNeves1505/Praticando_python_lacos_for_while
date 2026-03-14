'''Imprimindo o portifolio com resposta personalizada para None'''

print('Portifolio da Ana')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~')
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
	if projeto != None:
		print(projeto)
	else:
		print('Projeto Ausente')
	