'''Busca por um livro, quando encontrar encerra a busca

Inputs:
	- Livro requerido (str)
	
Outputs:
	- Livro encontrado (bool)
'''

print('Break do buscador de livros')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~')
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
livro_requerido = input('Digite o título que deseja: ')
livro_encontrado = False

for livro in livros:
	if livro_requerido.lower() == livro.lower():
		print(f'Livro encontrado: {livro_requerido}')
		livro_encontrado = True
		break
	else:
		continue
	
if livro_encontrado == False:
	print('Livro não encontrado!')
else:
	print()
	

