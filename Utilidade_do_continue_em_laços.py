'''Mostra os livros 1ue estão em estoque de uma lista'''

print('Filtragem do Buscante!')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~')

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
	if livro['estoque'] != 0:
		for key, value in livro.items():
			print(f'{key} -- {value}')
	else:
		continue
	