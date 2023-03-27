# função de formatção
from ast import While
from pickle import FALSE
from re import S
from ssl import ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE
from tabnanny import check
from Submenu_de_Usuarios import *

# __________________________________________________________________________Funções uteis______________________________________________________________________________


def imprime_formatado(texto, largura=60, moldura="|_+"):
    vertical, horizontal, canto = moldura
    print(f"{canto}{horizontal * (largura - 2)}{canto}")

    # cria uma copia da lista de strings, para não alterar a original, e acrescenta
    # uma linha em branco no começo e uma no final, para espaçamento:

    texto = texto[:]
    texto.insert(0, '')
    texto.append('')
    for linha in texto:
        print(f"{vertical}{linha:{largura-2}s}{vertical}")
    print(f"{canto}{horizontal * (largura - 2)}{canto}")


# Classepara por cores nas letras e deixa mais bonitinho :)
class bcolors:
    OK = '\033[92m'  # Verde
    WARNING = '\033[93m'  # Amarelo
    FAIL = '\033[91m'  # Vermelho
    RESET = '\033[0m'  # Reseta a cor para nao ficar no resto do programa
    # exemplos de escrever no print
    #print(bcolors.OK + "Certinho" + bcolors.RESET)
    #print(bcolors.WARNING + "AVISO" + bcolors.RESET)
    #print(bcolors.FAIL + "erro" + bcolors.RESET)

# Ve se ja existe funciona só para listas e strings


def CheckExistence(BBdoslivros, ISBN):

    for i in BBdoslivros:
        if i == ISBN:
            return True
    return False

# verifica existencia mas em bibliotecas


def CheckExistencegender(generos, add):

    for i in generos.values():
        if i == add:
            return True
    return False

# deixa a primeira letra maiuscula sem deixar a segunda tbm


def Captalize(string):
    Nstring = ""
    string = string.split()
    for palavra in string:
        Npalavra = palavra[0].upper()+palavra[1:].lower()
        Nstring = Nstring+Npalavra
    return Nstring

# ve se é numero ou nao


def checknumber(Number):

    N = Number.isdigit()
    return N


def isbn(Isbn):
    N = checknumber(Isbn)
    # Se não for um numero ele retorna pro menu com valor de "none"
    while N == False:
        print("------------------------------------------------------")
        print(bcolors.FAIL +
              "Insira um número valido não letras ou números quebrados!!" + bcolors.RESET)
        print("------------------------------------------------------")
        Isbn = input(
            "Digite novamente o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
        N = checknumber(Isbn)
    return (Isbn)


def existeisbn(bbdoslivros, isbn):
    for c, i in bbdoslivros.items():
        if c == int(isbn):
            return True
        else:
            return False
# _____________________________________________________________________________Fim Funçôes_________________________________________________________________________________________

# ______________________________________________________________________________ADICIONAR LIVRO________________________________________________________________
# Livros
# Inserir um livro Exemplo : Livro = (ISBN, Título, Gênero, Autores(While quantidade ilimitada), Número de Páginas)


def insertBooks(BBdoslivros, generos):
    # Declaro a lista dos livros como vazia
    listadoslivros = []

    # Pergunto codigo internacional
    ISBN = input(
        "Digite o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
    # Chama a função que verifica se o isbn é mesmo um numero
    N = checknumber(ISBN)
    # Se não for um numero ele retorna pro menu com valor de "none"
    while N == False:
        print("------------------------------------------------------")
        print(bcolors.FAIL +
              "Insira um número valido não letras ou números quebrados!!" + bcolors.RESET)
        print("------------------------------------------------------")
        ISBN = input(
            "Digite novamente o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
        N = checknumber(ISBN)

    # Checa se o codigo do livro existe
    flag = CheckExistence(BBdoslivros, int(ISBN))
    ISBN = int(ISBN)

    # Se o codigo não existir da um erro vermelho
    if flag == True:
        print("------------------------------------------------------")
        print(bcolors.FAIL + "O livro já está registrado" + bcolors.RESET)
        print("------------------------------------------------------")
    # Se existir faz as perguntas
    else:
        # pergunta titulo do livro e adiciona a lita de livros
        titulo = input("Digite o título do livro: ")
        listadoslivros.append(titulo)
        # Busca a função onde adiona e seleciona generos e depois adiciona na lista
        Genero = genders(generos)
        listadoslivros.append(Genero)
        # Busca a função de adicionar autores e adiciona na lista
        autor = addauthors()
        listadoslivros.append(autor)
        # pergunta numero de paginas
        Paginas = (input("Digite quantidade de paginas: "))
        # verifica se o número dado é um numero mesmo
        N2 = checknumber(Paginas)
        # Se o retornar false é porque o que foi digitado não é um numero então exibe um erro e retorna ao menu
        while N2 == False:
            print("------------------------------------------------------")
            print(
                bcolors.FAIL + "Insira um número valido não letras e nem números quebrados!!" + bcolors.RESET)
            print("------------------------------------------------------")
            Paginas = (input("Digite quantidade de paginas: "))
            N2 = checknumber(Paginas)
        listadoslivros.append(int(Paginas))
        # Confirma que os itens foram enviados
        print("------------------------------------------------------")
        print(bcolors.OK + "Todos os itens foram adicionados com sucesso👍" + bcolors.RESET)
        print("------------------------------------------------------")
        # Adiciona tudo a lista geral dos livros
        BBdoslivros[ISBN] = listadoslivros
        return (BBdoslivros)


# funçao que adiciona os autores
def addauthors():
    flag = False
    Autoreslista = []
    # Listas de possiveis respostas
    possiveis = "NAO , N, NO , NANANINANAO,NAONAO,NN,NEGATIVO,NAO,NÃO,Ñ,NEGO,NA"
    # Laço de analise
    while flag == False:
        autores = input("Digite os autores do livro: ")
        Q = checknumber(autores)
        # se estiver entre as possiveis respostas
        if Q == False:
            Autoreslista.append(Captalize(autores))

            SiNo = input("Deseja adicionar outro autor?: ").upper()
            if SiNo in possiveis:
                flag = True
                return Autoreslista
        # senão provavelmente é um sim
        else:
            print("------------------------------------------------------")
            print(bcolors.FAIL + "Insira um nome de ator coerente!!" + bcolors.RESET)
            print("------------------------------------------------------")


# Seleção de generos
def genders(generos):
    # Variavel de controle
    vdc = False
    # Repetição mas so serve se caso ele escreva um número invalido
    while vdc == False:
        # esse while cria um print formatado
        texto = [
            f'Selecione um Gênero:',
            '',
        ]
        for g in generos:

            genero = generos[g]
            texto = texto + [f' {g} {genero}']

        imprime_formatado(texto)

        Generoescolhido = input(": ")
        # verifica se o numero existe
        N = checknumber(Generoescolhido)
        while N == False:
            print("------------------------------------------------------")
            print(bcolors.FAIL + "Insira um número valido não letras!!" + bcolors.RESET)
            print("------------------------------------------------------")
            Generoescolhido = input(": ")
            N = checknumber(Generoescolhido)
        else:
            Generoescolha = int(Generoescolhido)

        lencontrol = len(generos) - 1
        # se 0 entao a escolha é adicionar
        if Generoescolha == 0:
            newadd = ""
            add = input("Digite o genero a adicionar: ")
            newadd = Captalize(add)

            trufal = CheckExistencegender(generos, newadd)
            if trufal == False:
                numero = len(generos)

                generos[numero] = newadd

                print(
                    "------------------------------------------------------------------")
                print(
                    bcolors.OK + "Gênero adicionado ao seu livro e a lista de gêneros com sucesso!!" + bcolors.RESET)
                print(
                    "------------------------------------------------------------------")
                return add
            else:
                print(
                    "------------------------------------------------------------------")
            print(bcolors.FAIL + "Esse gênero já existe" + bcolors.RESET)
            print("------------------------------------------------------------------")

        elif Generoescolha > lencontrol or Generoescolha < 0:
            print("------------------------------------------------------------------")
            print(
                bcolors.FAIL + "Número incorreto, Por favor digite um número correto." + bcolors.RESET)
            print("------------------------------------------------------------------")

        else:
            return generos[Generoescolha]

# ____________________________________________________________________________________Alterar__________________________________________________________________________________


# recebe o dicionario dos livros e um codigo de qual vai modificar
def alterar(BBdoslivros, ISBN, generos):
    achou = False
    if checkemptylist(BBdoslivros) == False:
        verificaisbn = 0

        while verificaisbn == 0:
            # clear é uma função usada ppra poder modificar o dicionario
            clear = False
            # função para checar ser é um número
            Checkisbn = checknumber(ISBN)
            # formatação de texto
            texto2 = [
                f'Livro:',
                '',
            ]
            # se for número
            if Checkisbn:

                # pega a chave e os itens dessa chave
                for chave, itens in BBdoslivros.items():
                    # se essa chave for igual ao isbn de pesquisa é porque a pessoa quer modificar esse livro
                    if chave == int(ISBN):
                        achou = True
                        newwhy = ""
                        # pega a formataçao e junta com a função de exibir um unico livro
                        texto2 = texto2 + listarum(BBdoslivros, ISBN)
                        # pega todos os textos para formataçao e chama a função que cria uma formatação
                        imprime_formatado(texto2)
                        why = input(f'O que deseja mudar: ').upper()
                        # chama a função que deixa todos os textos com a primeira letra maiuscula e o resto minusculo
                        newwhy = Captalize(why)

                        if "Isbn" in newwhy:
                            # clear é uma função para modificar o dicionario
                            clear = True
                            print(
                                "------------------------------------------------------------------")
                            print(
                                bcolors.OK + "Alterando o Padrão Internacional de Numeração de Livro" + bcolors.RESET)
                            print(
                                "------------------------------------------------------------------")
                            # Pergunto codigo internacional
                            NISBN = input(
                                "Digite o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
                            # Chama a função que verifica se o isbn é mesmo um numero
                            N = checknumber(NISBN)
                            # Se não for um numero ele retorna pro menu com valor de "none"
                            while N == False:
                                print(
                                    "------------------------------------------------------")
                                print(
                                    bcolors.FAIL + "Insira um número valido não letras ou números quebrados!!" + bcolors.RESET)
                                print(
                                    "------------------------------------------------------")
                                NISBN = input(
                                    "Digite novamente o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
                                N = checknumber(NISBN)
                            var = existeisbn(BBdoslivros, NISBN)
                            while var:
                                print(
                                    "------------------------------------------------------")
                                print(bcolors.FAIL +
                                      "ISBN já existe" + bcolors.RESET)
                                print(
                                    "------------------------------------------------------")
                                NISBN = input(
                                    "Digite novamente o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
                                N = checknumber(NISBN)
                                while N == False:
                                    print(
                                        "------------------------------------------------------")
                                    print(
                                        bcolors.FAIL + "Insira um número valido não letras ou números quebrados!!" + bcolors.RESET)
                                    print(
                                        "------------------------------------------------------")
                                    NISBN = input(
                                        "Digite novamente o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
                                    N = checknumber(NISBN)
                                var = existeisbn(BBdoslivros, NISBN)
                            additens = itens
                            verificaisbn = 1
                        elif "Nome" in newwhy:
                            clear = True
                            print(
                                "------------------------------------------------------------------")
                            print(bcolors.OK +
                                  "Alterando o nome do livro" + bcolors.RESET)
                            print(
                                "------------------------------------------------------------------")

                            Nome = input("Digite o nome do livro: ")
                            NISBN = ISBN
                            itens.pop(0)
                            itens.insert(0, Nome)
                            additens = itens
                            verificaisbn = 1
                        elif "Gênero" in newwhy or "Genero" in newwhy:
                            clear = True
                            print(
                                "------------------------------------------------------------------")
                            print(
                                bcolors.OK + "Alterando o gênero do livro" + bcolors.RESET)
                            print(
                                "------------------------------------------------------------------")

                            genero = genders(generos)
                            NISBN = ISBN
                            itens.pop(1)
                            itens.insert(1, genero)
                            additens = itens
                            verificaisbn = 1
                        elif "Autores" in newwhy:
                            clear = True
                            print(
                                "------------------------------------------------------------------")
                            print(
                                bcolors.OK + "Alterando os autores do livro" + bcolors.RESET)
                            print(
                                "------------------------------------------------------------------")
                            textaut = [
                                f'Autores:',
                                '',
                            ]
                            for a in itens[2]:
                                textaut = textaut + [f'{a}', '']
                            imprime_formatado(textaut)
                            varidec = True
                            vdec = 0
                            while varidec:

                                autores = input(
                                    "Qual autor deseja modificar?: ")
                                for a2 in range(len(itens[2])):
                                    if itens[2][a2] == autores:
                                        alte = input(
                                            "Por qual nome você deseja alterar: ")
                                        itens[2].pop(a2)
                                        itens[2].insert(a2, Captalize(alte))
                                        NISBN = ISBN
                                        additens = itens
                                        verificaisbn = 1
                                        varidec = False
                                    elif vdec == 0:
                                        print(
                                            "------------------------------------------------------")
                                        print(bcolors.FAIL + autores +
                                              " não é valido" + bcolors.RESET)
                                        print(
                                            "------------------------------------------------------")
                                        vdec = 1

                        elif "Numero" in newwhy or "Número" in newwhy:
                            clear = True
                            print(
                                "------------------------------------------------------------------")
                            print(
                                bcolors.OK + "Alterando o número de páginas do livro" + bcolors.RESET)
                            print(
                                "------------------------------------------------------------------")
                            # Pergunto codigo internacional
                            NPG = input("Digite o número de páginas: ")
                            # Chama a função que verifica se o isbn é mesmo um numero
                            N = checknumber(NPG)
                            # Se não for um numero ele retorna pro menu com valor de "none"
                            while N == False:
                                print(
                                    "------------------------------------------------------")
                                print(
                                    bcolors.FAIL + "Insira um número valido não letras ou números quebrados!!" + bcolors.RESET)
                                print(
                                    "------------------------------------------------------")
                                NPG = input(
                                    "Digite novamente o número de páginas: ")
                                N = checknumber(NPG)
                            itens.pop(3)
                            itens.insert(3, NPG)
                            additens = itens
                            NISBN = ISBN
                            verificaisbn = 1
                        else:
                            return

                if not achou:
                    print("------------------------------------------------------")
                    print(bcolors.FAIL + "ISBN NÃO ENCONTRADO" + bcolors.RESET)
                    print("------------------------------------------------------")
                    ISBN = input(
                        "Digite novamente o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
                    print("------------------------------------------------------")

            else:
                print("------------------------------------------------------")
                print(
                    bcolors.FAIL + "Insira um número valido não letras ou números quebrados!!" + bcolors.RESET)
                print("------------------------------------------------------")
                ISBN = input(
                    "Digite novamente o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")

        if clear:
            BBdoslivros.pop(int(ISBN))
            BBdoslivros[int(NISBN)] = additens
            print(BBdoslivros)
        return BBdoslivros
    else:
        print("------------------------------------------------------")
        print(bcolors.FAIL + "Não há livros registrados" + bcolors.RESET)
        print("------------------------------------------------------")
# ___________________________________________________________Listar um_____________________________________________________________________________________________


def listarum(BBdoslivros, ISBN):
    if checkemptylist(BBdoslivros) == False:
        texto = []
        autores = ""
        for codigo, itens in BBdoslivros.items():
            if codigo == int(ISBN):
                for i in itens[2]:
                    autores = autores + "," + " " + i
                texto = texto + [f'ISBN: {codigo}', '']
                texto = texto + [f'Nome do livro: {itens[0]}', '']
                texto = texto + [f'Gênero: {itens[1]}', '']
                texto = texto + [f'Autores:{autores}', '']
                texto = texto + [f'Número de paginas: {itens[3]}', '']
        return texto
    else:
        print("------------------------------------------------------")
        print(bcolors.FAIL + "Não há livros registrados" + bcolors.RESET)
        print("------------------------------------------------------")
#________________________________________________________existeautor____________________________________________
def existautor(BBdoslivros, str):
    for c, i in BBdoslivros.items():
        for a in range(len(i[2])):
            if str == i[2][a]:
                return True
    return False
# _________________________________________________Incluir_____________________________________________-___


def incluir(BBdoslivros):
    if checkemptylist(BBdoslivros) == False:
        print("------------------------------------------------------")
        print(bcolors.WARNING + "AVISO: Você só pode incluir autores" + bcolors.RESET)
        print("------------------------------------------------------")
        verificaisbn = 0
        vdc = 0
        while verificaisbn == 0:

            for c, i in BBdoslivros.items():
                livro = input("Digite o isbn do livro que quer incluir autores: ")
                clear = False
                if checknumber(livro):
                    if int(livro) == c:
                            print("------------------------------------------------------------------")
                            print(bcolors.OK + "incluindo autores ao livro" + bcolors.RESET)
                            print("------------------------------------------------------------------")
                            textaut = [
                                f'Autores:',
                                '',
                            ]
                            for sla in i[2]:
                                textaut = textaut + [f'{sla}', '']
                            imprime_formatado(textaut)
                            textaut = ""

                            incluir = input("Digite o nome do autor que vai incluir: ")
                            verific = existautor(BBdoslivros, Captalize(incluir))
                            print(verific)
                            while verific:
                                print("------------------------------------------------------")
                                print(bcolors.FAIL + "Já existe" + bcolors.RESET)
                                print("------------------------------------------------------")
                                incluir = input("Digite o nome do autor que vai incluir novamente: ")
                                verific = existautor(BBdoslivros, Captalize(incluir))

                            clear = True
                            i[2].append(Captalize(incluir))
                            additens = i
                            NISBN = c
                            verificaisbn = 1
                else:
                    print("------------------------------------------------------")
                    print(bcolors.FAIL + "Insira um número valido não letras ou números quebrados!!" + bcolors.RESET)
                    print("------------------------------------------------------")
                    livro = input("Digite novamente o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")

        if clear:
            BBdoslivros.pop(int(livro))
            BBdoslivros[int(NISBN)] = additens
            print("------------------------------------------------------------------")
            print(bcolors.OK + "Incluido com sucesso" + bcolors.RESET)
            print("------------------------------------------------------------------")
        return BBdoslivros
    else:
        print("------------------------------------------------------")
        print(bcolors.FAIL + "Não há livros registrados" + bcolors.RESET)
        print("------------------------------------------------------")
        return BBdoslivros
# ________________________________Verifica lista vazia_________________________________________________________________-


def checkemptylist(BBdoslivros):
    sla = len(BBdoslivros)
    if sla == 0:
        return True
    else:
        return False

# ________________________________Excluir_________________________________________________________________________________________


def delete(bbdoslivros):
    isbn = input("Digite o ISBN do livro que quer excluir: ")
    verifi = checknumber(isbn)
    clear = False
    clear2 = False
    vdc = True
    vedece = 0
    while vdc:
        if verifi:
            for c, i in bbdoslivros.items():
                if c == int(isbn):

                    textaut = [
                        f'O que deseja excluir?:',
                        '',
                        '1- Tudo',
                        '2- Autor',

                    ]
                    imprime_formatado(textaut)
                    escolha = int(input(": "))
                    if escolha == 1:
                        print(
                            "------------------------------------------------------------------")
                        print(bcolors.OK + "O livro " +
                              i[0] + " foi apagado" + bcolors.RESET)
                        print(
                            "------------------------------------------------------------------")
                        clear = True
                        vdc = False
                        nisbn = c
                    elif escolha == 2:
                            print( "------------------------------------------------------------------")
                            print(bcolors.OK + "Excluindo autores do livro" + bcolors.RESET)
                            print("------------------------------------------------------------------")
                            textsa = [
                                f'Autores:',
                                '',
                            ]
                            for sla in i[2]:
                                textsa = textsa + [f'{sla}', '']
                            imprime_formatado(textsa)
                            
                            while vedece == 0:
                                excluir = input("Digite o nome do autor que vai Excluir: ")
                                ecluir = Captalize(excluir)
                                for a in range(len(i[2])):
                                    if ecluir == i[2][a]:
                                        clear2 = True
                                        print("------------------------------------------------------------------")
                                        print(bcolors.OK + i[2][a] + " excluido" + bcolors.RESET)
                                        print("------------------------------------------------------------------")
                                        i[2].pop(a)
                                        itens = i
                                        nnisbn = c
                                        vedece = 1
                                        vdc = False
                                if vdc:
                                    print("------------------------------------------------------")
                                    print(bcolors.FAIL + excluir +" não existe" + bcolors.RESET)
                                    print("------------------------------------------------------")

        else:
            print("------------------------------------------------------")
            print(
                bcolors.FAIL + "Insira um número valido não letras ou números quebrados!!" + bcolors.RESET)
            print("------------------------------------------------------")
            isbn = input(
                "Digite novamente o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
    if clear:
        bbdoslivros.pop(nisbn)
    elif clear2:
        bbdoslivros.pop(nnisbn)
        bbdoslivros[nnisbn] = itens
# _________________________________________________Abrir aqrquivo_______________________________________________________________


def abrirarq(Arq):
    Arqs = open(Arq, 'r')
    linha = "a"
    BBdoslivros = {}
    # repete ate todos os dados tiverem sido processados
    while linha != "":
        linha = Arqs.readline()
        if linha != "":
            # separa as informações
            linha = linha.split("$separação$")
            key = int(linha[0])
            valor = [linha[1], linha[2], linha[3].split(
                "=separ="), int(linha[4])]
            # adiciona no dicionario
            BBdoslivros[key] = valor
    # fecha o arquivo
    Arqs.close()
    # retorna o banco de dados
    return BBdoslivros
# ____________________________________________________Adicionar arquivo_________________________________________________________


def adicionararql(Arq, BBdoslivros):
    # abre o arquivo
    Arqs = open(Arq, 'w')
    texto = ""
    autores = ""
    # passa de usuario em usuario
    for c, i in BBdoslivros.items():
        # separa as informações
        isbn = c
        nome = i[0]
        genero = i[1]
        for a in i[2]:
            autores = autores + "=separ=" + a

        npag = i[3]
        # junta tudo em um unico texto
        texto = texto + str(isbn) + "$separação$" + nome + "$separação$" + genero + \
            "$separação$" + autores + "$separação$" + \
            str(npag) + "$separação$" + "\n"
    # escreve as informações no arquivo
    Arqs.write(texto)
    # fecha o arquivo
    Arqs.close()
# _____________________________________________________________vefica existencia do arq________________________________________________


def existe_ArquivoL():
    import os
    if os.path.exists("livros.txt"):
        return True
    return False
# _______________________________________________________________________________________________________________________________________________________________________________
# verificar de existe
# Alterar
# Excluir
# Listar todos
# Listar elemento expecifico
# BBdoslivros = {1: ['babrsa', 'Comédia', ['asda', 'asda'], 123]}

def SubMenu_Livros():
    # Generos pre registrados
    generos = {0: "Adicionar Genero", 1: "Drama", 2: "Comédia", 3: "Terror", 4: "Romance", 5: "Ficcão Ciêntifica", 6: "Poesia", 7: "Fabula", 8: "Crônica", 9: "Conto", 10: "Fantasia", 11: "Suspense"}
    if not (existe_ArquivoL()):
        a = open("livros.txt", 'w')
        a.close()
    BBdoslivros = abrirarq("livros.txt")
    print("|---------------------------------------------------------------------------|")
    print("|                                 Livros                                    |")
    print("|---------------------------------------------------------------------------|")
    vdc = 0
    while vdc != 7:
        imprime_formatado(['MENU DE LIVROS', '', '1- Inserir livro', '', '2- Alterar livro', '', '3- Incluir itens ',
                          '', '4- Apagar', '', '5- Imprimir todos', '', '6- Imprimir um', '', '7- Voltar', ''])
        escolha = input(":")
        if escolha == "1":
            insertBooks(BBdoslivros, generos)

        elif escolha == "2":

            ISBN = input("Digite o isbn do livro que quer modificar: ")
            # se não tiver livro para mudar não mudar
            alterar(BBdoslivros, ISBN, generos)
        elif escolha == "3":

            incluir(BBdoslivros)
        elif escolha == "4":

            delete(BBdoslivros)
        elif escolha == "5":

            for c in BBdoslivros:
                texto = listarum(BBdoslivros, c)
                imprime_formatado(texto)
        elif escolha == "6":
            listar = input("Digite o Isbn do livro para mostar ele: ")
            textoform = listarum(BBdoslivros, listar)
            imprime_formatado(textoform)
        elif escolha == "7":
            vdc = 7
            Divisões(2)
            print("")
            continuar = input("<Enter> para continuar")
            Divisões(2)
        else:
            print("------------------------------------------------------")
            print(bcolors.FAIL + "Digite uma opção valida!" + bcolors.RESET)
            print("------------------------------------------------------")
    adicionararql("livros.txt", BBdoslivros)

