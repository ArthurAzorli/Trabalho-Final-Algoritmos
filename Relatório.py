from Submenu_de_Emprestimos import *
from datetime import *

def Relatorio():
    #cria o arquivo caso não exista
    if not(existe_Arquivoe()):
        a = open("loan.txt",'w')
        a.close()
    #Pega os dados do Arquivo
    emprestimos = abrirarqe("loan.txt")
    #cria o arquivo caso não exista
    if not(existe_Arquivo()):
        a = open("Users.txt",'w')
        a.close()
    #Pega os dados do Arquivo
    Usuarios = AbrirArquivo("Users.txt")
    #cria o arquivo caso não exista
    if not (existe_ArquivoL()):
        a = open("livros.txt", 'w')
        a.close()
    #Pega os dados do Arquivo
    BBdoslivros = abrirarq("livros.txt")
    #Relátorio
    print("|---------------------------------------------------------------------------|")
    print("|                                 Relatório                                 |")
    print("|---------------------------------------------------------------------------|")
    parar = False
    print("")
    while parar != True:
        Divisões(2)
        print("")
        #Pergunta as datas para a pesquisa
        Data1=datetime.strptime(Data(input("Digite a data inicial(DD/MM/AAAA):")), '%d/%m/%Y')
        Data2=datetime.strptime(Datae(input("Digite a data final(DD/MM/AAAA):")), '%d/%m/%Y')
        Divisões(2)
        #Arruma adequadamente as datas
        if Data1<Data2:
            DataC = Data1
            DataF = Data2
        else:
            DataC = Data2
            DataF = Data1
        escreveu = False
        #Pesquisa 
        for empres in emprestimos.items():
            multa = False
            #Pega a data de retirada
            DataP = datetime.strptime(empres[1][0], '%d/%m/%Y')
            #Pega a data de devolução
            DataD = datetime.strptime(empres[1][1], '%d/%m/%Y')
            #Pega o dia de hoje
            Hoje = datetime.strptime(formatardatetime(date.today()), '%d/%m/%Y')
            #Verifica se a data de devolução esta entres a datas entregues
            if DataF >= DataD and DataD >= DataC:
                #Se sim
                escreveu = True
                Divisões(2)
                print("")
                #Escreve o nome
                print(f"Usuário: {Usuarios[empres[0][0]][0]}")
                #Escreve o cpf
                print(f"CPF: {empres[0][0]}")
                Divisões(3)
                #Escreve o titulo do livro
                print(f"Livro: {BBdoslivros[int(empres[0][1])][0]}")
                #Escreve o Isbn
                print(f"ISBN: {empres[0][1]}")
                Divisões(3)
                #Escreve a data de retirada
                print(f"Data de Retirada: {DataP.day}/{DataP.month}/{DataP.year}")
                #Escreve a data de devoluçao
                print(f"Data de Devolução: {DataD.day}/{DataD.month}/{DataD.year}")
                Divisões(3)
                #Escreve o tempo restante para a devolução
                print(f"Tempo Restante para Entrega: ", end="")
                if int((DataD-Hoje).days) < 0:
                    #Se o livro estiver atrasado
                    multa = True
                    print(f"{int((DataD-Hoje).days)*-1} dia(s) atrasado(s)")
                else:
                    #Senão
                    print(f"{int((DataD-Hoje).days)} dia(s)")          
                print(f"Valor de multa de atraso por dia: R$ {float(empres[1][2][:2])}")
                #Se estiver atrasado escreve a o total da multa até então
                if multa:
                    print(f"Valor da Multa Total: R$ {float((Hoje-DataD).days)*float(empres[1][2][:2])}")
                Divisões(2)
        if escreveu==False:
            #caso não tenha emprestimos entre as datas entregues
            Divisões(2)
            print("")
            print("Sem Emprestimos entres estas Datas!")
            Divisões(2)
        Divisões(2)
        print("")
        #Ao final pergunta se o usuario quer voltar ao menu principal ou continuar no relatorio
        parar = SorN("Deseja Voltar para o Menu?")
        Divisões(2)
    #Espera a confirmação para continuar
    Divisões(2)
    print("")
    continuar = input("<Enter> para continuar")
    Divisões(2)
            
