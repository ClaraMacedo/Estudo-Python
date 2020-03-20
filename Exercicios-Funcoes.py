import math
from random import randint
import random
def ex1():
    def rand(n):
        for i in range(n):
            i += 1
            print((str(i)+" ")*i)

    n = int(input("Informe o número:"))
    rand(n)

def ex2():
    def rand(n):
        for i in range(1, n + 1):
            for j in range(i):
                print(j+1,end=" ")
            print("")
    n = int(input("Informe o número:"))
    rand(n)

def ex3():
    def rand(n,n1,n2):
        print("Soma=",n+n1+n2)
    n = int(input("Informe o primeiro argumento:"))
    n1 = int(input("Informe o segundo argumento:"))
    n2 = int(input("Informe o terceiro argumento:"))
    rand(n,n1,n2)

def ex4():
    def rand(n):
        if n>0:
            return "P"
        else:
            return "N"
    n = int(input("Informe o argumento argumento:"))
    print(rand(n))

def ex5():
    def somaImposto(taxaImposto,custo):
        return (taxaImposto*1/100) * custo + custo
    n = float(input("Informe a taxa do imposto:"))
    n1 = float(input("Informe o custo:"))
    n1=somaImposto(n,n1)
    print("Novo custo=",n1)

def ex6():
    def convert(h,m):
        c = h / 12
        if c <= 1:
            d = str(h)
            print("Hora: ",d,":",end="")
        elif c > 1 and c < 2:
            dd = str(h - 12)
            print("Hora: ",dd,":",end="")
        else:
            print('Hora inválida')
            return ()
        if c <= 1 and m <= 60:
            print(m, 'a.m')
        elif c > 1 and m <= 60:
            print(m, 'p.m')
        else:
            print('Formato de minutos invalidos')
            return ()
    h = int(input('Informe a hora:'))
    m = int(input('Informe os minutos: '))
    convert(h, m)

def ex7():
    prestacao = []
    valor = []
    cont=0
    def valorPagamento(prest, dias,cont):
        if dias>0:
            prestJuros = prest+(prest *3/100)
            valort = (dias*(prest*0.1/100))+prestJuros
            valor.append(valort)
            print('Valor corrigido:', valort)
            prestacao.append(cont)
        else:
            valor.append(prest)
            cont=cont+1
        return cont

    while True:
        n = float(input("Informe o valor da prestação: 0 - sair "))
        if n == 0:
            break
        dias = float(input("Informe o quantidade de dias em atraso:"))
        cont=valorPagamento(n, dias,cont)
    print("Quantidade de prestações pagas: ", cont)
    print("Valor total de prestações pagas no dia: R$", sum(valor))

def ex8():
    def qtd(n):
        s = str(n)
        return len(s)
    n = int(input("Informe o número:"))
    print("A quantidade de dígitos do número é:",qtd(n))

def ex9():
    def inverte(n):
        inv = str(n)
        return inv[::-1]
    n = int(input("Informe o número:"))
    print("O inverso do número é:",inverte(n))

def ex10():
    def craps():
        k = randint(2, 13)
        if k == 7 or k == 11:
            print("Ganhou!!", k)
        elif k == 2 or k == 3 or k == 12:
            print("Craps!!! Você perdeu!", k)
        elif (k>=4 and k<=6) or (k>=8 and k<=10):
            print("Esse é o seu numero! Numero:", k,"Você deve tirá-lo navamente")
            x = 0
            while k != x:
                s = input("Digite D para jogar o dado:")
                if s == 'D':
                    x = randint(2, 13)
                    print("Seu numero foi: ", x)
                    if x == 7:
                        print("Voce Perdeu! Que pena Amor")
                        break
            if x != 7:
                print("Voce Ganhou! Parabéns")
        else:
            print("Tirou 1, tente novamente")
    k=0
    craps()

def ex11():
    def extenso(d, m, a):
        if d <= 31:
            meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                     'Outrubro', 'Novembro', 'Dezembro']
            mes = meses[m - 1]
            if mes == 'Fevereiro' and d > 28 and a% 4 == 1:
                print("Fevereiro só tem 29 dias em anos bissextos!")
            elif mes == 'Fevereiro' and d >= 30:
                print("Fevereiro só tem 29 ou 28 dias!")

            else:
                print("%d de %s de %i" % (d, mes, a))
        else:
            print("Dia inválido")
    n = int(input("Informe o DIA:"))
    n1 = int(input("Informe o MES:"))
    n2 = int(input("Informe o ANO:"))
    extenso(n, n1, n2)

def ex12():
    def embaralhar(s):
        emb = random.sample(s,len(s))
        a = ''.join(emb)
        print(a)
    n = input("Informe a palavra:")
    print("O nome embaralhado é:",embaralhar(n))

def ex13():
    def valor_por_omissao(valor):
        if valor == '':
            return int(1)
        else:
            return faixa_minima_maxima(int(valor))

    def faixa_minima_maxima(valor):
        if valor < 1:
            return 1
        elif valor > 20:
            return 20
        else:
            return valor

    def cria_linha(linha):
        l = '+'
        for x in range(linha):
            l += '-'
        l += '+'
        print( l)

    def cria_coluna(linha, coluna):
        for y in range(coluna):
            c = '|'
            c += ' ' * linha
            c += '|'
            print(c)

    def desenha_moldura(linha, coluna):
        cria_linha(linha)
        cria_coluna(linha, coluna)
        cria_linha(linha)

    linha = int(input("Diga quantos +----+, entre 1 e 20: "))
    coluna = int(input("Diga quantos |    |, entre 1 e 20: "))
    desenha_moldura(valor_por_omissao(linha), valor_por_omissao(coluna))

def ex14():
    def gera_combinacoes(lista, n):
        for i in lista:
            for j in lista:
                if n + i + j == 15 and (n != i and n != j and i != j):
                    combinacoes.append((n, i, j))

    def gera_quadro(comb, L1):
        linha1 = L1
        for i in range(len(comb)):
            linha2 = comb[i]
            for j in range(len(comb)):
                linha3 = comb[j]

                if (linha1[0] + linha2[0] + linha3[0] == 15) and \
                        (linha1[1] + linha2[1] + linha3[1] == 15) and \
                        (linha1[2] + linha2[2] + linha3[2] == 15) and \
                        (linha1[0] + linha2[1] + linha3[2] == 15) and \
                        (linha1[2] + linha2[1] + linha3[0] == 15):

                    if (linha1[0] not in linha2) and \
                            (linha1[1] not in linha2) and \
                            (linha1[2] not in linha2):
                        print(linha1)
                        print(linha2)
                        print(linha3)
                        print()

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    combinacoes = []

    for n in range(1, 10):
        gera_combinacoes(lista, n)

    print()

    for L1 in combinacoes:
        gera_quadro(combinacoes, L1)
ex14()