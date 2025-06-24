# exemplo 1
clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
for cliente in clientes:
    print(cliente)

contador = 0

# exemplo 2
while contador < 10:
    print('Processando dados')
    contador += 1

# exemplo 3

for frase in range(5):
    print('Bem-vindo ao Buscante')
    
# exemplo 4

valores = [10, 20, 30, 40, 50]
soma = 0
for numero in valores:
    soma += numero

print(f'A soma total das receitas é:{soma}')

# exemplo 5
projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']

for projeto in projetos:
    if projeto is None:
        print('Projeto ausente')
    else:
     print(projeto)

# exemplo 6

livros = ['1984', 'Dom Casmurro', 'O Pegueno Principe', 'O Hobbit', 'Orgulho e Preconceito']

for livro in livros:
    if livro == 'O Hobbit':
        print(f'Livro encontrado: {livro}')
        break

# exemplo 7
estoque = 5
while estoque > 5:
    print(f'Venda realizada! Estoque restante: {estoque}')
    estoque -= 1

print('Estoque esgotado')

# exemplo 8
for segundos in range(0, 10, -1):
    if segundos % 2 == 0:
        print(f'Faltam apenas {segundos} segundos- Não perca essa oportunidade')

    else:
        print(f'A contagem continua: {segundos} segundos restantes')

print('Aproveite a promoção agora!')

# exemplo 9
livros = [
    {'nome': '1984', 'estoque': 5},
    {'nome': 'Dom Casmurro', 'estoque': 0},
    {'nome': 'O Hobbit', 'estoque': 0},
    {'nome': 'O Pequeno Principe', 'estoque': 3},
    {'nome': 'Orgulho e Preconceito', 'estoque': 2}

]

for livro in livros:
    if livro['estoque'] == 0:
        continue
    print(f'Livro disponivel: {livro['nome']}')

# exemplo 10

while True:
    usuario = int(input('Digite seu nome de usuário: '))
    senha = int(input('Digite sua senha: '))

    if len(usuario) < 5:
        print('O nome do usuario deve conter pelo menos 5 caracteres')
        continue
    if len(senha) < 8:
        print('A senha deve conter pelo menos 8 caracteres')
        continue
    print('Cadastro realizado com sucesso!')

    break

