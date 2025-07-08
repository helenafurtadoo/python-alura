# exmplo 1
import re
produto = int(input('Digite o nome do produto: '))
produto_padronizado = produto.strip().lower() 
# para padronizar, tirar letras minusculas e espaços esxtras
print(produto_padronizado)

# exemplo2
nome = int(input('Digite o nome do cliente: '))
cidade = int(input('Digite a cidade do cliente: '))
saudadacao = (f'Olá {nome}! Bem-vinda ao sistema da cidade de {cidade}')

# exemplo 3
texto = int(input('Digite uma palavra-chave: '))
primeiras = texto[:3]
ultimas = texto[-3:]
print(f'Primeirass: {primeiras}')
print(f'Ultimas: {ultimas}')

# exemplo 4
url = int(input('Digite a URL para validação: '))
if url.startswith('https://') and url.endswith(".com"):
    print('URL válida!')
else:
    print('URL inválida!')

# exemplo 5
# sempre o unico n presenta na receita--> \d
# sem usar lista ou loops
descricao_receita = int(input('Digtie a descrição da receita: '))
print(f'A receita {descricao_receita} foi enviada pelo cliente')
resultado = re.findall(r'\d', descricao_receita)[0]
# [0] pega apenas o primeiro numero encontrado na lista
print(f'O numero da receita é: {resultado} ')

# exemplo 6
# usar substituir 'bom' para 'otimo'
texto = int(input('Digite texto a ser revisado: '))
substituida = int(input('Qual palavra deseja substituir? '))
nova = int(input('Qual a nova palavra? '))
final = re.sub(rf'\b{texto}\b', nova)
print(final)

# exemplo 7
# entrada de um nome, e verificacao se atende á:
# comece com eltra maiuscula, e tenham apenas letras(sem numeros ou caracteres especiais)

import re 
nomes = int(input('Digite o nome do cliente para validação: '))
if re.fullmatch(r'[A-Z][a-z]*', nomes):
    print('Nome válido')
else:
    print('Nome inválido')

# exemplo 8
# verificar se os cpfs inseridos estao no padrao correto:
# tres blocos de 3 digitos separados por ponto seguidos por um bloco
# de 2 digitos separados por traço

import re
cpf = input('Digite o CPF no formato XXX.XXX.XXX-XX: ')
if re.fullmatch(r'\d{3} \.\d{3} \.\d{3} -\d{2}', cpf):
    print('CPF válido')
else:
    print('O CPF não está no formato correto')

# exemplo 9
 # pede o nome de livros, e voce organiza por ex de acordo com a letra que comecam
# dai ele da a resposta em forma de lista

import re
titulo = input('Digite o título do livro: ')
letra = input('Digite a letra inicial para a pesquisa: ')

padrao = rf'\b{letra} [a - z]*[A - Z]*'
palavras = re.findall(padrao, titulo, re.IGNORECASE )

if palavras:
    print('Palavras encontradas: ')
    for p in palavras:
        print(p)
    else:
        print('Nenhuma palavra encontrada com essa letra.')

# exemplo 10
import re
dados = input('Digite o nome completo e o ano de nascimento do paciente: ')
padrao = r'(\w) (\w) - (\d{4})'
resultado = re.fullmatch(padrao, dados)
if resultado:
    primeiroNome = resultado.group(1)
    segundoNome = resultado.group(2)
    anoNascimento = resultado;group(3)

    print(f'Pirmeiro nome: {primeiroNome}')
    print(f'Segundo nome: {segundoNome}')
    print(f'Ano de nascimento: {anoNascimento}')

else:
    print('Formato inválido!')

    