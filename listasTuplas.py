# exercicio 1
despensa = [Leite, Feijão, Manteiga, Arroz]
item = input('Digite o item que quer verificar: ')
if item in depensa:
    print(f'O item {item} já está armazenado')
else:
    print(f'O item {item} precisa ser comprado')
    print(f'Aqui estão os itens armazenados neste momento: {depensa}')
# exercicio 2
notas = [85, 70, 90, 60, 75]
print(f'Nota originais: {notas}')

notas.sort()
print(f'Notas ordenadas: {notas}')
         
# exercicio 3

while True: 
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    else: 
        print(f'Voluntários registrados: {lista}')

# exercicio 4
estoqueUm = tuple(input('Produtos do estoque 1 (separados por virgula:').split(","))
estoqueDois = tuple(input('Produtos do estoque 2 (separados por virgula): ').split(","))

estoqueCombinado = estoqueUm + estoqueDois
print(f'Estoque combinado: \n{estoqueCombinado}')

# exercicio 5
lista = ['Ana', 'Pedro', 'Carlos']
print[f'Lista atual de convidados: {lista}']
novoNome = input('Digite o nome do novo convidado: ')
posicao = ('Digite a posição na qual deseja inserir o novo convidado: ')
lista.insert(posicao - 1, novoNome)
print(f'Lista atualizada de convidados: {lista}')

# exercicio 6

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra2', 'Palestra 1']
eventos_registrados.reverse()
print(f'Ordem corrigida: {eventos_registrados}')

# exercicio 7

lista = ['Ana', 'Pedro', 'João']
print(f'Lista original: {lista}')

nomeErrado = input('Digite o nome incorreto: ')
if nomeErrado in lista:
    nomeCerto = input('Digite o nome correto: ')
    posicao = lista.index(nomeErrado)  #serve para encontrar a posicao dentro de uma lista
    lista.remove(nomeErrado)
    lista.insert(posicao, nomeCerto)
    print(f'O nome {nomeErrado} foi substituído por {nomeCerto}')
    print(f'Lista atualizada: {lista}')

else:
    print('Nome não encontrado')

# exercicio 8
pedido = input('Pedidos feitos (separados por virgula): ').split(",")
pedido.pop()
print(f'Pedidos finais: \n{pedido}')

# execicio 9

notasFinais = int(input('Digite a nota dos alunos (separadas por virgula)').split(","))
notasFinais = [float(nota) for nota in notasFinais] #transforma cada string da lista em um numero decimal

media = sum(notasFinais) / len(notasFinais)
#sum = soma todos os valores da lista// len = conta quantos ELEMENTOS tem na lista
print(f'A média da turma foi: {media:.2f}')

# exercicio 10
dados = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ').split(",")

for i in range(0, len(dados), 3):
    nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
    print(f'Aluno: {nome}')
    print(f'Idade: {idade}')
    print(f'Nota: {nota}')