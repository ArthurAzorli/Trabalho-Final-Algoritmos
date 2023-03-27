from Submenu_de_livros import *
from Submenu_de_Usuarios import *
from datetime import *
def checkloan(Emprestimos, chave):
    for i in Emprestimos:
        if i == chave:
            return True
    return False

def formatardatetime(Data):
    datafinal = "{}/{}/{}".format(Data.day, Data.month,Data.year)
    return(datafinal)

#Verifica se a data é valida
def Datae(data):
    #Pergunta se correponde ao modelo de data
    if data.count('/')>=2 and len(data)>4:
        #Separa o dia, mes e ano
        data=data.split("/")
        dia=data[0]
        if len(dia)==1:
            dia='0'+dia
        mes=data[1]
        if len(mes)==1:
            mes='0'+mes
        ano=data[2]
        Ndata = dia+'/'+mes+'/'+ano
        #Caso o ano seja inválido
        if Anoe(ano)==False:
            ERRO("Ano inválido!")
            print("Tente novamente:")
            Ndata = Data(dia+'/'+mes+'/'+input("Digite o ano(AAAA): "))
        #Caso o mes seja inválido
        elif Mese(mes)==False:
            ERRO("Mes inválido!")
            print("Tente novamente:")
            Ndata = Data(dia+'/'+input("Digite o mes(MM): ")+'/'+ano)
        #Caso o dia seja inválido
        elif Diae(dia,mes,ano) == False:
            ERRO("Dia inválido!")
            print("Tente novamente:")
            Ndata = Data(input("Digite o dia(DD): ")+'/'+mes+'/'+ano)
    else:
        ERRO("Data inválida!")
        Ndata = Data(input("Tente novamente seguindo o modelo(DD/MM/AAAA):"))
    #Retorna a data arrumada 
    return Ndata
#-------------------------------------------------------------------------------------------        

#verifica se dia é válido
def Diae(dia,mes,ano):
    if NumeroINT(dia)==True or '/' in dia:
        dia=int(dia)
        mes=int(mes)
        ano=int(ano)
        d31=range(1,31+1)
        d30=range(1,30+1)
        if ano%4==0:
            Fev=range(1,29+1)
        else:
            Fev=range(1,28+1)
        meses={1:d31,2:Fev,3:d31,4:d30,5:d31,6:d30,7:d31,8:d31,9:d30,10:d31,11:d30,12:d31}
        if meses[mes][0]<=dia and dia<=meses[mes][-1]:
            return True
    return False
#-------------------------------------------------------------------------------------------

#verifica se o mes é válido
def Mese(mes):
    if NumeroINT(mes)==True or '/' in mes:
        mes=int(mes)
        if 1<=mes and mes<=12:
            return True
    return False
#-------------------------------------------------------------------------------------------

#Verifica se o ano é válido
def Anoe(ano):
    if NumeroINT(ano)==True or '/' in ano:
        ano=int(ano)
        #Verifica se a pessoa é mais velha viva(16/05/2022) que a pessoa mais velha do mundo (Johanna Mazibuko) e se ela ainda não nasceu
        if ano<1894 or 2050<ano:
            return False
        return True
    return False
#-------------------------------------------------------------------------------------------

#_______________________________________________Adicionar emprestimos______________________________________________________
def checkempre(emprestimos, chave, data):
    for c, i in emprestimos.items():
        if c[1] == chave:
            if i[0] == data:
                return True
    
    return False

#________________________________________________________Verificaadatadedevol____________________________________________
def limitadevo(datadia, datadevo):
    ldia = datadia.split("/")
    ldevol = datadevo.split("/")
    if int(ldevol[2]) == int(ldia[2]):
        if int(ldevol[1]) >= int(ldia[1]):
            return True
    elif int(ldevol[2]) > int(ldia[2]):
        return True

    else: 
        return False
        
#_______________________________adiciona emprestimo________________________________________________________________

def addloan(BBdoslivros, Usuarios, emprestimos):
    listafinal = []
    print("------------------------------------------------------------------")
    print(bcolors.OK + "Adicionando emprestimo" + bcolors.RESET)
    print("------------------------------------------------------------------")
    Cpf = input("Digite o cpf do usuario: ")
    cpf2 = cpf(Cpf)
    if Existe(Usuarios, cpf2):
        
        Isbn = input("Digite o Padrão Internacional de Numeração de Livro(ISBN) APENAS OS NÚMEROS: ")
        #Chama a função que verifica se o isbn é mesmo um numero
        isbn2 = isbn(Isbn)

        flag = CheckExistence(BBdoslivros,int(isbn2))
        isbnf = int(isbn2)
        
        if flag:
            for c, i in emprestimos.items():
                if isbnf == c[1]:
                    print("------------------------------------------------------")
                    print(bcolors.FAIL + "Livro não foi devolvido" + bcolors.RESET)
                    print("------------------------------------------------------")
                    return
                    
            chave = (cpf2, isbnf)
            if(checkloan(emprestimos, chave)):
                print("------------------------------------------------------")
                print(bcolors.FAIL + "Emprestimo já registrado" + bcolors.RESET)
                print("------------------------------------------------------")
            else:
                
                datea = date.today()
                data = formatardatetime(datea)
                if not checkempre(emprestimos, isbnf, data):
                    print(f'A data {data} foi inserida: ')
                    Datadevol = input("Digite a data de devolução: ")
                    datadevol = Datae(Datadevol)
                    datacerta = limitadevo(data, datadevol)
                    while not datacerta:
                        print("------------------------------------------------------")
                        print(bcolors.FAIL + "Digite corretamente a data de devolução, ela não pode ser antes de hoje!!" + bcolors.RESET)
                        print("------------------------------------------------------")
                        Datadevol = input("Digite a data de devolução: ")
                        datadevol = Data(Datadevol)
                        datacerta = limitadevo(data, datadevol)
                    multa = input("Digite o valor da multa diaria: ")
                    check = checknumber(multa)
                    while check == False:
                        print("------------------------------------------------------")
                        print(bcolors.FAIL + "Insira um número valido ou arredonde o valor." + bcolors.RESET)
                        print("------------------------------------------------------")
                        multa = input("Digite novamente o valor da multa: ")
                        check = checknumber(multa)
                    listafinal.append(data)
                    listafinal.append(datadevol)
                    listafinal.append(multa + "R$")
                    emprestimos[chave] =  listafinal
                    return(emprestimos)
                else:
                    print("------------------------------------------------------")
                    print(bcolors.FAIL + "Esse livro já foi alugado hoje" + bcolors.RESET)
                    print("------------------------------------------------------")

                    

        else:
            print("------------------------------------------------------")
            print(bcolors.FAIL + "livro não existe" + bcolors.RESET)
            print("------------------------------------------------------")
            addloan(BBdoslivros, Usuarios, emprestimos)
    else: 
        print("------------------------------------------------------")
        print(bcolors.FAIL + "Cpf Não existe" + bcolors.RESET)
        print("------------------------------------------------------")

#_____________________________________Passou da data__________________________________________________________
def passoudata(emprestimos, BBdoslivros):
    datea = date.today()
    data = formatardatetime(datea)
    listaclear = []
    clear = False
    for c, i in emprestimos.items():
        datadevo = i[1]
        if limitadevo(datadevo, data):
            for a, b in BBdoslivros.items():
                if a == c[1]:
                    if SorN(f'O livro: {b[0]} de ISBN: {a} foi devolvido?: '):
                        clear = True
                        listaclear.append(c)
                    else:
                        print("------------------------------------------------------")
                        print(bcolors.FAIL + "O livro está atrasado!!!" + bcolors.RESET)
                        print("------------------------------------------------------")
    if clear:
        for cha in listaclear:
            emprestimos.pop(cha)

#_______________________________________________________listarum_______________________________________________________
def listarumloan(emprestimos, chave):
    texto=[
                f'Emprestimos:',
                        '',
            ]
    for c, i in emprestimos.items():
        if c == chave:
            texto = texto + [f'Cpf: {c[0]}','']
            texto = texto + [f'Isbn: {c[1]}','']
            texto = texto + [f'Data de retirada: {i[0]}', '']
            texto = texto + [f'Data de devolução:{i[1]}', '']
            texto = texto + [f'Valor diario da multa por atraso: {i[2]}', '']
            return(texto)
        

            
#_____________________________________________________alterar_________________________________________________________
def alterarloan(emprestimos):
    modific = False
    
    Cpf = input("Digite o cpf: ")
    Cpf2 = cpf(Cpf)
    Isbn = input("Digite o isbn do livro: ")
    isbn2 = isbn(Isbn)
    isbns = int(isbn2)
    chave = (Cpf2, isbns)
    if checkloan(emprestimos, chave):
        chavef = listarumloan(emprestimos, chave)
        print(chavef)
        imprime_formatado(chavef)
        op = input("Digite um opção para alterar: ")
        op2 = Captalize(op)
        for c, i in emprestimos.items():
            if c == chave:
                if "Cpf" in op2:
                    modific = True
                    Ncpf = input("Digite o novo cpf: ")
                    Nncpf = cpf(Ncpf)
                    Nchave = (Nncpf, isbns)
                    nlist = i
                elif "Isbn" in op2:
                    modific = True
                    Nisbn = input("Digite o novo ISBN: ")
                    Nnisbn = isbn(Nisbn)
                    Nchave = (Cpf2, Nnisbn)
                    nlist = i
                elif "Retirada" in op2:
                    modific = True
                    Ndata = input("Digite a nova data formato DD/MM/YYYY: ")
                    Nndata = Data(Ndata)
                    Nchave = (Cpf2, isbns)
                    i.pop(0)
                    i.insert(0, Nndata)
                    nlist = i
                elif "Devolução" in op2 or "Devolucao" in op2 or "Devoluçao" in op2 or "Devolucão" in op2:
                    modific = True
                    Ndata = input("Digite a nova data formato DD/MM/YYYY: ")
                    Nndata = Data(Ndata)
                    Nchave = (Cpf2, isbns)
                    i.pop(1)
                    i.insert(1, Nndata)
                    nlist = i
                elif "Multa" in op2:
                    modific = True
                    Nmulta = input("Digite o novo valor de multa:")
                    Nnmulta = isbn(Nmulta)
                    Nnmulta = Nnmulta + "R$"
                    Nchave = (Cpf2, isbns)
                    i.pop(2)
                    i.insert(2, Nnmulta)
                    nlist = i
                else: 
                    print("------------------------------------------------------")
                    print(bcolors.FAIL + "Opção não existe tente novamente" + bcolors.RESET)
                    print("------------------------------------------------------")
                    alterarloan(emprestimos)

        if modific:
            emprestimos.pop(chave)
            emprestimos[Nchave] = nlist
            return emprestimos
        
    else: 
        print("------------------------------------------------------")
        print(bcolors.FAIL + "Emprestimo não existe" + bcolors.RESET)
        print("------------------------------------------------------")
                
#_______________________________Exluir_____________________________________________________________________
def excluirloan(emprestimos):
    if checkemptylist(emprestimos) == False:
        print("------------------------------------------------------------------")
        print(bcolors.OK + "Excluindo um emprestimo." + bcolors.RESET)
        print("------------------------------------------------------------------")
        print("------------------------------------------------------")
        print(bcolors.FAIL + "Você so pode excluir o emprestimo inteiro deseja continuar?" + bcolors.RESET)
        re = input(": ")
        print("------------------------------------------------------")
        res = Captalize(re)
        if res in "Sim, S, Si, Yes, Ye, Concerteza":
            Ecpf = input("Digite o cpf do emprestimo que vai excluir: ")
            Necpf = cpf(Ecpf)
            Eisbn = input("Digite o isbn do emprestimo que vai excluir: ")
            Neisbn = isbn(Eisbn)
            chave = (Necpf, int(Neisbn))
            if checkloan(emprestimos, chave):
                emprestimos.pop(chave)
                print("------------------------------------------------------------------")
                print(bcolors.OK + "Emprestimo excluido" + bcolors.RESET)
                print("------------------------------------------------------------------")
            else:
                print("------------------------------------------------------")
                print(bcolors.FAIL + "Esse emprestimo não existe" + bcolors.RESET)
                print("------------------------------------------------------")
        else: 
            return


    else:
        print("------------------------------------------------------")
        print(bcolors.FAIL + "Não existe nenhum emprestimo registrado" + bcolors.RESET)
        print("------------------------------------------------------")
#_________________________________________________Abrir aqrquivo_______________________________________________________________
def abrirarqe(Arq):
    Arqs = open(Arq, 'r')
    linha = "a"
    emprestimos = {}
    #repete ate todos os dados tiverem sido processados
    while linha != "":
        linha = Arqs.readline()
        if linha != "":
            #separa as informações 
            linha = linha.split("$separ$")
            key = (linha[0], linha[1])
            valor = [linha[2],linha[3], linha[4]]
            #adiciona no dicionario
            emprestimos[key] = valor
    #fecha o arquivo
    Arqs.close()
    #retorna o banco de dados
    return emprestimos
#____________________________________________________Adicionar arquivo_________________________________________________________

def adicionararqe(Arq, emprestimos):
    #abre o arquivo
    Arqs = open(Arq, 'w')
    texto = ""
    autores = ""
    #passa de usuario em usuario 
    for c, i in emprestimos.items():
        #separa as informações
        cpf = c[0]
        isbn = c[1]
        dataretirada = i[0]
        dataentrega = i[1]
        multa = i[2]
        #junta tudo em um unico texto
        texto = texto + cpf+ "$separ$"+ str(isbn)+ "$separ$" +dataretirada+ "$separ$" +dataentrega+ "$separ$" +multa+ "$separ$" + "\n"
    #escreve as informações no arquivo
    Arqs.write(texto)
    #fecha o arquivo
    Arqs.close()
#_____________________________________________________________vefica existencia do arq________________________________________________
def existe_Arquivoe():
    import os
    if os.path.exists("loan.txt"):
        return True
    return False
#________________________________________________________________Submenu_________________________________________________________________________


def submenuempre():
    emprestimos = {}
    if not (existe_ArquivoL()):
        a = open("livros.txt", 'w')
        a.close()
    if not(existe_Arquivo()):
        a = open("Users.txt",'w')
        a.close()
    if not(existe_Arquivoe()):
        a = open("loan.txt",'w')
        a.close()
    emprestimos = abrirarqe("loan.txt")
    Usuarios = AbrirArquivo("Users.txt")
    BBdoslivros = abrirarq("livros.txt")
    print("|---------------------------------------------------------------------------|")
    print("|                                 Emprestimos                               |")
    print("|---------------------------------------------------------------------------|")
    vdc = 0
    while vdc != 6:
        imprime_formatado(['MENU DE EMPRESTIMOS','','1- Inserir emprestimo', '', '2- Alterar emprestimo', '', '3- Apagar', '', '4- Imprimir todos', '', '5- Imprimir um', '', '6- Voltar', ''])
        escol = int(input(": "))
        passoudata(emprestimos, BBdoslivros)
        if escol == 1:
            addloan(BBdoslivros, Usuarios, emprestimos)
        elif escol == 2:
            alterarloan(emprestimos)
        elif escol == 3:
            excluirloan(emprestimos)
        elif escol == 4:
            for c in emprestimos:
                    texto = listarumloan(emprestimos, c)
                    imprime_formatado(texto)
        elif escol == 5:
            Ecpf = input("Digite o cpf do emprestimo que quer ver: ")
            Necpf = cpf(Ecpf)
            Eisbn = input("Digite o isbn: ")
            Neisbn = isbn(Eisbn)
            chave = (Necpf, int(Neisbn))
            sla = listarumloan(emprestimos, chave)
            imprime_formatado(sla)
        elif escol == 6:
            vdc = 6
            Divisões(2)
            print("")
            continuar = input("<Enter> para continuar")
            Divisões(2)
        else:
            print("------------------------------------------------------")
            print(bcolors.FAIL + "Digite uma opção valida!" + bcolors.RESET)
            print("------------------------------------------------------")
    adicionararqe("loan.txt", emprestimos)

