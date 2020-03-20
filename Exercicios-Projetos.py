def ex1():
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

    usuarios.sort(key=lambda a: a[3])

    elementos = len(usuario)
    media = (total) / (elementos + 1)

    arquivo=open("relatorio.html", "w")
    arquivo.write("<!DOCTYPE html>")
    arquivo.write("<html>")
    arquivo.write("<head>")
    arquivo.write("<meta charset='utf-8'/> ")
    arquivo.write("<style>table {font-family: arial, sans-serif; border-collapse: collapse;width: 50%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style>")
    arquivo.write("</head>")
    arquivo.write("<body>")
    arquivo.write("<br/><h2> ACME Inc.               Uso do espaço em disco pelos usuários. </h2>")
    arquivo.write("</p>--------------------------------------------------------------</p>")
    arquivo.write("<table style='width:50%'>")
    arquivo.write("<tr><th>Nr.</th><th>Usuário</th><th>Espaço utilizado</th><th>% do uso</th></tr>")

    for usuario in usuarios:
        arquivo.write("<tr>")
        percentagem = "{0:.2f}".format(round(usuario[3], 2))
        arquivo.write("<td>")
        arquivo.write(str(usuario[0])  + " </td><td> {:<15}".format(usuario[1])  + "</td><td>{:<16}".format(percentagem) + "MB </td><td> " + "{0:.2f}".format(usuario[4]) + '%' + '\n</td>')
        arquivo.write("</tr>")
    arquivo.write("</table>")

    arquivo.write('<br\><p>\nEspaço Total Ocupado: ' + "{0:.2f}".format(total) + ' MB</p>')
    arquivo.write('<p>\nEspaço médio Ocupado: ' + "{0:.2f}".format(media) + ' MB</p>')

    arquivo.write("</body>")
    arquivo.write("</html>")
    arquivo.close()
    arquivo=open("relatorio.html", "r")
    print(arquivo.read())

def ex2():
    strings=[]
    arquivo=open("logsApache.txt", "r")
    site="www.tins.com"
    listaPalavras = []
    for linha in arquivo:
        strings.append(linha.split())

    for www in strings:
        if www[1]==site:
            if listaPalavras.count(www[0])==0:
                listaPalavras.append(www[0])

    print("Palavras pesquisadas que ajudam a chegar no site",site)
    for i in listaPalavras:
        print(i)

def ex3():
    strings = []
    negados = []
    arquivo = open("squid.txt", "r")
    arquivoN = open("squidNegado.txt", "r")
    for linha in arquivo:
        strings.append(linha.split())

    for linha in arquivoN:
        negados.append(linha.split())

    cont=0
    for i in negados:
        for j in strings:
            if i[0]==j[6]:
                cont+=1

    print("Os sites negados:")
    for i in negados:print(i,end=" ")
    print("\nEles foram pesquisados",cont,"vezes!")

ex2()