def ex1():
    class Bola:
        def __init__(self, color="unknown", circunf=0, material="unknown"):
            self.color = color
            self.circunf = circunf
            self.material = material

        def trocaCor(self):
            mudar= input("Deseja mudar a cor atual? s-sim n-não")

            mudar = mudar.lower()

            if mudar == "s":
                nova_cor = input("\n> Nova Cor: ")
                self.color = nova_cor
            else:
                print("A cor continua sendo:",self.color)

        def mostraCor(self):
            print("\nA cor atual é:",self.color)

    bola=Bola("verde", 3, "plastico")
    c="s"

    while c=="s":
        bola.mostraCor()
        bola.trocaCor()

        c = input("Continuar? s-sim n-não")
        c = c.lower()
        if c == "n":
            break

    bola.mostraCor()

def ex2():
    class Quadrado:
        def __init__(self, tamLado=0):
            self.tamLado = tamLado

        def trocaValorLado(self):
            mudar= input("Deseja mudar o tamanho do lado do Quadrado? s-sim n-não")

            mudar = mudar.lower()

            if mudar == "s":
                novo_lado = float(input("\n> Novo Lado: "))
                self.tamLado = novo_lado
            else:
                print("O tamanho do lado continua sendo:",self.tamLado)

        def mostraValorLado(self):
            print("\nO tamanho do lado é:",self.tamLado)

        def calculaArea(self):
            area=self.tamLado*self.tamLado
            print("\nO tamanho da área é:",area)

    quadrado=Quadrado(3)
    c="s"
    while c=="s":
        quadrado.mostraValorLado()
        quadrado.trocaValorLado()
        quadrado.calculaArea()

        c = input("Continuar? s-sim n-não")
        c = c.lower()
        if c == "n":
            break

    quadrado.mostraValorLado()

def ex3():
    class Retangulo:
        def __init__(self, comprimento=0, largura=0):
            self.comprimento = comprimento
            self.largura = largura

        def trocaValorLado(self):
            mudar= input("Deseja mudar os valores dos lados do Retângulo? s-sim n-não")

            mudar = mudar.lower()

            if mudar == "s":
                novo_comp = float(input("\n> Novo Comprimento: "))
                novo_alt = float(input("\n> Nova Largura: "))
                self.comprimento = novo_comp
                self.largura = novo_alt
            else:
                print("O comprimento e a largura continuam sendo respectivamente:",self.comprimento,self.largura)

        def mostraValorLado(self):
            print("\nO comprimento e a largura são respectivamente::",self.comprimento,self.largura)

        def calculaArea(self):
            area=self.comprimento*self.largura
            return area

        def calculaPerimetro(self):
            per=2*(self.comprimento+self.largura)
            return per

    comp=float(input("Informe o comprimento:"))
    larg=float(input("Informe a largura:"))
    quadrado = Retangulo(comp,larg)
    c = "s"
    while c == "s":
        quadrado.mostraValorLado()
        quadrado.trocaValorLado()
        print("Serão necessários",quadrado.calculaArea(),"m^2 de piso")
        print("Serão necessários",quadrado.calculaPerimetro(),"m de radapé")

        c = input("Continuar? s-sim n-não")
        c = c.lower()
        if c == "n":
            break

    quadrado.mostraValorLado()

def ex4():
    class Pessoa:
        def __init__(self, nome="unknown", idade=0, peso=0,altura=0):
            self.nome = nome
            self.idade = idade
            self.peso= peso
            self.altura = altura

        def envelhecer(self):
            self.idade+=1
            return self.idade

        def engordarOuEmagrecer(self,pes):
                self.peso=pes
                return self.peso

        def crescer(self):
            if self.idade<21:
                self.altura+=0.05

        def mostraPessoa(self):
            print("\nO Nome, idade, peso e altura são respectivamente::",self.nome,self.idade,self.peso,self.altura)

    nome = input("Informe o nome:")
    idade = int(input("Informe a idade:"))
    peso = float(input("Informe o peso:"))
    altura = float(input("Informe a altura:"))
    pessoa = Pessoa(nome,idade,peso,altura)
    c = "s"
    while c == "s":
        pessoa.envelhecer()
        peso=float(input("Se passou um ano, Informe o novo peso:"))
        pessoa.engordarOuEmagrecer(peso)
        pessoa.crescer()

        c = input("Continuar? s-sim n-não")
        c = c.lower()
        if c == "n":
            break

    pessoa.mostraPessoa()

def ex5():
    class ContaCorrente:
        def __init__(self, numConta, nomCor, saldo=0):
            self.numConta = numConta
            self.nomCor = nomCor
            self.saldo= saldo

        def alterarNome(self):
            mudar = input("Deseja mudar o nome atual? s-sim n-não")

            mudar = mudar.lower()

            if mudar == "s":
                novo_nome = input("\n> Novo Nome: ")
                self.nomCor = novo_nome
            else:
                print("O nome continua sendo:", self.nomCor)

        def deposito(self):
            valor=float(input("Informe o valor do depósito:"))
            self.saldo+=valor
            return self.saldo

        def saque(self):
            valor=float(input("Informe o valor do saque:"))
            self.saldo-=valor
            return self.saldo

        def mostraDadosConta(self):
            print("\nO Nome, conta e o saldo são respectivamente::",self.nomCor,self.numConta,self.saldo)

    nome = input("Informe o nome:")
    numConta = int(input("Informe o número da conta corrente:"))
    saldo = float(input("Informe o saldo:"))
    conta = ContaCorrente(numConta,nome,saldo)
    c = 1
    while c != 0:
        print("Conta corrente")
        print("1 - Mudar Nome")
        print("2 - Depósito")
        print("3 - Saque")
        print("0 - Sair")
        op=int(input(""))
        if op==1:
            print("entrar 1")
            conta.alterarNome()
        elif op==2:
            conta.deposito()
        elif op==3:
            conta.saque()

        elif op == 0:
            break
    conta.mostraDadosConta()

def ex6():
    class Tv:
        def __init__(self, canal=0,volume=0):
            self.canal = canal
            self.volume = volume

        def diminuirVolume(self,valor):
            vol=self.volume-valor
            if vol<=0:
                print("Volume já chegou ao mínimo 0")
                self.volume=0
            else:
                self.volume=vol
            return self.volume

        def  aumentarVolume(self,valor):
            vol = self.volume + valor
            if vol >= 100:
                print("Volume já chegou ao máximo 100")
                self.volume = 100
            else:
                self.volume = vol
            return self.volume

        def mudarCanal(self):
            canal=int(input("Informe o canal:"))
            if canal>0 and canal<=100:
                self.canal=canal
                return self.canal
            else:
                print("Este canal não existe")

        def mostraDadosTv(self):
            print("\nO Canal e o volume são respectivamente:",self.canal,self.volume)

    canal = int(input("Informe o canal:"))
    if canal>100:
        canal=100
    elif canal<=0:
        canal=1
    volume= int(input("Informe o volume:"))
    tv = Tv(canal,volume)
    c = 1
    while c != 0:
        print("Tv")
        print("1 - Mudar Canal")
        print("2 - Aumentar Volume")
        print("3 - Diminuir volume")
        print("0 - Sair")
        op=int(input(""))
        if op==1:
            tv.mudarCanal()
        elif op==2:
            vol=int(input("Quanto você deseja aumentar:"))
            tv.aumentarVolume(vol)
        elif op==3:
            vol = int(input("Quanto você deseja diminuir:"))
            tv.diminuirVolume(vol)

        elif op == 0:
            break
    tv.mostraDadosTv()

def ex7():
    class Tamagushi:
        def __init__(self, nome="",fome=0,saude=0,idade=0):
            self.nome = nome
            self.fome = fome
            self.saude = saude
            self.idade = idade

        def alterarNome(self):
            nome=input("Informe o nome do Tamagushi:")
            self.nome=nome

        def alterarFome(self):
            fome=int(input("Informe a fome do Tamagushi:"))
            self.fome=fome

        def alterarSaude(self):
            saude=int(input("Informe a saúde do Tamagushi:"))
            self.saude=saude

        def alterarIdade(self):
            idade=int(input("Informe a idade do Tamagushi:"))
            self.idade=idade

        def retornarNome(self):
            print("\nO nome do Tamagushi:",self.nome)

        def retornarFome(self):
            print("\nA fome do Tamagushi:",self.fome)

        def retornarSaude(self):
            print("\nA saude do Tamagushi:",self.saude)

        def retornarIdade(self):
            print("\nA idade do Tamagushi:",self.idade)

        def calcularHumor(self):
            humor=(self.saude+self.fome)/2
            return humor

        def mostraDadosTamagushi(self):
            humor=self.calcularHumor()
            print("\nO nome, fome, saúde, idade e humor são respectivamente:",self.nome,self.fome,self.saude,self.idade,humor)

    nome = input("Informe o nome do Tamagushi:")
    tamagushi = Tamagushi(nome)
    c = 1
    print("Quando for infomrar os níveis, 1-baixo 5-muito alto")
    while c != 0:
        print("Tamagushi")
        print("1 - Mudar Nome")
        print("2 - Mudar Fome")
        print("3 - Mudar Saúde")
        print("4 - Mudar Idade")
        print("5 - Ver Nome")
        print("6 - Ver Fome")
        print("7 - Ver Saúde")
        print("8 - Ver Idade")
        print("9 - Ver Humor")
        print("0 - Sair")
        op = int(input(""))
        if op == 1:
            tamagushi.alterarNome()
        elif op == 2:
            tamagushi.alterarFome()
        elif op == 3:
            tamagushi.alterarSaude()
        elif op == 4:
            tamagushi.alterarIdade()
        elif op == 5:
            tamagushi.retornarNome()
        elif op == 6:
            tamagushi.retornarFome()
        elif op == 7:
            tamagushi.retornarSaude()
        elif op == 8:
            tamagushi.retornarIdade()
        elif op == 9:
            print("Humor:",tamagushi.calcularHumor())

        elif op == 0:
            break
    tamagushi.mostraDadosTamagushi()

def ex8():
    class Macaco:
        def __init__(self, nome=""):
            self.nome = nome
            self.bucho = []

        def __repr__(self):
            return str(self.__dict__)

        def comer(self,comida,i):
            lista[i].bucho.append(comida)

        def verBucho(self):
            print(self.bucho)

        def digerir(self,i):
            i.bucho.pop()

    nome = input("Informe o nome do primeiro Macaco:")
    nome2 = input("Informe o nome do segundo Macaco:")
    macaco1 = Macaco(nome)
    macaco2 = Macaco(nome2)
    lista=[]
    lista.append(macaco1)
    lista.append(macaco2)
    d=len(lista)
    c = 1
    cont=1
    while c != 0:
        print("\nMacaco")
        print("1 - Comer")
        print("2 - Digerir")
        print("0 - Sair")
        op=int(input(""))
        if op==0:
            break
        elif op ==1:
            for i in range(d):
                comida = input("Informe a comida do Macaco:")
                lista[i].comer(comida,i)
            print("\nRefeição -",cont)
            for i in lista:
                i.verBucho()
            cont+=1
        elif op==2:
            for i in lista:
                i.digerir(i)
            print("\nMacacos Digeriram")

    print(lista)
    macaco1.comer(macaco2,0)
    print(lista)


def ex9():
    class Ponto:
        def __init__(self, x=0,y=0):
            self.x = x
            self.y = y

        def __repr__(self):
            return str(self.__dict__)

        def imprimirDados(self):
            print("\nOs valores de x e y são espectivamente:",self.x,self.y)

    class Retangulo:
        def __init__(self, comprimento, largura, inicio):
            self.comprimento = comprimento
            self.largura = largura
            self.inicio = inicio

        def __repr__(self):
            return str(self.__dict__)

        def encontrarCentro(self):
            x = self.inicio.x + (self.comprimento / 2)
            y = self.inicio.y + (self.largura / 2)

            centro = Ponto(x, y)

            print("Centro:", centro)

    def criarRetangulo():
        print("Retangulo")

        ini = Ponto(0, 0)
        ret = Retangulo(5, 5, ini)

        comprimento = float(input("Comprimento: "))
        largura = float(input("largura: "))
        ret.comprimento = comprimento
        ret.largura = largura

        x = float(input("Eixo X: "))
        y = float(input("Eixo Y: "))
        ini = Ponto(x, y)
        ret.inicio = ini

        return ret

    ret = criarRetangulo()
    continuar = True

    while continuar:
        print("\n\n\n")
        print(ret)

        print("1 - Criar Retângulo")
        print("2 - Encontar centro")
        print("0 - Sair")
        op = int(input("Selcione uma opção = "))
        print()

        if op == 1:
            ret = criarRetangulo()

        elif op == 2:
            ret.encontrarCentro()
            cont = input("Pressione qualquer tecla para continuar...")

        elif op == 0:
            continuar = False

ex9()

def ex10():
    class BombaCombustivel:
        def __init__(self, tipoCombustivel="",valorLitro=0,qtdCombustivel=0):
            self.tipoCombustivel = tipoCombustivel
            self.valorLitro = valorLitro
            self.qtdCombustivel = qtdCombustivel

        def alterarQuantidadeCombustivel(self,qtd):
            soma=self.qtdCombustivel-qtd
            if soma<=0:
                print("\nCANCELANDO VENDA - Acabou o combustivel")
            else:
                self.qtdCombustivel-=qtd

        def abastecerPorValor(self):
            valor=float(input("Informe o valor que deseja abastecer:"))
            litros=valor/self.valorLitro
            print("A quantidade de Litros é igual a:",litros)
            self.alterarQuantidadeCombustivel(litros)

        def abastecerPorLitro(self):
            litros=float(input("Informe a quantidade de litros que abastecer:"))
            valor=litros*self.valorLitro
            print("O valor a ser pago é de: R$",valor)
            self.alterarQuantidadeCombustivel(litros)

        def alterarValor(self):
            valor=float(input("Informe o novo Valor do litro combustível:"))
            self.valorLitro=valor

        def alterarCombostivel(self):
            tipo=input("Informe o tipo do combustivel:")
            self.tipoCombustivel=tipo

        def mostrarDadosCombustivel(self):
            print("\nO tipo, valor do litro e quantidade de combustível são respectivamente:", self.tipoCombustivel, self.valorLitro, self.qtdCombustivel)

    tipo = input("Informe o tipo do Combustível:")
    qtd = float(input("Informe a quantidade de Combustível na bomba:"))
    valor = float(input("Informe o valor do combustivel:"))
    comb = BombaCombustivel(tipo,valor,qtd)
    c = 1
    while c != 0:
        print("Combustivel")
        print("1 - Abastecer por valor")
        print("2 - Abastecer por Litro")
        print("3 - Alterar Valor")
        print("4 - Alterar Combustivel")
        print("0 - Sair")
        op = int(input(""))
        if op == 1:
            comb.abastecerPorValor()
        elif op == 2:
            comb.abastecerPorLitro()
        elif op == 3:
            comb.alterarValor()
        elif op == 4:
            comb.alterarCombostivel()
        elif op == 0:
            break
    comb.mostrarDadosCombustivel()

def ex11():
    class Carro:
        def __init__(self, consumo=0, qtdCombs=0):
            self.consumo = consumo
            self.qtdCombs= qtdCombs

        def andar(self,km):
            val=km/self.consumo
            self.qtdCombs-=val

        def obterGasolina(self):
            print("A quantidade de Combustível é restante no tanque:",self.qtdCombs)

        def adicionarGasolina(self,abst):
            self.qtdCombs+=abst

    consumo = float(input("Informe o consumo do Carro km/l:"))
    meuFusca = Carro(consumo)
    c = 1
    while c != 0:
        print("Carro")
        print("1 - Abastecer")
        print("2 - Andar")
        print("3 - Mostrar a qtd de combustivel restante")
        print("0 - Sair")
        op = int(input(""))
        if op == 1:
            abast=float(input("Informe o valor em litros do abastecimento:"))
            meuFusca.adicionarGasolina(abast)
        elif op == 2:
            km = float(input("Informe o valor dos kms rodadados:"))
            meuFusca.andar(km)
        elif op == 3:
            meuFusca.obterGasolina()
        elif op == 0:
            break

def ex12():
    class contaInvestimento:
        def __init__(self, numConta, nomCor, saldo=0, taxajuros=0):
            self.numConta = numConta
            self.nomCor = nomCor
            self.saldo= saldo
            self.taxajuros= taxajuros

        def alterarNome(self):
            mudar = input("Deseja mudar o nome atual? s-sim n-não")

            mudar = mudar.lower()

            if mudar == "s":
                novo_nome = input("\n> Novo Nome: ")
                self.nomCor = novo_nome
            else:
                print("O nome continua sendo:", self.nomCor)

        def deposito(self):
            valor=float(input("Informe o valor do depósito:"))
            self.saldo+=valor
            return self.saldo

        def saque(self):
            valor=float(input("Informe o valor do saque:"))
            self.saldo-=valor
            return self.saldo

        def mostraDadosConta(self):
            print("\nO Nome, conta e o saldo são respectivamente::",self.nomCor,self.numConta,self.saldo)

        def adicioneJuros(self):
            self.saldo=self.saldo+(self.saldo*self.taxajuros/100)

    conta = contaInvestimento(1,"nome",1000,10)
    print("Conta corrente")
    conta.adicioneJuros()
    conta.adicioneJuros()
    conta.adicioneJuros()
    conta.adicioneJuros()
    conta.adicioneJuros()
    conta.mostraDadosConta()

def ex13():
    class Funcionario:
        def __init__(self, nome="", salario=0):
            self.nome = nome
            self.salario = salario

        def devolverNome(self):
            return self.nome

        def devolverSalario(self):
            return self.salario

    func = Funcionario("nome", 1000)
    print("Nome:",func.devolverNome())
    print("Salario:",func.devolverSalario())

def ex14():
    class Funcionario:
        def __init__(self, nome="", salario=0):
            self.nome = nome
            self.salario = salario

        def devolverNome(self):
            return self.nome

        def devolverSalario(self):
            return self.salario

        def aumentarSalario(self,perc):
            self.salario=self.salario+(self.salario*perc/100)

    harry = Funcionario("Harry", 25000)
    harry.aumentarSalario(10)
    print("\nNome:",harry.devolverNome())
    print("Salario:",harry.devolverSalario())

def ex15():
    class Tamagushi:
        def __init__(self, nome="",fome=0,saude=0,idade=0, humor=0):
            self.nome = nome
            self.fome = fome
            self.saude = saude
            self.idade = idade
            self.humor = humor

        def alterarNome(self):
            nome=input("Informe o nome do Tamagushi:")
            self.nome=nome

        def alterarFome(self):
            fome=int(input("Informe a fome do Tamagushi:"))
            self.fome=fome

        def aumentarFome(self):
            self.fome+=1

        def darComida(self,valor):
            self.fome-=valor

        def alterarSaude(self):
            saude=int(input("Informe a saúde do Tamagushi:"))
            self.saude=saude

        def alterarIdade(self):
            idade=int(input("Informe a idade do Tamagushi:"))
            self.idade=idade

        def retornarNome(self):
            print("\nO nome do Tamagushi:",self.nome)

        def retornarFome(self):
            print("\nA fome do Tamagushi:",self.fome)

        def retornarSaude(self):
            print("\nA saude do Tamagushi:",self.saude)

        def retornarIdade(self):
            print("\nA idade do Tamagushi:",self.idade)

        def calcularHumor(self):
            humor=(self.saude+self.fome+self.humor)/2
            return humor

        def brincar(self):
            self.humor+=1

        def naoBrincar(self):
            self.humor-=1

        def mostraDadosTamagushi(self):
            n=int(self.humor)
            humor=self.calcularHumor()+n
            print("\nO nome, fome, saúde, idade e humor são respectivamente:",self.nome,self.fome,self.saude,self.idade,humor)

    nome = input("Informe o nome do Tamagushi:")
    tamagushi = Tamagushi(nome)
    c = 1
    print("Quando for infomrar os níveis, 1-baixo 5-muito alto")
    while c != 0:
        print("Tamagushi")
        print("1 - Mudar Nome")
        print("2 - Mudar Fome")
        print("3 - Mudar Saúde")
        print("4 - Mudar Idade")
        print("5 - Ver Nome")
        print("6 - Ver Fome")
        print("7 - Ver Saúde")
        print("8 - Ver Idade")
        print("9 - Ver Humor")
        print("10 - Dar Comida")
        print("11 - Brincar")
        print("0 - Sair")
        op = int(input(""))
        if op == 1:
            tamagushi.alterarNome()
        elif op == 2:
            tamagushi.alterarFome()
        elif op == 3:
            tamagushi.alterarSaude()
        elif op == 4:
            tamagushi.alterarIdade()
        elif op == 5:
            tamagushi.retornarNome()
        elif op == 6:
            tamagushi.retornarFome()
        elif op == 7:
            tamagushi.retornarSaude()
        elif op == 8:
            tamagushi.retornarIdade()
        elif op == 9:
            print("Humor:",tamagushi.calcularHumor())
        elif op ==10:
            valor=int(input("Insira a quantidade de comida 1-pouco -> 5-muito"))
            tamagushi.darComida(valor)
        elif op ==11:
            tamagushi.brincar()
        elif op == 0:
            break
        if op==10 or op==11:
            tamagushi.aumentarFome()
            tamagushi.naoBrincar()

    tamagushi.mostraDadosTamagushi()

def ex16():
    class Tamagushi:
        def __init__(self, nome="", fome=0, saude=0, idade=0, humor=0):
            self.nome = nome
            self.fome = fome
            self.saude = saude
            self.idade = idade
            self.humor = humor

        def alterarNome(self):
            nome = input("Informe o nome do Tamagushi:")
            self.nome = nome

        def alterarFome(self):
            fome = int(input("Informe a fome do Tamagushi:"))
            self.fome = fome

        def aumentarFome(self):
            self.fome += 1

        def darComida(self, valor):
            self.fome -= valor

        def alterarSaude(self):
            saude = int(input("Informe a saúde do Tamagushi:"))
            self.saude = saude

        def alterarIdade(self):
            idade = int(input("Informe a idade do Tamagushi:"))
            self.idade = idade

        def retornarNome(self):
            print("\nO nome do Tamagushi:", self.nome)

        def retornarFome(self):
            print("\nA fome do Tamagushi:", self.fome)

        def retornarSaude(self):
            print("\nA saude do Tamagushi:", self.saude)

        def retornarIdade(self):
            print("\nA idade do Tamagushi:", self.idade)

        def calcularHumor(self):
            humor = (self.saude + self.fome + self.humor) / 2
            return humor

        def brincar(self):
            self.humor += 1

        def naoBrincar(self):
            self.humor -= 1

        def mostraDadosTamagushi(self):
            n = int(self.humor)
            humor = self.calcularHumor() + n
            print("\nO nome, fome, saúde, idade e humor são respectivamente:", self.nome, self.fome, self.saude,
                  self.idade, humor)

        def str(self):
            print("Nome =",self.nome," Idade =",self.idade,"Fome =",self.fome,"Saúde =",self.saude,"Humor= ",self.humor)

    nome = input("Informe o nome do Tamagushi:")
    tamagushi = Tamagushi(nome)
    c = 1
    print("Quando for infomrar os níveis, 1-baixo 5-muito alto")
    while c != 0:
        print("Tamagushi")
        print("1 - Mudar Nome")
        print("2 - Mudar Fome")
        print("3 - Mudar Saúde")
        print("4 - Mudar Idade")
        print("5 - Ver Nome")
        print("6 - Ver Fome")
        print("7 - Ver Saúde")
        print("8 - Ver Idade")
        print("9 - Ver Humor")
        print("10 - Dar Comida")
        print("11 - Brincar")
        print("0 - Sair")
        op = int(input(""))
        if op == 1:
            tamagushi.alterarNome()
        elif op == 2:
            tamagushi.alterarFome()
        elif op == 3:
            tamagushi.alterarSaude()
        elif op == 4:
            tamagushi.alterarIdade()
        elif op == 5:
            tamagushi.retornarNome()
        elif op == 6:
            tamagushi.retornarFome()
        elif op == 7:
            tamagushi.retornarSaude()
        elif op == 8:
            tamagushi.retornarIdade()
        elif op == 9:
            print("Humor:", tamagushi.calcularHumor())
        elif op == 10:
            valor = int(input("Insira a quantidade de comida 1-pouco -> 5-muito"))
            tamagushi.darComida(valor)
        elif op == 11:
            tamagushi.brincar()
        elif op == 13:
            tamagushi.str()
        elif op == 0:
            break
        if op == 10 or op == 11:
            tamagushi.aumentarFome()
            tamagushi.naoBrincar()

    tamagushi.mostraDadosTamagushi()

def ex17():
    class Tamagushi:
        def __init__(self, nome="", fome=0, saude=0, idade=0, humor=0):
            self.nome = nome
            self.fome = fome
            self.saude = saude
            self.idade = idade
            self.humor = humor

        def __repr__(self):
            return str(self.__dict__)

        def calcularHumor(self):
            humor = (self.saude + self.fome + self.humor) / 3
            return humor

        def brincar(self):
            self.humor += 1

        def naoBrincar(self):
            self.humor -= 1

        def ouvir(self):
            self.humor +=1

        def darComida(self, valor):
            self.fome -= valor

        def aumentarFome(self):
            self.fome += 1

        def mostraDadosTamagushi(self):
            n = int(self.humor)
            humor = self.calcularHumor() + n
            print("\nO nome, fome, saúde, idade e humor são respectivamente:", self.nome, self.fome, self.saude,
                  self.idade, humor)

        def str(self):
            print("Nome =",self.nome," Idade =",self.idade,"Fome =",self.fome,"Saúde =",self.saude,"Humor= ",self.humor)


    tamagushi = Tamagushi("1",15,0,0,10)
    tamagushi2 = Tamagushi("2",16,0,0,1)
    tamagushi3 = Tamagushi("3",2,0,0,3)
    fazenda=[]
    fazenda.append(tamagushi)
    fazenda.append(tamagushi2)
    fazenda.append(tamagushi3)
    c = 1
    print("Quando for infomrar os níveis, 1-baixo 5-muito alto")
    while c != 0:
        print("1 - Dar Comida")
        print("2 - Brincar")
        print("3 - Ouvir")
        print("0 - Sair")
        op = int(input(""))
        if op == 1:
            valor = int(input("Insira a quantidade de comida 1-pouco -> 5-muito"))
            for i in fazenda:
                i.darComida(valor)
        elif op == 2:
            for i in fazenda:
                i.brincar()
        elif op == 3:
            for i in fazenda:
                i.ouvir()
        elif op == 0:
            break

        for i in fazenda:
            i.aumentarFome()
            if op!=2:
                i.naoBrincar()

    print(fazenda)
