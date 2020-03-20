import math

#Lista de Exercícios - Estrutura De Decisão

def ex1():
    num = float(input("Insera uma nota de 0 a 10: "))
    while num<0 or num>10:
        num = float(input("Insera uma nota válida: "))

def ex2():
    nome = input("Informe seu nome de usuário: ")
    senha = input("Informe sua senha: ")
    while nome==senha:
        senha = input("Informe uma senha que seja diferente do nome do usuário: ")

def ex3():
    nome = input("Informe seu nome: ")
    idade= int(input("Informe sua idade: "))
    salario = float(input("Informe seu salário: "))
    sexo= input("Informe o seu sexo: f-feminino m-masculino")
    estadoC= input("informe o seu Estado Civil: s-solteiro c-casado v-viuvo d-divorciado")
    tamNome=len(nome)
    while tamNome<=3:
        print("Nome inválido")
        nome = input("Informe seu nome (ele deve ter mais que 3 caracteres): ")
        tamNome = len(nome)
    while idade<0 and idade>150:
        print("Idade inválida")
        idade = int(input("Informe sua idade (ela deve ser positiva e menor que 150 anos): "))
    while salario<0:
        print("Salário inválido")
        salario = float(input("Informe seu salário (ele deve ser positivo ou igual a 0): "))
    while sexo!="f" and sexo!="m":
        print("Sexo inválido")
        sexo = input("Informe seu sexo (f-feminino m-masculino): ")
    while estadoC!="s" and estadoC!="c" and estadoC!="v" and estadoC!="d":
        print("Estado Civil inválido")
        estadoC = input("Informe seu estado civil ( s-solteiro c-casado v-viuvo d-divorciado): ")

def ex4():
    paisA=80000
    paisB=200000
    taxaA=3
    tavaB=1.5
    ano=0

    while paisA<paisB:
        paisA=paisA+(paisA*taxaA/100)
        paisB=paisB+(paisB*tavaB/100)
        ano+=1

    print("A quantidade de anos necessários para que o número da população do país A ultrapasse ou se iguale a do país B é de",ano,"anos")

def ex5():
    novamente="s"
    while novamente=="s":
        paisA = int(input("Informe a população do País A: "))
        while paisA < 0:
            print("População inválida")
            paisA = int(input("Informe a população do País A (ela deve ser positiva ou igual a 0): "))

        taxaA = int(input("Informe a taxa de Crescimento do País A: "))
        while taxaA < 0:
            print("Taxa inválida")
            taxaA = int(input("Informe a taxa de Cresmento do País A (ela deve ser positiva ou igual a 0): "))

        paisB = int(input("Informe a população do País B: "))
        while paisB < 0:
            print("População inválida")
            paisB = int(input("Informe a população do País B (ela deve ser positiva ou igual a 0): "))

        tavaB = int(input("Informe a taxa de Crescimento do País B: "))
        while tavaB < 0:
            print("Taxa inválida")
            tavaB = int(input("Informe a taxa de Cresmento do País B (ela deve ser positiva ou igual a 0): "))

        ano = 0

        while paisA<paisB:
            paisA=paisA+(paisA*taxaA/100)
            paisB=paisB+(paisB*tavaB/100)
            ano+=1

        print("A quantidade de anos necessários para que o número da população do país A ultrapasse ou se iguale a do país B é de",ano,"anos")
        novamente=input("Deseja realizar a operação novamente? s-sim n-não")

def ex6():
    for i in range(1,21):
        print(i)

def ex61():
    for i in range(1,21):
        print(i, end=" ")

def ex7():
    maior=-99999999
    for i in range(5):
        num = float(input("Insera um número: "))
        if num>maior:
            maior=num
    print('O Maior número é: ', maior)

def ex8():
    soma=0
    for i in range(5):
        num = float(input("Insera um número: "))
        soma+=num
    media=soma/5
    print('O Média é: ', media)

def ex9():
    for i in range(1,51):
        if i%2!=0:
            print(i, end=" ")

def ex10():
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    if num1>num2:
        maior=num1
        menor=num2
    else:
        maior=num2
        menor=num1
    for i in range(menor,maior):
        if type(i)==int:
            print(i, end=" ")

def ex11():
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    soma=0
    if num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1
    for i in range(menor, maior):
        if type(i) == int:
            soma+=i
            print(i, end=" ")
    print("\nSoma dos números:", soma)

def ex12():
    tab = int(input("De qual número você deseja a tabuada? 1 a 10 "))
    while tab<=0 or tab>10:
        tab = int(input("De qual número você deseja a tabuada? 1 a 10 "))
    for i in range(1,11):
        mult=tab*i
        print(tab,"X",i,"=",mult)

def ex13():
    base = int(input("Insira a base: "))
    exp = int(input("Insira o expoente: "))
    pt=1
    for i in range(pt,exp+1):
        pt=pt*base
        #print(base,"^",i,"=",pt)
    print("O valor dessa potência",base,"^",exp,"=", pt)

def ex14():
    par=0
    impar=0
    for i in range(10):
        num = int(input("Insira um número: "))
        if num%2==0:
            par+=1
        else:
            impar+=1
    print("Os qtd de números pares é:",par)
    print("Os qtd de números ímpares é:", impar)

def ex15():
    fib=0
    n=int(input("Fibonacci de qual número:"))
    ult=1
    pen=1
    if n==1 or n==2:
        print("1")
    else:
        for i in range(2,n):
            fib=ult+pen
            pen=ult
            ult=fib
        print(fib)

def ex16():
    fib = 0
    ult = 1
    pen = 1
    if fib == 1 or fib == 2:
        print("1")
    else:
        while fib<=500:
            fib=ult+pen
            pen=ult
            ult=fib
            print(fib)

def ex17():
    fat = int(input("Informe o fatorial:"))
    tfat=1
    i=1
    while i<=fat:
        tfat*=i
        i+=1
    print(tfat)

def ex18():
    n = int(input("Informe a quantidade de números a comparar:"))
    soma=0
    maior=0
    menor=0

    i=1
    while i<=n:
        num = int(input("Informe o valor:"))
        soma+=num
        if i==1:
            maior=menor=num
        else:
            if maior<num:
                maior=num
            else:
                menor=num
        i+=1
    media=soma/num
    print("Media:", media)
    print("Maior número:", maior)
    print("Menor número:", menor)

def ex19():
    n = int(input("Informe a quantidade de números a comparar:"))
    soma = 0
    maior = 0
    menor = 0

    i = 1
    while i <= n:
        num = int(input("Informe o valor:"))
        while num<=0 or num>1000:
            num = int(input("Ops, Informe o valor:"))
        soma += num
        if i == 1:
            maior = menor = num
        else:
            if maior < num:
                maior = num
            else:
                menor = num
        i += 1
    media = soma / num
    print("Media:", media)
    print("Maior número:", maior)
    print("Menor número:", menor)

def ex20():
    op="s"
    while op=="s":
        fat = int(input("Informe o fatorial:"))
        while fat <= 0 or fat>= 16:
            fat = int(input("Ops, Informe o fatorial:"))
        tfat = 1
        i = 1
        while i <= fat:
            tfat *= i
            i += 1
        print(tfat)
        op=input("Deseja realizar a operação novamente: s-sim n-não")

def ex21():
    num = int(input("Informe um número:"))
    mult=0

    for i in range(2, num):
        if (num%i == 0):
            mult += 1

    if (mult == 0):
        print("É primo")
    else:
        print("Não é Primo")

def ex22():
    num = int(input("Informe um número:"))
    mult = 0

    for i in range(2, num):
        if (num % i == 0):
            mult += 1

    if (mult == 0):
        print("É primo")
    else:
        print("Não é primo. Ele é divisível por: ", mult, "múltiplo(s) acima de 2 e abaixo de", num)

def ex23():
    num = int(input("Informe um número:"))
    mult = 0

    for i in range(2, num):
        if (num % i == 0):
            print("Múltiplo de", i)
            mult += 1

    if (mult == 0):
        print("É primo")
    else:
        print("Não é primo. Ele é divisível por: ", mult, "múltiplo(s) acima de 2 e abaixo de", num)

def ex24():
    op="s"
    soma=0
    cont=0
    while op=="s":
        n=int(input("Informe um número:"))
        soma+=n
        cont+=1
        op=input("Deseja informar mais algum número: s-sim n-nao")
    media=soma/cont
    print("A média dos",cont,"valores é",media)

def ex25():
    op = "s"
    soma = 0
    cont = 0
    while op == "s":
        n = int(input("Informe a idade:"))
        soma += n
        cont += 1
        op = input("Deseja informar mais alguma idade: s-sim n-nao")
    media = soma / cont
    if media>=0 and media<=25:
        sit="Jovem"
    elif media>25 and media<=60:
        sit="Adulta"
    else:
        sit="Idosa"
    print("A média das", cont, "idades é", media,"anos, sendo assim a turma é:",sit)

def ex26():
    n = int(input("Informe a quantidade de eleitores:"))
    cand1=0
    cand2=0
    cand3=0
    for i in range(n):
        vt = int(input("Para qual candidato irá seu voto: 1-Cand1 2-Cand2 3-Cnad3"))
        if vt==1:
            cand1+=1
        elif vt==2:
            cand2+=1
        else:
            cand3+=1
    print("O total de votos do Cand1=",cand1)
    print("O total de votos do Cand2=",cand2)
    print("O total de votos do Cand3=",cand3)

def ex27():
    t = int(input("Informe a quantidade de turmas:"))
    soma=0
    for i in range(t):
        a = int(input("Informe a quantidade de alunos da turma:"))
        while a<0 or a>40:
            a = int(input("Ops Turma não pode ter mais que 40 alunos, Informe a quantidade de alunos da turma:"))
        soma += a
    media=soma/t
    print("A média de alunos em cada sala é",media)

def ex28():
    t = int(input("Informe a quantidade de CDs:"))
    soma = 0
    for i in range(t):
        a = float(input("Informe o valor do CD:"))
        soma += a
    media = soma / t
    print("A média de valor dos CDs é de", media)

def ex29():
    vl=1.99
    print("Lojas Quase Dois - Tabela de preços")
    for i in range(1,51):
        vlt=vl*i
        print(i,"- R$",vlt)

def ex30():
    vl = float(input("Informe o Preço do Pão:"))
    print("Preço do Pão: R$",vl)
    print("Panificadora Pão de Ontem - Tabela de preços")
    for i in range(1, 51):
        vlt = vl * i
        print(i, "- R$", vlt)

def ex31():
    op=1
    soma = 0
    pdt=0
    var=[""]
    while op!=0:
        vl = float(input(""))
        if vl==0:
            op=0
        else:
            pdt+=1
            soma+=vl
            var.append(vl)
    lenv=len(var)
    print("Lojas Tabajara")
    for i in range(1,lenv):
        print("Produto", i, ": R$",var[i])
    print("Total: R$",soma)
    dinheiro=float(input(""))
    troco=dinheiro-soma
    print("Troco: R$",troco,"\n ...")
    ex31()

def ex32():
    fat = int(input("Informe o fatorial:"))
    tfat = 1
    i = 1
    print("Fatorial de:",fat)
    print(fat,"! =",fat,end="")
    o = fat-1
    while i <= fat:
        if o!=0:
            print(".",o,end=" ")
        tfat *= i
        i += 1
        o -= 1
    print("=",tfat)

def ex33():
    op="s"
    soma=0
    cont=0
    maior = 0
    menor = 0
    print("Digite 000 quando tiver informado todas as temperaturas")
    while op=="s":
        n=int(input("Informe uma temperatura:"))
        if n==000:
            op="n"
        else:
            soma+=n
            if cont == 1:
                maior = menor = n
            else:
                if maior < n:
                    maior = n
                else:
                    menor = n
        cont+=1
    media=soma/cont
    print("A média das",cont,"temperaturas é",media)
    print("A maior Temperatura foi:",maior,"°C")
    print("A menor Temperatura foi:",menor,"°C")

def ex34():
    num = int(input("Informe um número:"))
    mult = 0

    for i in range(2, num):
        if (num % i == 0):
            mult += 1
    if (mult == 0):
        print("É primo")
    else:
        print("Não é primo")


###TENTAR REFAZER ESSA
def ex35():
    num = int(input("Informe um número:"))
    i=1
    n=num
    while i<=num:
        if (n%i == 0):
            print(n)
        i+=1
        n-=1

def ex36():
    tab=0
    while tab <= 0 or tab > 10:
        tab = int(input("Montar Tabuada de:"))
        com = int(input("Começar por:"))
        ter = int(input("Terminar em:"))
        while ter<com:
            print("Ops, começo maior que o termino")
            com = int(input("Começar por:"))
            ter = int(input("Terminar em:"))
    print("Montar Tabuada de:",tab)
    print("Começar por:",com)
    print("Terminar em",ter)
    print("Vou montar a tabuada de",tab,"começando em",com,"e terminando em",ter,":")
    for i in range(com, ter):
        mult = tab * i
        print(tab, "X", i, "=", mult)

def ex37():
    op = 1
    cont = 0

    somAlt=0
    somPes=0
    maisAlt=0
    maisBai=0
    maisPes=0
    maisMag=0
    codMa=0
    codMBa=0
    codMPe=0
    codMMa=0


    print("Digite 0 quando tiver informado todas as informaçẽos pedidas")
    while op != 0:
        cod = int(input("Informe seu código:"))
        if cod == 0:
            op = 0
        else:
            pes = float(input("Informe seu peso:"))
            alt = float(input("Informe sua altura:"))
            somAlt+=alt
            somPes+=pes
            if cont == 1:
                maisAlt = maisBai = alt
                maisPes = maisMag = pes
                codMMa = codMPe = codMBa = codMa = cod
            else:
                if maisAlt < alt:
                    maisAlt = alt
                    codMa = cod
                if maisPes < pes:
                    maisPes= pes
                    codMPe= cod
                if maisBai > alt:
                    maisBai = alt
                    codMBa= cod
                if maisMag > pes:
                    maisMag =pes
                    codMMa = cod
            cont += 1
    mediapes = somPes / cont
    mediaalt = somAlt/cont
    print("A média das", cont, "alturas é", mediaalt)
    print("A média dos", cont, "pesos é", mediapes)
    print("O cliente mais Alto:", codMa)
    print("O cliente mais Baixo:", codMBa)
    print("O cliente mais Gordo:", codMPe)
    print("O cliente mais Magro:", codMMa)

def ex38():
    ano=1996
    salarioIni=1000
    aumento=1.5
    salariot=salarioIni+(salarioIni*aumento/100)
    anos=2020-ano
    for i in range(anos):
        aumento=aumento*2
        salariot=salariot+(salariot*aumento/100)
    print("O salário com os novos ajustes é de: R$", salariot)

def ex381():
    ano=1996
    salarioIni=float(input("Informe o slário inicial:"))
    aumento=1.5
    salariot=salarioIni+(salarioIni*aumento/100)
    anos=2020-ano
    for i in range(anos):
        aumento=aumento*2
        salariot=salariot+(salariot*aumento/100)
    print("O salário com os novos ajustes é de: R$", salariot)

def ex39():
    cont = 1
    maisAlt = 0
    maisBai = 0
    codMa = 0
    codMBa = 0
    while cont<=10:
        cod = int(input("Informe seu código:"))
        alt = int(input("Informe sua altura:"))
        if cont == 1:
            maisAlt = maisBai = alt
            codMBa = codMa = cod
        else:
            if maisAlt < alt:
                maisAlt = alt
                codMa = cod
            if maisBai > alt:
                maisBai = alt
                codMBa = cod
        cont += 1
    print("O cliente mais Alto:", codMa,"com altura de",maisAlt)
    print("O cliente mais Baixo:", codMBa,"com altura de",maisBai)

def ex40():
    cont = 1
    masAci = 0
    menosAci = 0
    codMasAcid = 0
    codMenAcid = 0
    somaAcid=0
    somaVeic=0
    somaAcid2 = 0
    contcity=0
    while cont<=5:
        cod = int(input("Informe o código da cidade:"))
        veic = int(input("Informe a quantidade de veículos em 1999:"))
        acid = int(input("Informe a quantidade de acidentes com vítimas em 1999: "))
        somaVeic += veic
        if veic<2000:
            contcity+=1
            somaAcid2 += acid
        if cont == 1:
            masAci = menosAci = acid
            codMasAcid = codMenAcid = cod
        else:
            if masAci < acid:
                masAci = acid
                codMasAcid = cod
            if menosAci > acid:
                menosAci = acid
                codMenAcid = cod
        cont += 1
    mediaVeic=somaVeic/5
    mediaAcid2=somaAcid/contcity
    print("A cidade com maior índice de Acidentes é:", codMasAcid,"com",masAci,"acidentes")
    print("A cidade com menor índice de Acidentes é:", codMenAcid,"com",menosAci,"acidentes")
    print("A média de véiculos nas cinco cidades é:",mediaVeic)
    print("A média de acidentes nas cidades com menos de 2000 veículos é:", mediaAcid2)

def ex41():
    divini = float(input("Informe o valor da dívida:"))
    parc=0
    juros=0
    div=divini
    print("Valor Dívida           Juros              Qtd Parcelas             Valor Parcela")
    for i in range(1,13):
        parc+=1
        if i==1 or i==3 or i==6 or i==9 or i==12:
            if i==1:
                juros=0
            elif i==3:
                juros=10
            else:
                juros=juros+5
            vlParcela = div / parc
            vljuros = div * juros / 100
            div += vljuros
            print("R$",div,"            ",vljuros,"           ",parc,"                R$",vlParcela)
            div= divini

def ex42():
    n=0
    int1=0
    int2=0
    int3=0
    int4=0
    while n>=0:
        n = int(input("Informe um inteiro positivo:"))
        if n<0:
            n=n
        else:
            if n>=0 and n<=25:
                int1+=1
            elif n>25 and n<=50:
                int2+=1
            elif n>50 and n<=75:
                int3+=1
            else:
                int4+=1
    print("No intervalo [0-25]:",int1)
    print("No intervalo [26-50]:",int2)
    print("No intervalo [51-75]:",int3)
    print("No intervalo [76-100]:",int4)

def ex43():
    n = 1
    preco100=1.2
    preco101=1.3
    preco102=1.5
    preco103=1.2
    preco104=1.3
    preco105=1
    totalGeral=0
    precot100 = 0
    precot101 = 0
    precot102 = 0
    precot103 = 0
    precot104 = 0
    precot105 = 0
    while n != 0:
        n = int(input("Informe o código do item:"))
        if n == 0:
            n = n
        else:
            qtd = int(input("Informe o quantidade de compra do item:"))
            if n==100:
                precot100+=preco100*qtd
                totalGeral+=precot100
            elif n==101:
                precot101+=preco101*qtd
                totalGeral+=precot101
            elif n==102:
                precot102+=preco102*qtd
                totalGeral+=precot102
            elif n==103:
                precot103 += preco103 * qtd
                totalGeral += precot103
            elif n==104:
                precot104+=preco104*qtd
                totalGeral+=precot104
            elif n==105:
                precot105 += preco105 * qtd
                totalGeral += precot105
    print("O preço Total de Cachorro quente é de: R$",precot100)
    print("O preço Total de Bauru Simples é de: R$",precot101)
    print("O preço Total de Bauru com ovo  é de: R$",precot102)
    print("O preço Total de Hambúrguer  é de: R$",precot103)
    print("O preço Total de Cheeseburguer  é de: R$",precot104)
    print("O preço Total de Refrigerante  é de: R$",precot105)
    print("O preço Total da Compra foi de: R$",totalGeral)

def ex44():
    n = 1
    totalGeral = 0
    vt1 = 0
    vt2 = 0
    vt3 = 0
    vt4 = 0
    vt5 = 0
    vt6 = 0
    print("-------Votação-------")
    print("Número      Candidato")
    print("  1            José")
    print("  2            João")
    print("  3            Maria")
    print("  4            Marta")
    print("  5            Nulo")
    print("  6            Branco")
    print("Obs.: 0 para encerrar eleição")
    while n != 0:
        n = int(input("Informe o número do candidato"))
        if n == 0:
            n = n
        else:
            totalGeral+=1
            if n==1:
                vt1+=1
            elif n==2:
                vt2+=1
            elif n==3:
                vt3+=1
            elif n==4:
                vt4+=1
            elif n==5:
                vt5+=1
            elif n==6:
                vt6+=1
    print("-------Votação-------")
    print("Número de Votos      Candidato")
    print("  ",vt1,"                  José")
    print("  ",vt2,"                  João")
    print("  ",vt3,"                  Maria")
    print("  ",vt4,"                  Marta")
    print("  ",vt5,"                  Nulo")
    print("  ",vt6,"                  Branco")
    percNulo=(vt5/totalGeral)*100
    percBranc=(vt6/totalGeral)*100
    print("Percentual de Votos Nulos=",percNulo,"%")
    print("Percentual de Votos em Branco=",percBranc,"%")

def ex45():
    continuar = "s"
    respostas =  ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    media = 0
    totalAlunos=0
    maior=0
    menor=10
    while continuar=="s":
        nota=0
        erros=0
        for resposta in respostas:
            q = input("Informe a resposta da questão:").upper()
            if resposta==q:
                nota+=1
            else:
                erros+=1
        totalAlunos+=1
        media+=nota
        if nota>maior:
            maior=nota
        if erros<menor:
            menor=erros
        continuar = input('Deseja continuar a usar o programa? Digite s-sim n-não\n')

    media=media/totalAlunos
    print(totalAlunos,"alunos usaram o sistema")
    print("A maior quantidade de acertos:",maior)
    print("A menor quantidade de acertos:",menor)
    print("A média da turma foi:",media)

def ex451():
    continuar = "s"
    respostas=[]
    for i in range(10):
        q = input("Informe o gabarito:").upper()
        respostas.append(q)
    media = 0
    totalAlunos=0
    maior=0
    menor=10
    while continuar=="s":
        nota=0
        erros=0
        for resposta in respostas:
            q = input("Informe a resposta da questão:").upper()
            if resposta==q:
                nota+=1
            else:
                erros+=1
        totalAlunos+=1
        media+=nota
        if nota>maior:
            maior=nota
        if erros<menor:
            menor=erros
        continuar = input('Deseja continuar a usar o programa? Digite s-sim n-não\n')

    media=media/totalAlunos
    print(totalAlunos,"alunos usaram o sistema")
    print("A maior quantidade de acertos:",maior)
    print("A menor quantidade de acertos:",menor)
    print("A média da turma foi:",media)

def ex46():
    saltos = []
    media = 0
    maior = 0
    menor = 10
    nome=input("Informe o nome do atleta:")
    for i in range(5):
        s = float(input("Informe o salto:"))
        saltos.append(s)
        if i==0:
            maior=menor=s
        if s>maior:
            maior=s
        if s<menor:
            menor=s
    print("Atleta:",nome,"\n")
    print("Primeiro salto:", saltos[0],"m")
    print("Segundo salto:", saltos[1],"m")
    print("Terceiro salto:", saltos[2],"m")
    print("Quarto salto:", saltos[3],"m")
    print("Quinto salto:", saltos[4],"m\n")

    print("Melhor salto:", maior,"m")
    print("Pior salto:", menor, "m")
    saltos.remove(maior)
    saltos.remove(menor)
    for i in range(3):
        media+=saltos[i]
    media=media/3
    print("Média dos demias saltos:", media, "m\n")
    print("Resultado Final:")
    print(nome,":",media,"m\n")

def ex47():
    notas = []
    media = 0
    maior = 0
    menor = 10
    nome = input("Informe o nome do atleta:")
    for i in range(7):
        s = float(input("Informe a nota do atleta:"))
        notas.append(s)
        if i == 0:
            maior = menor = s
        if s > maior:
            maior = s
        if s < menor:
            menor = s
    print("Atleta:", nome, "\n")
    for i in range(7):
        print("Nota:", notas[i])

    print("\nResultado Final:")
    print("Atleta:",nome)
    print("Melhor nota:", maior)
    print("Pior nota:", menor)
    notas.remove(maior)
    notas.remove(menor)
    for i in range(5):
        media += notas[i]
    media = media/5
    print("Média:", media)

def ex48():
    n = int(input("Informe um número:"))
    s = str(n)
    d=len(s)
    l=[]
    for i in range(d):
        l.append(s[i])
    for i in range(d):
        print(l[-1],end="")
        l.pop()

def ex49():
    n=int(input("Informe um número:"))
    m=1
    o=1
    s=0
    for i in range(n):
        s+=(o/m)
        o+=1
        m+=2
    print("A Soma das divisões de S é:",s)

def ex50():
    n = int(input("Informe um número:"))
    m = 1
    o = 1
    s = 0
    for i in range(n):
        s += (o / m)
        m += 1
    print("A Soma das divisões de H é:", s)

def ex51():
    n = int(input("Informe um número:"))
    m = 1
    o = 1
    s = 0
    print("S=",end="")
    for i in range(n):
        s += (o / m)
        if i==n-1:
            print(o, "/", m)
        else:
            print(o,"/",m,"+",end=" ")
        o += 1
        m += 2
    print("\nA Soma das divisões de S é:", s)

ex51()