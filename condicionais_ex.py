# exercicio 1
macasVendidas = int(input('Digite a quantidade de maçãs que foram vendidas.'))
bananasVendidas = int(
    input('Digite a quantidade de bananas que foram vendidas. '))

if macasVendidas > bananasVendidas:
    print('As maçãs tiveram mais vendas.')
elif bananasVendidas > macasVendidas:
    print('As bananas tiveram mais vendas.')
else:
    print('As vendas foram iguais.')

# exericio 2
atividadeA = int(input('Informe o numero de dias da atividade. '))

atividadeB = int(input('Informe o numero de dias da atividade.'))

atividadeC = int(input('Informe o numero de dias da atividade. '))

if atividadeA < 0 or atividadeB or atividadeC:
    print('ERRO: Os dias não podem ser negativos. ')
else:
    tempo_total = atividadeA + atividadeB + atividadeC
    print(f'O tempo total do projeto é de {tempo_total} dias. ')

#  exercicio 3

temperaturaAtual = int(input('Digite o valor da temperatura atual. '))

if temperaturaAtual > 25:
    print('ALERTA! Temperatura acima do limite permitido.')

else:
    print('Temperatura dentro do limite. ')

# exercicio 4
altura = float(input('Digite a altura do usuário (em metros):'))

peso = float(input('Digite o peso do usuário (em kg): '))

imc = peso / (altura ** 2)

print(f'Seu IMC é: {imc:.2f}')

if imc >= 25:
    print('Você stá acima do peso.')

elif imc <= 18.5:
    print('Você está com o peso normal. ')

else:
    print('Você esta abaixo do peso. ')

# exercicio 5

depsesas = float(input('Digite em reais o valor total das despesas deste mês'))

if despesas > "3.000":
    print('Atenção! Você ultrapassou o limite do orçamento')

else:
    print('Você está dentro do orçamento.')


# exercicio 6

horaAtual = float(input('Digite a hora atual (em formato de 24 horas): '))

if 8 <= horaAtual < 18:
    print('Acesso permitido')

else:
    print('Acesso negado')


# exercicio 7

nota1 = float(input('Digite o valor da primeira nota'))

nota2 = float(input('Digite o valor da segunda nota'))

nota3 = float(input('Digite o valor da terceira nota'))

mediaFinal = (nota1 + nota2 + nota3) / 3

if mediaFinal >= 7:
    print('Aluno aprovado')

elif 5 <= mediaFinal < 7:
    print('Recuperação')

else:
    print('Aluno reprovado')

# exercicio 8

distancia = float(input('Informe a distância percorrida: '))

if distancia <= 100:
    print('Valor do pedágio: R$ 10,00')

elif 100 < distancia <= 200:
    print('Valor do pedagio: R$ 20,00')

else:
    print('Valor do pedágio: R$ 30,00')


# exercicio 9

numeroInteiro = int(input('Digite um numero inteiro'))

if numeroInteiro % 2 == 0:
    print('O numero é par')

else:
    print('O numero é impar')

# exercicio 10
rendaMensal = float(input('Digite o valor da renda mensal: '))
valorParcela = float(input('Digite o valor da parcela: '))

if rendaMenesal > 2000 and valorParcela <= 0.3 * rendaMensal:
    print('Empréstimo aprovado!')

elif renda <= 2000:
    print('Empréstimo negado: renda insuficiente')

else:
    print('Empréstimo negado: parcela acima de 30% da renda.')
