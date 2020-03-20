import sys,socket
def ex1():
    arq = open("ips.txt", "r")
    conteudo = arq.read()
    ips = conteudo.split("\n")
    invalidos = []
    validos=[]

    for i in ips:
        try:
            socket.inet_aton(i)
            validos.append(i+'\n')
        except socket.error:
            invalidos.append(i + '\n')

    print(validos)
    print("///////------")
    print(invalidos)

def ex2():
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
ex1()