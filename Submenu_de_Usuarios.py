#Submenu de Usuários

#Funções

#______________________________________________________________________________________________________________________
#Listar Todos
def Exibir_Todos(BD):
    Divisões(1)
    print("")
    print("Usuários:")
    print("")
    #Exibição
    for User in BD.items():
        Exibir(User)
    #Informa que o Usuario foi cadastrado
    print("")
    Divisões(2)
    print("")
    print("Todos os Usuário listados com Sucesso!")
    Divisões(2)
     #Espera a confirmação para continuar
    print("")
    continuar = input("<Enter> para continuar")
    Divisões(2)

#______________________________________________________________________________________________________________________
#Listar um Elemento
def Exibir_Item(BD):
    Divisões(1)
    print("")
    print(" Pesquisa de Usuário:")
    print("")
    #Exibição
    Dados = itensDIC(BD, cpf(input("Digite o CPF do usuário desejado: ")), "CPF não Cadastrado!")
    #Cancelamento
    if Dados == 'cancel':
        #Informa que o processo foi cancelado
        print("")
        Divisões(2)
        print("")
        print("Processo cancelado com Sucesso!")
        Divisões(2)
    #Lista as informações
    else:
        Exibir(Dados)
        #Informa que o Usuario foi listado
        print("")
        Divisões(2)
        print("")
        print( "Usuário listado com Sucesso!")
        Divisões(2)
    #Espera a confirmação para continuar
    print("")
    continuar = input("<Enter> para continuar")
    Divisões(2)

#______________________________________________________________________________________________________________________
#Adicionar
def Inserir(BD):
    Cancel = False
    Divisões(1)
    print("")
    print("Adicionando Novo Usuário:")
   #Sepação
    print("")
    Divisões(3)
    print("Dados do Usuário")
    print("")
    #Pergunta o CPF
    CPF=cpf(input("Digite o CPF do Usuário: ").strip())
    #Verifica se CPF existe
    if Existe(BD, CPF) == True:
        #Caso exista
        ERRO("CPF já existe no sistema!")
        TN = (input("Tente novamente ou Cancele a ação digitando '-1':").strip())
        if TN != '-1':
            CPF = cpf(TN)
        else:
            Cancel = True
    if Cancel == False: 
        #Pergunta nome
        Nome=Captalize(input("Digite o nome completo do Usuário: ").strip())
        #Pergunta data de nascimento e Verifica se a data é válida
        DataNas=Data(input("Digite a data de nascimento (DD/MM/AAAA):  "))
        #Pegunta a Categoria
        Categoria=CATEG(Captalize(input("Digite a Categoria (Professor/Aluno): ").strip()))
        #Sepação
        print("")
        Divisões(3)
        print("Endereço do Usuário")
        print("")
        #Pergunta a Cidade
        Cidade = Captalize(input("Digite a Cidade: ").strip())
        #Pergunta o Estado e Verifica se o UF é válido
        Estado = UF(input("Digite o Estado(UF): ").strip().upper())
        #Pergunta o Bairro
        Bairro = Captalize(input("Digite o Bairro: ").strip())
        #Pergunta a Rua
        Rua = Captalize(input("Digite a Rua: ").strip())
        #Pergunta o Numero
        Numero = NumeroCasa(input("Digite o número da Casa(sem complemento): ").strip().upper())
        #Pergunta se há complemento
        if SorN("Há complemento? ") == True:
            #Se sim, pergunta o complemento
            Complemento=input("Digite o complemento: ").strip()
        else:
            Complemento=""
        #Separação
        print("")
        Divisões(3)
        print("Formas de contato: ")
        print("")
        #Pergunta e Verifica se o email é válido
        Email = EMAIL(input("Digite o Email: ").strip())
        #Pergunta e Verifica se o telefone é válido
        Telefone = Tel(input("Digite o Telefone (com o DDD e sem espaços): ").strip())
        #Prepara as informações para armazenar
        Endereço = [Cidade,Estado, Bairro, Rua, Numero + Complemento]
        Dados = [Nome, Endereço, Email, Telefone, DataNas, Categoria]
        BD[CPF] = Dados
        #Informa que o Usuario foi cadastrado
        print("")
        Divisões(2)
        print("")
        print("Usuario Cadastrado com Sucesso!")
    else:
        #Informa que o processo foi cancelado
        print("")
        Divisões(2)
        print("")
        print("Processo Cancelado com Sucesso!")
    #Espera a confirmação para continuar
    Divisões(2)
    print("")
    continuar = input("<Enter> para continuar")
    Divisões(2)
    #Devolve os dados ao dicionario de armazenamento
    return BD

#______________________________________________________________________________________________________________________
#Alterar
def Alterar(BD):
    op = ""
    #Opções de modificação
    OpsMOD = ['','','Nome', 'DataNas', 'Categ', 'Endereço', 'Email', 'Telefone']
    parar = False
    MSG = "Digite o CPF do usuario que deseja alterar: "
    Divisões(1)
    print("")
    print("Alterando Dados do Usuário:")
   #Sepação
    print("")
    while parar != True:
        Divisões(2)
        print("")
        chave = cpf(input(MSG))
       #Validar se o cpf existe no BD
        valor = BD.get(chave, False)
        if valor != False:
            Divisões(2)
            print("")
            #Exibe os dados do Usuario selecionado
            print("Os dados do Usuário Selecionado são:")
            Exibir((chave, valor))
            #Menu de modificações
            while op != '8':
                Cancel = False
                AntChave = chave
                NBD = {}
                Divisões(2)
                print("")
                print("O que deseja alterar?")
                print("")
                Divisões(3)
                #Opções
                print("1 - CPF")
                print("2 - Nome")
                print("3 - Data de Nascimento")
                print("4 - Categoria")
                print("5 - Endereço")
                print("6 - E-mail")
                print("7 - Telefone")
                print("8 - Voltar")
                Divisões(3)
                print("")
                #Pergunta as opções
                op = input("Digite a opção desejada: ")
                print("")
                Divisões(3)
                print("")
                if op != '8':
                    #Opção 1
                    if op == '1':
                        Nchave = cpf(input("Digite o novo CPF do Usuário: "))
                        print("")
                        Divisões(3)
                        item = AltChave(BD, chave, Nchave)
                        if item != 'Cancel':
                            NBD = item[1]
                            chave = item[0]
                        else:
                            #Cancela
                            Cancel = True
                            
                    #Opção 2  
                    elif op == '2':
                        NBD = AltValor(BD, chave, OpsMOD[2])
                        if NBD == 'Cancel': 
                            Cancel = True

                    #Opção 3
                    elif op == '3':
                        NBD = AltValor(BD, chave, OpsMOD[3])
                        if NBD == 'Cancel': 
                            Cancel = True

                    #Opção 4
                    elif op == '4':
                        NBD = AltValor(BD, chave, OpsMOD[4])
                        if NBD == 'Cancel': 
                            Cancel = True

                    #Opção 5      
                    elif op == '5':
                        NBD = AltValor(BD, chave, OpsMOD[5])
                        if NBD == 'Cancel': 
                            Cancel = True
                    #Opção 6    
                    elif op == '6':
                        NBD = AltValor(BD, chave, OpsMOD[6])
                        if NBD == 'Cancel': 
                            Cancel = True
                    #Opção 7   
                    elif op == '7':
                        NBD = AltValor(BD, chave, OpsMOD[7])
                        if NBD == 'Cancel': 
                            Cancel = True
                            
                    #Opção inválida  
                    else:
                        ERRO("Opção inválida!")
                        print("Tente novamente!")
                        Cancel = ""

                    #Se não cancelou
                    if Cancel == False:
                        Dados = itensDIC(NBD, chave, "CPF não Cadastrado!")
                        #Cancela
                        if Dados == 'cancel':
                            Cancel = True
                        else:
                            Divisões(2)
                            print("")
                            #Exibe como as modificações ficaram
                            print("As alterações dos Dados ficaram da seguinte maneira:")
                            Exibir(Dados)
                            Divisões(2)
                            print("")
                            #Pergunta se tem certeza se quer alterar
                            if SorN("Você tem certeza que quer alterar?")== True:
                                BD = NBD.copy()
                                #Informa que os dados foram alterados
                                Divisões(2)
                                print("")
                                print("Usuario Alterado com Sucesso!")
                                
                            else:
                                chave = AntChave
                                #Informa que o processo foi cancelado
                                print("")
                                Divisões(2)
                                print("")
                                print("Processo Cancelado com Sucesso!")
                    elif Cancel == True:
                        #Informa que o processo foi cancelado
                        print("")
                        Divisões(2)
                        print("")
                        print("Processo Cancelado com Sucesso!")
            parar = True
            #Espera a confirmação para continuar
            Divisões(2)
            print("")
            continuar = input("<Enter> para continuar")
            Divisões(2)
        else:
            MSG = "Tente Novamente:"
    #Devolve os dados ao dicionario de armazenamento
    return BD
#______________________________________________________________________________________________________________________
#Excluir
def Excluir(BD):
    cancel = False
    Divisões(1)
    print("")
    print("Apagando o Usuário:")
    #Sepação
    print("")
    Divisões(2)
    print("")
    MSG = "Digite o CPF do usuario que deseja excluir: "
    #Repete ate o cpf for cadastrado
    while cancel == False:
        chave = input(MSG)
        #caso não seja cancelado
        if chave != "-1":
            #Verifica se cpf é cadastrado
            chave = cpf(chave)
            valor = BD.get(chave, False)
            #Se não 
            if valor == False:
                ERRO("CPF não Cadastrado!")
                MSG = "Tente novamente ou digite -1 para cancelar:"
            #Se sim
            else:
                User = (chave, valor)
                NBD = BD.copy()
                NBD.pop(chave)
                #Exibe os dados do usuario Selecionado
                print("Os dados do Usuário Selecionado são:")
                Exibir(User)
                Divisões(2)
                print("")
                #Pergunta se tem certeza que quer excluir
                if SorN("Você tem certeza que quer excluir?")== True:
                    BD = NBD.copy()
                    #Informa que os dados foram excluidos
                    Divisões(2)
                    print("")
                    print("Usuario Excluido com Sucesso!")
                                    
                else:
                    #Informa que o processo foi cancelado
                    print("")
                    Divisões(2)
                    print("")
                    print("Processo Cancelado com Sucesso!")
                cancel = True
        else:
            #Informa que o processo foi cancelado
            print("")
            Divisões(2)
            print("")
            print("Processo Cancelado com Sucesso!")
            cancel = True
    #Espera a confirmação para continuar
    Divisões(2)
    print("")
    continuar = input("<Enter> para continuar")
    Divisões(2)
    #Devolve os dados ao dicionario de armazenamento 
    return BD
#______________________________________________________________________________________________________________________
#Extras

#Verifica se o CPF é valido
def cpf(CPF):
    CPF = CPF.strip()
    #Arruma o cpf 
    if "." not in CPF and "-" not in CPF:
        CPF = ArrumaCPF(CPF, 2)
    elif "." not in CPF:
        CPF = ArrumaCPF(CPF, '.')
    elif "-" not in CPF:
        CPF = ArrumaCPF(CPF, '-')

   #Separa e verifica se cada parte é válida
    Pcpf = CPF.split(".")
    P = Pcpf[-1].split("-")[1]
    Pcpf[-1]=Pcpf[-1].split("-")[0]
    erro = False
    for i in Pcpf:
        if len(i) != 3 or NumeroINT(i) == False:
            erro = True
    if erro == True or len(P) != 2 or NumeroINT(P) == False:
        ERRO("CPF inválido!")
        CPF = cpf(input("tente novamente: ").strip())
    #Retorna o CPF pronto
    return CPF
#-------------------------------------------------------------------------------------------

#Arruma o CPF
def ArrumaCPF(CPF, falta):
    erro = False
    #Caso não tenha pontos nem o traço
    if falta == 2:
        if len(CPF) == 11:
           CPF = CPF[:3]+"."+CPF[3:6]+"."+CPF[6:9]+"-"+CPF[9:]
        else:
            erro = True
    #Caso não tenha pontos
    elif falta == '.':
        if len(CPF) == 12:
             CPF = CPF[:3]+"."+CPF[3:6]+"."+CPF[6:9]+CPF[9:]
        else:
             erro = True
    #Caso não tenha o traço
    elif falta == '-':
        if len(CPF) == 13:
             CPF = CPF[:11]+"-"+CPF[11:]
        else:
             erro = True
    #Caso de erro
    if erro == True:
        ERRO("CPF inválido!")
        CPF = cpf(input("tente novamente: ").strip())
    #Retorna o CPF arrumado
    return CPF
#-------------------------------------------------------------------------------------------

#Verifica se algo existe
def Existe(BD, item):
    tem=False
    for i in BD:
        if item in i:
            return True
    return False
#-------------------------------------------------------------------------------------------

#mensagem de Erro
def ERRO(mensagem):
    Divisões(2)
    print("")
    print("Erro!")
    print(mensagem)
    Divisões(2)
    print("")
    
#-------------------------------------------------------------------------------------------

#Divisões(Decoração)
def Divisões(divisão):
    estilos={1:"-------------------------//-------------------------", 2:"__________________________________________________", 3:"---------------------"} 
    print(estilos[divisão])
    
#-------------------------------------------------------------------------------------------
    
#Verifica se a data é valida
def Data(data):
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
        if Ano(ano)==False:
            ERRO("Ano inválido!")
            print("Tente novamente:")
            Ndata = Data(dia+'/'+mes+'/'+input("Digite o ano(AAAA): "))
        #Caso o mes seja inválido
        elif Mes(mes)==False:
            ERRO("Mes inválido!")
            print("Tente novamente:")
            Ndata = Data(dia+'/'+input("Digite o mes(MM): ")+'/'+ano)
        #Caso o dia seja inválido
        elif Dia(dia,mes,ano) == False:
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
def Dia(dia,mes,ano):
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
def Mes(mes):
    if NumeroINT(mes)==True or '/' in mes:
        mes=int(mes)
        if 1<=mes and mes<=12:
            return True
    return False
#-------------------------------------------------------------------------------------------

#Verifica se o ano é válido
def Ano(ano):
    if NumeroINT(ano)==True or '/' in ano:
        ano=int(ano)
        #Verifica se a pessoa é mais velha viva(16/05/2022) que a pessoa mais velha do mundo (Johanna Mazibuko) e se ela ainda não nasceu
        if ano<1894 or 2022<ano:
            return False
        return True
    return False
#-------------------------------------------------------------------------------------------

#Deixa a primeira letra de cada palavra em maiuscula
def Captalize(string):
    Nstring=""
    string=string.split()
    for palavra in string:
        Npalavra=palavra[0].upper()+palavra[1:].lower()
        Nstring=Nstring+" "+Npalavra
    #retorna a string
    return Nstring.strip()
#-------------------------------------------------------------------------------------------
        
#Verifica se o UF é válido
def UF(Estado):
    if len(Estado)!= 2:
        ERRO("UF inválido!")
        Estado = UF(input("Tente novamente: ").strip().upper() )
    #retorna o uf
    return Estado
#-------------------------------------------------------------------------------------------

#verifica o número da casa é válido
def NumeroCasa(num):
    if NumeroINT(num)==False:
        ERRO("Número Inválido!")
        num = NumeroCasa(input("Tente novamente: "))
    #retorna o número
    return num
#-------------------------------------------------------------------------------------------

#Verifica se pode ser um número inteiro
def NumeroINT(num):
    return num.isdigit()
    #algoritmo improvisado
    '''
    alf=['0','1','2','3','4','5','6','7','8','9']
    num=num.strip()
    for dig in num:
        if dig not in alf:
            return False
    return True
    '''
#-------------------------------------------------------------------------------------------

#Faz uma Pergunta de SIM ou NÃO
def SorN(mensagem):
    resposta = input(mensagem + "(S/N): ").strip().upper()
    #Se a resposta for sim
    if resposta == "S":
        return True
    #Se a resposta for não
    elif resposta == "N":
        return False
    #Se a resposta for inválida
    else:
        ERRO("Resposta Inválidia!")
        return SorN("Tente novamente, digitando 'S' para SIM ou 'N' para NÃO: ")
#-------------------------------------------------------------------------------------------

#Faz uma Pergunta para o Usuario se ele é prof ou aluno
def CATEG(Categ):
    if Categ != "Professor" and Categ != "Aluno":
        ERRO("Resposta Inválida!")
        Categ = CATEG(Captalize(input("Tente novamente(Professor/Aluno): ").strip()))
        print(Categ)
    #retorna a caregoria
    return Categ
#-------------------------------------------------------------------------------------------
 
#Verifica o Email
def EMAIL(email):
    erro=False
    #se corresponde ao modelo de email
    if '@' not in email:
        erro=True
    elif not('.org' in email or '.edu' in email or '.gov' in email or '.com' in email):
        erro=True
    if erro == True:
        ERRO("Email Inválido!")
        email = EMAIL(input("Tente novamente: ").strip())
    #devolve o email
    return email
#-------------------------------------------------------------------------------------------
        
#Verifica o telefone
def Tel(Telefone):
    #separa o ddd do resto do telefone
    Telefone = Telefone.strip().split(")")
    #caso o ddd tenha parenteses
    if len(Telefone)==2:
        Num = Telefone[0][1:]+Telefone[1]
    #caso o ddd não tenha 
    else:
        Num = Telefone[0]
    #se o telefone é um número 
    if NumeroINT(Num) == False:
        ERRO("Número inválidopapo!")
        Telefone = Tel(input("Tente novamente digitando apenas números: ").strip())
    #devolve o telefone
    return ArrumaTel(Num)
#-------------------------------------------------------------------------------------------

#Modifica o Telefone 
def ArrumaTel(Num):
    tel = Num[-9:]
    ddd = Num[:(len(Num)-len(tel))]
    telefone = '+55'+'('+ddd+')'+tel
    #caso o ddd não tenha o 0 ou não seja de 3 digitos
    if len(ddd)==2:
        ddd='0'+ddd
        telefone = '+55'+'('+ddd+')'+tel
    elif len(ddd)!=3:
        #caso seja numero fixo
        if tel[1] == '3':
            telefone = ArrumaFix(Num)
        #erro
        else:
            ERRO("Telefone inválido!")
            telefone = Tel(input("Tente novamente: ").strip())
    #Retorna o telefone
    return telefone
#-------------------------------------------------------------------------------------------

#Modifica o Telefone Fixo
def ArrumaFix(Num):
    tel = Num[-8:]
    ddd = Num[:(len(Num)-len(tel))]
    telefone = '+55'+'('+ddd+')'+tel
    #caso o ddd não tenha o 0 ou não seja de 3 digitos
    if len(ddd)==2:
        ddd='0'+ddd
        telefone = '+55'+'('+ddd+')'+tel
    #erro
    elif len(ddd)!=3:
        ERRO("Telefone inválido!")
        telefone = Tel(input("Tente novamente: ").strip())
    #Retorna o telefone
    return telefone
#-------------------------------------------------------------------------------------------

#Exibir
def Exibir(usuario):
    #Nome
    Divisões(2)
    print("")
    print(f"Nome: {usuario[1][0]}")
    print("")
    Divisões(3)
    print("")
    #Dados
    print(f"CPF: {usuario[0]}")
    print(f"Data de Nascimento: {usuario[1][4]}")
    print(f"Categoria: {usuario[1][5]}")
    print("")
    Divisões(3)
    print("")
    #Endereço
    print(f"Endereço: {usuario[1][1][2]}, {usuario[1][1][3]} {usuario[1][1][4]}, {usuario[1][1][0]}-{usuario[1][1][1]} ")
    print("")
    Divisões(3)
    print("")
    #Contato
    print(f"Email: {usuario[1][2]}")
    print(f"Telefone: {usuario[1][3]}")
    print("")
#-------------------------------------------------------------------------------------------

#Monta um item específico de um dicionário
def itensDIC(BD, key, ErroMSG):
    #Verifica se a chave tem um valor no dicionarrio
    valor = BD.get(key, False)
    if valor == False:
        ERRO(ErroMSG)
        key = input("Tente novamente ou cancele digitando '-1': ")
        #caso cancele
        if key == '-1':
            item = 'cancel'
        #caso não cancele
        else:
            item = itensDIC(BD, cpf(key), ErroMSG)
    else:
        #monta o item 
        item = (key, valor)
    #devolve o item
    return item

#-------------------------------------------------------------------------------------------

#Altera a chave
def AltChave(BD, chave, Nchave):
    #Verifica se a chave tem um valor no dicionario
    if BD.get(chave, False) == False:
        ERRO("CPF não cadastrado!")
        chave = input("Tente novamente ou cancele digitando '-1': ")
        #caso não cancele
        if chave != '-1':
            item = AltChave(BD, cpf(chave), Nchave)
        #caso cancele
        else:
            return 'Cancel'
    else:
        parar = False
        while parar == False:
            #Verifica se CPF existe
            if Existe(BD, Nchave) == True:
                #Caso já exista
                ERRO("CPF já existe no sistema!")
                Nchave = input("Tente novamente ou Cancele a ação digitando '-1':")
                if Nchave == '-1':
                    #caso cancela
                    return 'Cancel'
                else:
                    #caso não cancela
                    Nchave = cpf(Nchave)
            else:
                #arruma os valores certinho
                NBD = BD.copy()
                valor = NBD[chave]
                NBD.pop(chave)
                NBD[Nchave] = valor
                parar = True
                item = (Nchave, NBD)
        #retorna o item
        return item
#-------------------------------------------------------------------------------------------
def AltValor(BD, chave, mudança):
    #Verifica se a chave tem um valor no dicionario
    if BD.get(chave, False) == False:
            #erro
            ERRO("CPF não cadastrado!")
            chave = input("Tente novamente ou cancele digitando '-1': ")
            if chave != '-1':
                #caso não cancele
                item = AltValor(BD, cpf(chave), mudança)
            else:
                #caso cancele
                return 'Cancel'
    else:
        Dados = BD[chave]
        #caso mude o nome
        if mudança == "Nome":
            #muda o nome
            Nome = Captalize(input("Digite o nome completo do Usuário: ").strip())
            #adiciona os outros valores
            DataNas = Dados[4]
            Categoria = Dados[5]
            Endereço = Dados[1]
            Email = Dados[2]
            Telefone = Dados[3]
        #caso mude a data de nascimento
        elif mudança == "DataNas":
            #adiciona os outros valores
            Nome = Dados[0]
            #muda a data
            DataNas = Data(input("Digite a data de nascimento (DD/MM/AAAA):  "))
            Categoria = Dados[5]
            Endereço = Dados[1]
            Email = Dados[2]
            Telefone = Dados[3]
        #caso mude a categoria
        elif mudança == "Categ":
            #adiciona os outros valores
            Nome = Dados[0]
            DataNas = Dados[4]
            #muda a categoria
            Categoria = CATEG(Captalize(input("Digite a Categoria (Professor/Aluno): ").strip()))
            Endereço = Dados[1]
            Email = Dados[2]
            Telefone = Dados[3]
        #caso mude o Endereço
        elif mudança == "Endereço":
            #adiciona os outros valores
            Nome = Dados[0]
            DataNas = Dados[4]
            Categoria = Dados[5]
            #muda a cidade
            Cidade = Captalize(input("Digite a Cidade: ").strip())
            #muda o estado
            Estado = UF(input("Digite o Estado(UF): ").strip().upper())
            #muda o bairro
            Bairro = Captalize(input("Digite o Bairro: ").strip())
            #muda a rua
            Rua = Captalize(input("Digite a Rua: ").strip())
            #muda o numero da casa
            Numero = NumeroCasa(input("Digite o número da Casa(sem complemento): ").strip().upper())
            #pergunta se tem complemento
            if SorN("Há complemeto? ") == True:
                #muda o complemento
                Complemento=input("Digite o complemento: ").strip()
            else:
                Complemento=""
            #arruma os dados bonitinho
            Endereço = [Cidade,Estado, Bairro, Rua, Numero + Complemento]
            Email = Dados[2]
            Telefone = Dados[3]
        #caso mude o email
        elif mudança == "Email":
            #adiciona os outros valores
            Nome = Dados[0]
            DataNas = Dados[4]
            Categoria = Dados[5]
            Endereço = Dados[1]
            #muda o email
            Email = EMAIL(input("Digite o Email: ").strip())
            Telefone = Dados[3]
        #caso mude o telefone    
        elif mudança == "Telefone":
            #adiciona os outros valores
            Nome = Dados[0]
            DataNas = Dados[4]
            Categoria = Dados[5]
            Endereço = Dados[1]
            Email = Dados[2]
            #muda o telefone
            Telefone = Tel(input("Digite o Telefone (com o DDD e sem espaços): ").strip())
        #arruma os dados
        NBD = BD.copy()
        NBD[chave] = [Nome, Endereço, Email, Telefone, DataNas, Categoria]
    #Retorna os dados 
    return NBD
#-------------------------------------------------------------------------------------------
#Abre um arquivo e adiciona os dados a um dicionário
def AbrirArquivo(arq):
    #abre o arquivo
    Arqs = open(arq, 'r')
    linha = "a"
    BD = {}
    #repete ate todos os dados tiverem sido processados
    while linha != "":
        linha = Arqs.readline()
        if linha != "":
            #separa as informações 
            linha = linha.split("$separação$")
            key = linha[0]
            valor = [linha[1],linha[2].split("=separ="), linha[3], linha[4], linha[5], linha[6]]
            #adiciona no dicionario
            BD[key] = valor
    #fecha o arquivo
    Arqs.close()
    #retorna o banco de dados
    return BD
#-------------------------------------------------------------------------------------------
#Abre um arquivo e salva os dados de um dicionário
def SalvarArquivo(arq, BD):
    #abre o arquivo
    Arqs = open(arq, 'w')
    texto = ""
    #passa de usuario em usuario 
    for user in BD.items():
        #separa as informações
        cpf = user[0]
        nome = user[1][0]
        endereço = user[1][1][0]+"=separ="+user[1][1][1]+"=separ="+user[1][1][2]+"=separ="+user[1][1][3]+"=separ="+user[1][1][4]
        email = user[1][2]
        tel = user[1][3]
        data = user[1][4]
        categ = user[1][5]
        #junta tudo em um unico texto
        texto = texto + cpf+ "$separação$" +nome+ "$separação$" +endereço+ "$separação$" +email+ "$separação$" +tel+ "$separação$" +data + "$separação$" + categ + "$separação$" + "\n"
    #escreve as informações no arquivo
    Arqs.write(texto)
    #fecha o arquivo
    Arqs.close()
#-------------------------------------------------------------------------------------------
def existe_Arquivo():
    import os
    if os.path.exists("Users.txt"):
        return True
    return False
    
#______________________________________________________________________________________________________________________
#Submenu de Usuários
def SubMenu_Usuarios():
    #cria o arquivo caso não exista
    if not(existe_Arquivo()):
        a = open("Users.txt",'w')
        a.close()
    #Pega os dados do Arquivo
    Usuarios = AbrirArquivo("Users.txt")
    op=""
    MSG = "Digite a opção desejada: "
    #Menu
    print("|---------------------------------------------------------------------------|")
    print("|                                 Usuários                                  |")
    print("|---------------------------------------------------------------------------|")
    while op != '6':
        #Opções
        Divisões(2)
        print("")
        print("Menu de opções:")
        Divisões(2)
        print("")
        print("|---|")
        print("| 1 |", " - Inserir")
        print("|   |")
        print("| 2 |", " - Alterar")
        print("|   |")
        print("| 3 |", " - Pesquisar Usuário")
        print("|   |")
        print("| 4 |", " - Exibir Todos")
        print("|   |")
        print("| 5 |", " - Excluir")
        print("|   |")
        print("| 6 |", " - Voltar")
        print("|---|")
        print("")
        Divisões(2)
        print("")
        #Pergunta a opção
        op = input(MSG).strip()
        Divisões(2)
        print("")
        #Resultado para cada opção
        if op != '6':
            #opção 1
            if op == '1':
                Usuarios = Inserir(Usuarios)
                MSG = "Digite a opção desejada: "
            #opção 2
            elif op == '2':
                Usuarios = Alterar(Usuarios)
                MSG = "Digite a opção desejada: "
            #opção 3
            elif op == '3':
                Exibir_Item(Usuarios)
                MSG = "Digite a opção desejada: "
            #opção 4
            elif op == '4':
                Exibir_Todos(Usuarios)
                MSG = "Digite a opção desejada: "
            #opção 5
            elif op == '5':
                Usuarios = Excluir(Usuarios)
                MSG = "Digite a opção desejada: "
            #opção inválida
            else:
                ERRO("opção inválida!")
                MSG = "Tente Novamente: "
        #opção 6
        else:
            SalvarArquivo("Users.txt", Usuarios)
            #Espera para Continuar
            Divisões(2)
            print("")
            continuar = input("<Enter> para continuar")
            Divisões(2)




