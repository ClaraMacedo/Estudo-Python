import math
from random import randint, uniform
import re

def ex1():
    lista = []
    for i in range(5):
        n = int(input("Informe o número:"))
        lista.append(n)
    for i in lista:
        print(i)

def ex2():
    lista=[]
    for i in range(10):
        n = float(input("Informe o número:"))
        lista.append(n)
    d=len(lista)
    for i in range(d):
        print(lista[-1],end=" ")
        lista.pop()

def ex3():
    notas=[]
    media=0
    for i in range(4):
        n = float(input("Informe a nota:"))
        notas.append(n)
        media+=n
    for i in notas:
        print(i,end=" ")
    media=media/4
    print("\nA média das notas é:", media)

def ex4():
    lista = []
    listac = []
    cont=0
    for i in range(10):
        n = input("Informe um character:")
        lista.append(n)
        if n!= "a" and n !="e" and n!="i" and n!="o" and n!="u":
            cont+=1
            listac.append(n)
    print("Foram lidas",cont,"consoantes")
    for i in listac:
        print(i, end="  ")

def ex5():
    numeros = []
    pares = []
    impares =[]
    for i in range(20):
        n = int(input("Informe um número:"))
        numeros.append(n)
        if n%2==0:
            pares.append(n)
        else:
            impares.append(n)
    print("Números: ")
    for i in numeros:
        print(i, end="  ")

    print("\nPares: ")
    for i in pares:
        print(i, end="  ")

    print("\nÍmpares: ")
    for i in impares:
        print(i, end="  ")

def ex6():
    listaNotas = []
    cont=0
    for i in range(10):
        media = 0
        notasAluno = []
        for j in range(4):
            notasAluno.append(float(input('Nota ' + str(j + 1) + '\n')))
            media += notasAluno[j]
        media = media / 4
        if media>=7:
            cont+=1
        listaNotas.append(media)
    print(listaNotas)
    print(cont,"alunos tem a média maior ou igual a 7")

def ex7():
    lista = []
    soma = 0
    mult=1
    for i in range(5):
        n = int(input("Informe um número:"))
        lista.append(n)
        soma+=n
        mult*=n
    print("\nNúmeros:", end=" ")
    for i in lista:
        print(i,end=" ")
    print("\nSoma:",soma)
    print("Multiplicação:",mult)

def ex8():
    listaId = []
    listaAlt = []
    for i in range(5):
        idade = int(input("Informe a idade:"))
        alt = float(input("Informe a altura:"))
        listaId.append(idade)
        listaAlt.append(alt)

    print("Lista de Idades:")
    for i in range(5):
        print(listaId[-1],end=" ")
        listaId.pop()

    print("\nLista de Alturas:")
    for i in range(5):
        print(listaAlt[-1], end=" ")
        listaAlt.pop()

def ex9():
    lista=[]
    soma=0
    for i in range(10):
        n = int(input("Informe um número"))
        lista.append(n)
        soma=soma+(2*n)
    print("\nA soma do quadrado dos números é:", soma)

def ex10():
    lista1 = []
    lista2 = []
    vetorF = []
    print("Primeiro vetor")
    for i in range(10):
        n = int(input("Informe um número"))
        lista1.append(n)
    print("Segundo vetor")
    for i in range(10):
        n = int(input("Informe um número"))
        lista2.append(n)
    for i in range(10):
        vetorF.append(lista1[i])
        vetorF.append(lista2[i])
    print(vetorF)

def ex11():
    lista1 = []
    lista2 = []
    lista3 = []
    vetorF = []
    print("Primeiro vetor")
    for i in range(10):
        n = int(input("Informe um número"))
        lista1.append(n)
    print("Segundo vetor")
    for i in range(10):
        n = int(input("Informe um número"))
        lista2.append(n)
    print("Terceiro vetor")
    for i in range(10):
        n = int(input("Informe um número"))
        lista3.append(n)
    for i in range(10):
        vetorF.append(lista1[i])
        vetorF.append(lista2[i])
        vetorF.append(lista3[i])
    print(vetorF)

def ex12():
    listaId = []
    listaAlt = []
    mediaALt=0
    for i in range(2):
        idade = int(input("Informe a idade:"))
        alt = float(input("Informe a altura:"))
        mediaALt+=alt
        listaId.append(idade)
        listaAlt.append(alt)
    mediaALt=mediaALt/2
    cont=0
    for i in range(2):
        if listaId[i]>13:
            if listaAlt[i]<mediaALt:
                cont+=1
    print("A média de altura da turma é:",mediaALt)
    print(cont,"alunos com mais de 13 anos possuem a altura menor que a média")

def ex13():
    temperatura = []
    meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    media = 0
    acimaMedia = []
    mesAcima = []
    for i in range(len(meses)):
        n=float(input('Informe a Temperatura media de ' + meses[i] + ':'))
        temperatura.append(n)
        media += temperatura[i]
    media = media/len(meses)

    for i in range(len(meses)):
        if(temperatura[i] > media):
            acimaMedia.append(temperatura[i])
            mesAcima.append(meses[i])

    print('Media das temperaturas : Anual -> ',media)
    print('Meses com temperaturas acima da media:')
    for i in range(len(acimaMedia)):
        print(mesAcima[i],":",acimaMedia[i])

def ex14():
    lista=[]
    print("Responda s-sim ou n-não")
    p1 = input("Telefonou para a vítima?")
    p2 = input("Esteve no local do crime?")
    p3 = input("Mora perto da vítima?")
    p4 = input("Devia para a vítima?")
    p5 = input("Já trabalhou com a vítima?")
    lista.append(p1)
    lista.append(p2)
    lista.append(p3)
    lista.append(p4)
    lista.append(p5)
    cont=0
    for i in range(len(lista)):
        if lista[i]=="s":
            cont+=1
    if cont==2:
        print("Suspeita")
    elif cont==3 or cont==4:
        print("Cúmplice")
    elif cont==5:
        print("Assassino")
    else:
        print("Inocente")

def ex15():
   notas=[]
   cont=0
   print("Insira as notas. Insira -1 quando finalizar a entrada de notas")
   media=0
   n=0
   while n!=-1:
       n= float(input("Informe a nota:"))
       if n!=-1:
           notas.append(n)
           media+=n
           cont+=1

   print("Foram lidos:",cont,"valores")
   print("Valores:",end=" ")
   for i in notas:
       print(i,end="  ")


   nota2=[]
   f=len(notas)
   print("\nValores ao contrário:")
   for i in range(f):
       d=notas[-1]
       print(d)
       nota2.append(d)
       notas.pop()
   print("A soma dos valores:", media)
   media=media/f
   contMed=0
   contSet=0
   print("A média dos valores:", media)
   for i in nota2:
       if i>media:
           contMed+=1
       elif i<7:
           contSet+=1

   print("Valores ácima da média:", contMed)
   print("Valores abaixo da sete:", contSet)
   print("\nÉ isso aí velhinho...")

def ex16():
    salarios = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699],[700, 799], [800, 899], [900, 999]]
    faixa = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("Digite 0 para encerrar a entrada de dados.")
    vendas = float(input("Digite o valor das vendas:"))

    while vendas != 0:
        salario = (vendas*9/100)+ 200
        if salario < 1000:
            for i in range(8):
                if salario > salarios[i][0] and salario < salarios[i][1]:
                    faixa[i] += 1
        else:
            faixa[8] += 1
        vendas = float(input("Digite o valor das vendas:"))

    for i in range(8):
        print("Entre R$", salarios[i][0], "e R$", salarios[i][1], ":", faixa[i], "vendedores.")
    print("Salarios maiores que R$1000:", faixa[8], "vendedores.")

def ex17():
    saltos = []
    media = 0
    maior = 0
    menor = 10
    nome = input("Informe o nome do atleta:")
    while nome!="":
        for i in range(5):
            s = float(input("Informe o salto:"))
            saltos.append(s)
            if i == 0:
                maior = menor = s
            if s > maior:
                maior = s
            if s < menor:
                menor = s
        print("Atleta:", nome, "\n")
        print("Primeiro salto:", saltos[0], "m")
        print("Segundo salto:", saltos[1], "m")
        print("Terceiro salto:", saltos[2], "m")
        print("Quarto salto:", saltos[3], "m")
        print("Quinto salto:", saltos[4], "m\n")

        print("Melhor salto:", maior, "m")
        print("Pior salto:", menor, "m")
        saltos.remove(maior)
        saltos.remove(menor)
        for i in range(3):
            media += saltos[i]
        media = media / 3
        print("Média dos demias saltos:", media, "m\n")
        print("Resultado Final:")
        print(nome, ":", media, "m\n")
        nome = input("\nInforme o nome do atleta:")

def ex18():
    faixa = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    cont=0
    votos=[]
    lista=[]
    print("Enquete: Quem foi o melhor jogador?\n")
    num = int(input("Número do jogador (0=fim):"))
    while num!=0:
        if num>=1 and num<=23:
            votos.append(num)
            cont+=1
            for i in range(24):
                if num-1==i:
                    faixa[i]+=1
        else:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
        num = int(input("Número do jogador (0=fim):"))
    print("Resultado da votação:\n")
    print("Foram computados",cont,"votos.:\n")
    print("Jogador       Votos         %")
    vt=[]
    jj=[]
    for i in range(len(faixa)):
        if faixa[i]!=0:
            vt.append(faixa[i])
            jj.append(i)
    maior=0
    maiorvt=0
    for i in range(len(jj)):
        print("   ",jj[i]+1,"        ",vt[i],"        ",vt[i]/cont*100)
        if i==0:
            maior=jj[i]
            maiorvt=vt[i]
        elif maiorvt<vt[i]:
            maior=jj[i]
            maiorvt=vt[i]
    maior+=1
    print("O melhor jogador foi o número",maior,", com",maiorvt,"votos, correspondendo a",maiorvt/cont*100,"% do total de votos.")

def ex19():
    faixa = [0,0,0,0,0,0]
    tipos=[' Windows Server','Unix','Linux','Netware','Mac OS','Outro']
    cont=0
    votos=[]
    print("Qual o melhor Sistema Operacional para uso em servidores?\n")
    for i in range(len(tipos)):
        print(i+1,"-",tipos[i])
    num = int(input("Número da opção (0=fim):"))
    while num!=0:
        if num>=1 and num<=6:
            votos.append(num)
            cont+=1
            for i in range(7):
                if num-1==i:
                    faixa[i]+=1
        else:
            print("Informe um valor entre 1 e 6 ou 0 para sair!")
        num = int(input("Número da opção (0=fim):"))


    print("Resultado da votação:\n")
    print("Sistema Operacional       Votos           %")
    vt = []
    jj = []
    for i in range(len(faixa)):
        if faixa[i] != 0:
            vt.append(faixa[i])
            jj.append(i)
    maior = 0
    maiorvt = 0
    print("-------------------     -----   ---")
    for i in range(len(jj)):
        print(tipos[i], "            ", vt[i], "             ", vt[i] / cont * 100)
        if i == 0:
            maior = tipos[i]
            maiorvt = vt[i]
        elif maiorvt < vt[i]:
            maior = tipos[i]
            maiorvt = vt[i]

    print("-------------------     -----   ---")
    print("   Total               ",cont,"\n")
    print("O melhor jogador foi o número", maior, ", com", maiorvt, "votos, correspondendo a", maiorvt / cont * 100, "% do total de votos.")

def ex20():
    cont = 0
    sal = []
    print("Projeção de Gastos com Abono")
    print("============================\n")
    num = float(input("Salário:"))
    contMin=0
    somAbono=0
    maiorAbon=0
    while num != 0:
        if num >= 100:
            sal.append(num)
            cont += 1
        num = float(input("Salário:"))
    print("Salario        -    Abono")
    for i in range(len(sal)):
        abon=sal[i]*20/100
        if abon<=100:
            abon=100
            contMin+=1
        somAbono+=abon
        if i==0:
            maiorAbon=abon
        if maiorAbon<abon:
            maiorAbon=abon
        print("R$",sal[i],"     -   R$  ",abon)
    print("\nForam processados",cont,"colaboradores")
    print("Total gasto com abonos: R$",somAbono)
    print("Valor mínimo pago a",contMin,"colaboradores")
    print("Maior valor de abono pago: R$",maiorAbon)

def ex21():
    tipos=[]
    consumo=[]
    maiorN=0
    maior=0
    for i in range(5):
        print("Veículo",i+1)
        tipo = input("Nome:")
        km = float(input("Km por litro:"))
        tipos.append(tipo)
        consumo.append(km)
    print("\nRelatório Final")
    for i in range(5):
        cons=1000/consumo[i]
        prec=cons*2.25
        if i==0:
            maior=prec
            maiorN=tipos[i]
        if maior>prec:
            maior=prec
            maiorN=tipos[i]
        print(i+1,"-",tipos[i],"          -   ",consumo[i]," - ",cons,"litros  -  R$",prec)
    print("O maior consumo é do",maiorN)

def ex22():
    print("Selecione a opção: ")
    sit=["necessita da esfera","necessita de limpeza","necessita troca do cabo ou conector","quebrado ou inutilizado"]
    cont=0
    mouse=[]
    defeito=[]
    contx=[0,0,0,0]
    num = int(input("Número de identificação:"))
    while num!=0:
        if num>=1 and num<=4:
            defe = int(input("Tipo de defeito:"))
            mouse.append(num)
            defeito.append(defe)
            cont += 1
        else:
            print("Informe um valor entre 1 e 4 ou 0 para sair!")
        num = int(input("Número de identificação:"))
    for i in range(len(mouse)):
        if defeito[i]==1:
            contx[0]+=1
        if defeito[i]==2:
            contx[1]+=1
        if defeito[i]==3:
            contx[2]+=1
        if defeito[i]==4:
            contx[3]+=1
    print("\nQuantidade de mouses:",cont)
    print("\nSituação                             Quantidade                   Percentual")
    for i in range(len(sit)):
        perc=contx[i]/cont*100
        print(i+1,"-",sit[i],"                ",contx[i],"                 ",perc,"%")

def ex23():
    usuarios=[]
    cont = 1
    total = 0
    arquivo=open("usuarios.txt", "r")
    valor = 0
    media=0

    for linha in arquivo:
        usuarios.append(linha.split())

    for usuario in usuarios:
        usuario.insert(0, cont)
        valor = float(usuario[2]) / (1024 * 1024)
        total += valor
        usuario.insert((len(usuario)), valor)
        cont += 1

    for usuario in usuarios:
        percentual = (usuario[3] / total) * 100
        usuario.insert((len(usuario)), percentual)

    elementos = len(usuario)
    media = (total) / (elementos + 1)

    arquivo=open("relatorio.txt", "w")
    arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários.\n")
    arquivo.write("--------------------------------------------------------------\n")
    arquivo.write("Nr. Usuário     Espaço utilizado    % do uso\n\n")

    for usuario in usuarios:
        percentagem = "{0:.2f}".format(round(usuario[3], 2))
        arquivo.write(str(usuario[0])  + "  {:<15}".format(usuario[1])  + "{:<16}".format(percentagem) + 'MB   ' + "{0:.2f}".format(usuario[4]) + '%' + '\n')

    arquivo.write('\nEspaço Total Ocupado: ' + "{0:.2f}".format(total) + ' MB')
    arquivo.write('\nEspaço médio Ocupado: ' + "{0:.2f}".format(media) + ' MB')
    arquivo.close()

    arquivo=open("relatorio.txt", "r")
    print(arquivo.read())

def ex24():
    lista=[]
    for i in range(0,100):
        rand=(randint(1,6))
        lista.append(rand)

    print(lista)
    print("Quantidade de 1=",lista.count(1))
    print("Quantidade de 2=",lista.count(2))
    print("Quantidade de 3=",lista.count(3))
    print("Quantidade de 4=",lista.count(4))
    print("Quantidade de 5=",lista.count(5))
    print("Quantidade de 6=",lista.count(6))

ex24()