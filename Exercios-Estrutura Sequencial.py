import math

#Lista de Exercícios - Estrutura Sequencial

def ex1():
    print("Alo mundo")

def ex2():
    num= int(input("Insera um número: "))
    print("O número informado foi: ", num)

def ex3():
    num= int(input("Insera um número: "))
    num2= int(input("Insera outro número: "))
    soma=num+num2
    print("A soma dos dois números é: ", soma)

def ex4():
    nota1= int(input("Insera a primeira nota: "))
    nota2= int(input("Insera a segunda nota: "))
    nota3= int(input("Insera a terceira nota: "))
    nota4= int(input("Insera a quarta nota: "))
    media= (nota1+nota2+nota3+nota4)/4
    print("A média das quatro notas é: ", media)

def ex5():
    metros= float(input("Insera o valor em metros: "))
    centimetros= metros*100
    print("O valor em centimetros é: ", centimetros)

def ex6():
    raio= float(input("Insera o valor do raio do círculo: "))
    area= 3.14*(raio**2)
    print("O valor em centimetros é: ", area)


def ex7():
    lado= float(input("Insera o valor do lado do quadrado: "))
    area= 2*(lado*lado)
    print("O dobro do valor da área do quadrado é: ", area)

def ex8():
    ganhoHora= float(input("Quanto você ganha por hora: "))
    horasTrab = float(input("Quantas horas vc trabalha no mês: "))
    salario= ganhoHora*horasTrab
    print("O valor do seu salário é: ", salario)

def ex9():
    farenheit= float(input("Insira a temperatura em farenheit: "))
    celsius= (5*(farenheit-32)/9)
    print("A temperatura em Celsius é: ", celsius)

def ex10():
    celsius= float(input("Insira a temperatura em celsius: "))
    farenheit= ((celsius*1.8)+32)
    print("A temperatura em Farenheit é: ", farenheit)

def ex11():
    inteiro1= int(input("Insira um número inteiro: "))
    inteiro2 = int(input("Insira outro número inteiro: "))
    real = float(input("Insira um número real: "))
    a= ((2*inteiro1)+(inteiro2/2))
    b= ((3*inteiro1)+real)
    c= (real**3)
    print("O produto do dobro do primeiro com metade do segundo é: ", a)
    print("A soma do triplo do primeiro com o terceiro é:", b)
    print("O terceiro elevado ao cubo é:", c)

def ex12():
    altura= float(input("Insira a sua altura: "))
    pesoId= ((72.7*altura)-58)
    print("O seu peso ideal é: ", pesoId)

def ex13():
    altura= float(input("Insira a sua altura: "))
    pesoIdH= ((72.7*altura)-58)
    pesoIdM= ((62.1*altura)-44.7)
    print("O seu peso ideal se for Homem é: ", pesoIdH)
    print("O seu peso ideal se for Mulher é: ", pesoIdM)

def ex14():
    peso= float(input("Insira o valor do peso: "))
    excesso=peso-50
    multa=excesso*4
    if(multa>0):
        print("O valor da multa é: ", multa)
    else:
        print("Não há multas")

def ex15():
    ganhoHora = float(input("Quanto você ganha por hora: "))
    horasTrab = float(input("Quantas horas vc trabalha no mês: "))
    a = ganhoHora * horasTrab
    b = a*11/100
    c = a*8/100
    d = a*5/100
    e = a-(b+c+d)
    print("+ Salário Bruto: R$ ", a)
    print("- IR (11%): R$ ", b)
    print("- INSS (8%): R$ ", c)
    print("- Sindicato (5%): R$ ", d)
    print("= Salário Líquido: R$ ", e)

def ex16():
    metros= float(input("Insira o valor em metros quadrados da área pintada: "))
    litros=metros/3
    latas=litros/18
    valor=latas*80
    print("Quantidade de latas =", latas," valor total=", valor)

def ex17():
    metros= float(input("Insira o valor em metros quadrados da área pintada: "))
    litros=metros/6
    latas=litros/18
    galoes=litros/3.6
    valor=latas*80
    valorg=galoes*25
    a1= math.ceil(int(litros/18))
    a2 = litros%18
    a3 =math.ceil((a2 / 3.6))
    a4 = round(((a1 * 80) + (a3 * 25)))
    a5 = (a4+(a4*10/100))

    print("Quantidade de litros: ",litros)
    print("Apenas Latas de 18L: \nQuantidade de latas =", latas," valor total=", valor)
    print("Apenas Galões de 3.6L: \nQuantidade de galões =", galoes, " valor total=", valorg)
    print("Com Galões e Latas, menor preço: \n latas",a1,"galoes", a3, "pagar aproximadamente", a5)

def ex18():
    tamanho= float(input("Insira o tamanho do arquivo em MB: "))
    internet = float(input("Insira a velocidade de link da internet em Mbps: "))
    tempo=tamanho/(internet*60)
    print("Tempo aproximado de download é de", tempo,"min")

ex18()
