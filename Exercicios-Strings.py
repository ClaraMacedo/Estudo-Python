import random
def ex1():
    def qtd(n):
        return len(n)
    s = input("Informe a primeira String:")
    s1 = input("Informe a segunda String:")
    d=qtd(s)
    d1=qtd(s1)
    print("A quantidade de caracteres de '",s,"' é:",d)
    print("A quantidade de caracteres de '",s1,"' é:",d1)
    if d == d1:
        print("As duas strings são de tamanhos iguais")
    else:
        print("As duas strings são de tamanhos diferentes")
    if s==s1:
        print("As duas strings possuem conteúdo igual")
    else:
        print("As duas strings possuem conteúdo diferente")

def ex2():
    def inverte(n):
        return n[::-1]
    n = input("Informe uma palavra:")
    print("O inverso da palavra é:",inverte(n).upper())

def ex3():
    n = input("Informe uma palavra:")
    for i in n:
        print(i.upper())

def ex4():
    n = input("Informe uma palavra:")
    for i in range(0, len(n)+1):
        for j in range(i):
            print(n[j].upper(),end="")
        print("")

#REFAZER
def ex5():
    n = input("Informe uma palavra:")
    o=len(n)
    s=""
    for i in range(o):
        for j in range(i):
            h=n[0:-j]
            print(h)
        print("")

def ex6():
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
                print("Você nasceu em",d,"de",mes,"de",a)
        else:
            print("Dia inválido")
    n = int(input("Informe o DIA:"))
    n1 = int(input("Informe o MES:"))
    n2 = int(input("Informe o ANO:"))
    extenso(n, n1, n2)

def ex7():
    space=0
    vogais=0
    palavra=input("informe a palavra:")
    for i in palavra:
        if i==" ":
            space+=1
        elif i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            vogais+=1
    print("Espaços:",space)
    print("Vogais:",vogais)

def ex8():
    palavra = input("informe a palavra ou frase:")
    palavra=palavra.replace(" ","")
    tam=len(palavra)
    normal=palavra[0:tam]
    inverso=palavra[tam::-1]

    if normal==inverso:
        print("Essa frase é um palíndromo")
    else:
        print("Essa frase não é um palíndromo")

def ex9():
    cpf = input("CPF(xxx.xxx.xxx-xx) :")
    if (cpf[3] != ".") or (cpf[7] != ".") or (cpf[11] != "-"):
        cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")
    else:
        print("O 'CPF' está no formato correto")

def ex10():
    nums=["um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","desenove"]
    casas=["vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]

    num=int(input("insira um número até 99:"))
    s=str(num)
    for i in range(len(s)):
        if len(s)==1 and i==0:
            print(nums[num-1])
        elif len(s)==2 and i==0:
            if num>=10 and num<=19:
                print(nums[num-1])
            else:
                if i==0:
                    o=int(s[i])-2
                    p=int(s[1])-1
                    print(casas[o],"e",nums[p])

def ex11():
    arq = open("palavras.txt", "r")
    conteudo=arq.read()
    palavras = conteudo.split(" ")

    palavra = palavras[random.randrange(0, len(palavras))]
    palavra = palavra.lower()
    palavra_forca = ["_" for i in palavra]
    chance = 1
    while (chance < 7 and palavra_forca.count("_") != 0):
        letra = input("Digite uma letra: ")
        if (letra in palavra):
            print("A palavra é: ", end=" ")
            for p in range(len(palavra)):
                if letra == palavra[p]:
                    del palavra_forca[p]
                    palavra_forca.insert(p, letra)
                    print("".join(palavra_forca))
        else:
            print("-> Você errou pela " + str(chance) + "a vez. Tente de novo!")
            chance = chance + 1
    if palavra_forca.count("_") == 0:
        print("Parabéns! Você acertou a palavra.")
    else:
        print("Forca! Fim de jogo.")
        print("A palavra era:",palavra)

#VERIFICAR PARTE DO HÍFEN
def ex12():
    num = input("Telefone:")
    s=str(num)
    letra=""
    if len(s)==8:
        print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
        letra="3"+s
    print("Telefone corrigido sem formatação:",letra)
    print("Telefone corrigido com formatação",letra)

def ex13():
    arq = open("palavras.txt", "r")
    conteudo=arq.read()
    palavras = conteudo.split(" ")

    palavra = palavras[random.randrange(0, len(palavras))]
    palavra = palavra.lower()
    tam=len(palavra)
    emb=random.sample(palavra,tam)
    print(emb)
    chance = 1
    cont=0
    acert=0
    while chance < 7:
        letra = input("Qual é a palavra: ")
        if letra != palavra:
            print("-> Você errou pela " + str(chance) + "a vez. Tente de novo!")
            cont+=1
            chance = chance + 1
        else:
            acert+=1
            print("Parabéns! Você acertou a palavra.")
            break
    if acert==0:
        print("Você errou")
        print("A palavra era:", palavra)

def ex14():
    replacements = (('a', '4'), ('e', '3'), ('i', '1'), ('o', '0'), ('u', 'v'))
    my_string = input("Digite o texto:")
    new_string = my_string
    for old, new in replacements:
        new_string = new_string.replace(old, new)

    print(new_string)


ex14()