import math

#Lista de Exercícios - Estrutura De Decisão

def ex1():
    num= int(input("Insera o primeiro número: "))
    num2= int(input("Insera o segundo número: "))
    if num>num2:
        print("O número ",num," é maior que o número ", num2)
    else:
        if num2 > num:
            print("O número ", num2, " é maior que o número ", num)
        else:
            print("O número ", num2, " é igual ao número ", num)

def ex2():
    num= int(input("Insera o valor: "))
    if num>0:
        print("O número ",num," é positivo")
    else:
        if num < 0:
            print("O número ", num, " é negativo")
        else:
            print("O número é igual a 0")

def ex3():
    letra= input("Insera F ou M: ")
    if letra=="F":
        print("F - Feminino")
    elif letra=="M":
        print("M - Masculino")
    else:
        print("Sexo Inválido")

def ex4():
    letra = input("Insera uma letra: ")
    if letra == "a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        print("Vogal")
    else:
        print("Consoante")

def ex5():
    nota1 = float(input("Insera a primeira nota: "))
    nota2 = float(input("Insera a segunda nota: "))
    media= (nota1+nota2)/2
    if media<7:
        print("Reprovado")
    else:
        if media>=10:
            print("Aprovado com Distinção")
        else:
            print("Aprovado")

def ex6():
    num1 = float(input("Insera o primeiro número: "))
    num2 = float(input("Insera o segundo número: "))
    num3 = float(input("Insera o terceiro número: "))
    maior = num1
    if (num2 > maior):
        maior = num2
    if (num3 > maior):
        maior = num3

    print('O Maior número é: ', maior)

def ex7():
    num1 = float(input("Insera o primeiro número: "))
    num2 = float(input("Insera o segundo número: "))
    num3 = float(input("Insera o terceiro número: "))
    maior = num1
    if (num2 > maior):
        maior = num2
    if (num3 > maior):
        maior = num3

    menor = num1
    if (num2 < menor):
        menor = num2
    if (num3 < menor):
        menor = num3

    print('O Maior número é: ', maior)
    print('O Menor número é: ', menor)

def ex8():
    preco1 = float(input("Insera o primeiro preço: "))
    preco2 = float(input("Insera o segundo preço: "))
    preco3 = float(input("Insera o terceiro preço: "))
    menor = preco1

    if (preco2 < menor):
        menor = preco2
    if (preco3 < menor):
        menor = preco3

    print('O Menor preço é: ', menor)

def ex9():
    num1 = float(input("Insera o primeiro número: "))
    num2 = float(input("Insera o segundo número: "))
    num3 = float(input("Insera o terceiro número: "))

    if (num3 > num2):
        aux = num3
        num3 = num2
        num2 = aux

    if (num2 > num1):
        aux = num2
        num2 = num1
        num1 = aux

    if (num3 > num2):
        aux = num3
        num3 = num2
        num2 = aux

    print(num1, '-', num2, '-', num3)

def ex10():
    turno = input("Insera seu Turno de Estudo: M-matutino ou V-Vespertino ou N- Noturno: ")
    if turno=="M":
        print("Bom dia!")
    elif turno=="V":
        print("Boa Tarde!")
    elif turno=="N":
        print("Boa Noite!")
    else:
        print("Valor Inválido")

def ex11():
    salario = float(input("Insira o valor do seu salário: "))
    if salario<=280:
        percentual=20
    elif salario>280 and salario<700:
        percentual = 15
    elif salario>700 and salario<1500:
        percentual=10
    else:
        percentual=5
    aumento=(salario*percentual/100)
    nsalario=salario+aumento
    print("Salário Anterior= R$",salario)
    print("Percentual aplicado=", percentual,"%")
    print("Valor do aumento= R$",aumento)
    print("Valor do Novo Salário= R$",nsalario)

def ex12():
    ganhoHora = float(input("Quanto você ganha por hora: "))
    horasTrab = float(input("Quantas horas vc trabalha no mês: "))
    slBrut = ganhoHora * horasTrab
    if slBrut<=900:
        ir=0
    elif slBrut<=1500:
        ir=5
    elif slBrut<=2500:
        ir=10
    else:
        ir=20
    calcir = slBrut*ir/100
    inss = slBrut*10/100
    fgts = slBrut*11/100
    desc=calcir+inss
    liq = slBrut-desc
    print("+ Salário Bruto (",ganhoHora,"*",horasTrab,") : R$ ", slBrut)
    print("- IR (",ir,"%): R$ ", calcir)
    print("- INSS (10%): R$ ", inss)
    print("FGTS (11%): R$ ", fgts)
    print("Total dos descontos: R$ ", desc)
    print("= Salário Líquido: R$ ", liq)

def ex13():
    num = float(input("Insira um número: "))
    if num==1:
        print("1-Domingo")
    elif num == 2:
        print("2-Segunda")
    elif num == 3:
        print("3-Terça")
    elif num == 4:
        print("4-Quarta")
    elif num == 5:
        print("5-Quinta")
    elif num == 6:
        print("6-Sexta")
    elif num == 7:
        print("7-Sabádo")
    else:
        print("Valor Inválido")

def ex14():
    nota1 = float(input("Insera a primeira nota: "))
    nota2 = float(input("Insera a segunda nota: "))
    media= (nota1+nota2)/2
    if media>=9 and media<=10:
        conceito="A"
    elif media>=7.5 and media<9:
        conceito = "B"
    elif media>=6 and media<7.5:
        conceito = "C"
    elif media >= 4 and media<6:
        conceito = "D"
    else:
        conceito="E"

    if conceito=="A" or conceito=="B" or conceito=="C":
        situacao="APROVADO"
    else:
        situacao="REPROVADO"
    print("Primeira Nota=",nota1,"Segunda Nota=",nota2,"Média=",media,"Conceito=",conceito," - ", situacao)


def ex15():
    lado1 = float(input("Insera o primeiro lado: "))
    lado2 = float(input("Insera o segundo lado: "))
    lado3 = float(input("Insera o terceiro lado: "))

    if not (lado1+lado2)> lado3 and (lado1+lado3)>lado2 and (lado2+lado3)>lado1:
        print("É impossivel ser um triângulo")
    elif lado1 == lado2 and lado1 == lado3:
            print("Triângulo Equilátero")
    elif lado1 != lado2 and lado1!=lado3 and lado2!=lado3:
            print("Triângulo Escaleno")
    else:
            print("Triângulo Isósceles")

def ex16():
    print("Formula = ax2+bx+c")
    a = float(input("Insera o valor de a: "))
    if a!=0:
        b = float(input("Insera o valor de b: "))
        c = float(input("Insera o valor de c: "))

        delta= (b**2)-(4*a*c)
        if delta<=0:
            print("A equação não possui raizes reais")
        else:
            r1 = (-b + math.sqrt(delta)) / (2 * a)
            r2 = (-b - math.sqrt(delta)) / (2 * a)
            print('Raizes:  ', r1, ' e ', r2)
    else:
        print("Não é uma equação de segundo grau")

def ex17():
    ano = int(input("Insera o ano: "))
    if (ano%4==0 and ano%100!=0) or (ano%400 == 0):
        print('Bissexto')
    else:
        print('Não é bissexto')

def ex18():
    dia=int(input("Insera o dia: "))
    mes=int(input("Insera o mês: "))
    ano=int(input("Insera o ano: "))

    dtV=False
    if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and mes>0:
        if (dia<=31) and dia>0:
            dtV=True
    elif (mes==4 or mes==6 or mes==9 or mes==11) and mes>0:
        if (dia <= 30) and dia>0:
            dtV=True
    elif mes==2:
        if (ano%4==0 and ano%400!=0) or (ano%400==0):
            if (dia<= 29) and dia>0:
                dtV = True
        elif (dia<=28) and dia>0:
            dtV = True

    if(dtV):
        print("Data Válida")
    else:
        print("Data Inválida")

def ex19():
    num=int(input("Insera um número menor que 1000: "))
    numStr = str(num)
    tam = len(numStr)

    if num>=1000:
        print("Esse número é maior ou igual a 1000")
    else:
        if tam == 3:
            centena = numStr[0:1]
            dezena = numStr[1:2]
            unidade = numStr[2:3]
            c = "centenas"
            if centena == "1":
                c = "centena"
            d = "dezenas"
            if dezena == "1":
                d = "dezena"
            u = "unidades"
            if unidade == "1":
                u = "unidade"
            print(num,"=",centena,c,dezena,d,"e",unidade,u)

        if tam == 2:
            dezena = numStr[0:1]
            unidade = numStr[1:2]
            d = "dezenas"
            if dezena == "1":
                d = "dezena"
            u = "unidades"
            if unidade == "1":
                u = "unidade"
            print(num,"=" ,dezena,d,"e",unidade,u)

        if tam == 1:
            unidade = numStr[0:1]
            u = "unidades"
            if unidade == "1":
                u = "unidade"
            print(num,"=",unidade, u)

def ex20():
    nota1 = float(input("Insera a primeira nota: "))
    nota2 = float(input("Insera a segunda nota: "))
    nota3 = float(input("Insera a terceira nota: "))
    media= (nota1+nota2+nota3)/3
    if media>10:
        situacao="Aprovado com Distinção"
    elif media<=10 and media>=7:
        situacao="Aprovado"
    else:
        situacao="Reprovado"
    print(situacao,"com média", media)

def ex21():
    valor = int(input('Valor para sacar de 10 a 600: '))
    if valor>=10 and valor<=600:
        cem = int(valor/100)
        valor = valor-(cem*100)
        cinquenta = int(valor/50)
        valor = valor-(cinquenta*50)
        dez = int(valor/10)
        valor = valor-(dez*10)
        cinco = int(valor/5)
        valor = valor-(cinco*5)
        um = valor

        print('Notas R$100,00 = ', cem)
        print('Notas R$ 50,00 = ', cinquenta)
        print('Notas R$ 10,00 = ', dez)
        print('Notas R$  5,00 = ', cinco)
        print('Notas R$  1,00 = ', um)
    else:
        print("O valor é inválido")

def ex22():
    num = int(input('Insira o número: '))
    if num%2==0:
        print("O número é par")
    else:
        print("É ímpar")

def ex23():
    num = float(input('Insira o número: '))
    n=round(num)
    if n==num:
        print("num é inteiro")
    else:
        print("num é decimal")

def ex24():
    num1 = float(input('Insira o primeiro número: '))
    num2 = float(input("Insira o segundo número"))
    op=int(input("Escolha uma operação: 1-par ou ímpar 2-positivo ou negativo 3-inteiro ou decimal"))
    def op1(num):
        if num % 2 == 0:
            print("O número",num," é par")
        else:
            print("O número", num, " é ímpar")
    def op2(num):
        if num>=0:
            if num==0:
                print("O número", num, " é zero")
            print("O número",num," é positivo")
        else:
            print("O número", num, " é negativo")
    def op3(num):
        n = round(num)
        if n == num:
            print("O número",num," é inteiro")
        else:
            print("O número",num,"é decimal")
    if op==1:
        op1(num1)
        op1(num2)
    elif op==2:
        op2(num1)
        op2(num2)
    else:
        op3(num1)
        op3(num2)

def ex25():
    print("responda com s - sim ou n - não")
    p1=input("Telefonou para a vítima?")
    p2=input("Esteve no local do crime?")
    p3=input("Mora perto da vítima?")
    p4=input("Devia para a vítima?")
    p5=input("Já trabalhou com a vítima?")

    count=0
    if p1=="s":
        count += 1
    if p2=="s":
        count += 1
    if p3=="s":
        count += 1
    if p4=="s":
        count += 1
    if p5=="s":
        count += 1

    if count==2:
        print("Suspeita")
    elif count==3 or count==4:
        print("Cúmplice")
    elif count==5:
        print("Assassino")
    else:
        print("Inocente")

def ex26():
    comb=input("Qual o Tipo de Compustivel A-álcool G-gasolina: ")
    litros=float(input("Insira a quantidade de Litros?"))
    pGas = 2.50
    pAlc = 1.90
    if comb=="A":
        if litros<=20:
            desc=3
        else:
            desc=5
        valc = pAlc * litros
        vldesc=valc*desc/100
        vtalc=valc-vldesc
        print("O valor a ser pago é de R$", vtalc)
    else:
        if litros<=20:
            desc=4
        else:
            desc=6
        vgas=pGas*litros
        vldesc = vgas * desc / 100
        vtgas = vgas - vldesc
        print("O valor a ser pago é de R$", vtgas)

def ex27():
    kilosMo = float(input("Insira a quantidade de Kilos de Morango?"))
    kilosMa = float(input("Insira a quantidade de Kilos de Maça?"))

    if kilosMo>5:
        valorMo=kilosMo*2.2
    else:
        valorMo=kilosMo*2.5
    if kilosMa>5:
        valorMa=kilosMa*1.5
    else:
        valorMa=kilosMa*1.8

    vt=valorMo+valorMa
    if kilosMa>8 or kilosMo>8 or vt>25 or vt>25:
        vt=vt-(vt*10/100)

    print("O valor total é de R$", vt)

def ex28():
    tipoCarne = input("O que você está comprando? F-File Duplo A-Alcatra P-Picanha")
    kilosCarne = float(input("Insira a quantidade de Kilos de Carne que você está comprando!"))
    cartao = input("Você irá pagar no cartão? s-sim n-não")

    if tipoCarne=="F":
        if kilosCarne>5:
            pCarne=5.8
        else:
            pCarne=4.9
    elif tipoCarne=="A":
        if kilosCarne>5:
            pCarne=6.8
        else:
            pCarne=5.9
    else:
        if kilosCarne > 5:
            pCarne = 7.8
        else:
            pCarne = 6.9

    vtCarne = kilosCarne*pCarne
    if cartao=="s":
        vtCarne=vtCarne-(vtCarne*5/100)

    print("O valor total é de R$", vtCarne)



ex28()