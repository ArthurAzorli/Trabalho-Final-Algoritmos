from Submenu_de_Usuarios import *
from Submenu_de_livros import *
from Submenu_de_Emprestimos import *
from Relatório import *
Divisões(2)
print("")
print("----Programa Inicializado----")
Divisões(2)
#Espera a confirmação para continuar
Divisões(2)
print("")
continuar = input("<Enter> para continuar")
Divisões(2)
op=""
MSG = "Digite a opção desejada: "
#Menu
titulo = True
while op != '5':
    if titulo:
        print("")
        print("|---------------------------------------------------------------------------|")
        print("|                                                                           |")
        print("|                                Bliblioteca                                |")
        print("|                                                                           |")
        print("|---------------------------------------------------------------------------|") 
    #Opções
    Divisões(2)
    print("")
    print("Menu de opções:")
    Divisões(2)
    print("")
    print("|---|")
    print("| 1 |", " - Usuários")
    print("|   |")
    print("| 2 |", " - Livros")
    print("|   |")
    print("| 3 |", " - Emprestimos")
    print("|   |")
    print("| 4 |", " - Relatório")
    print("|   |")
    print("| 5 |", " - Fechar")
    print("|---|")
    print("")
    Divisões(2)
    print("")
    #Pergunta a opção
    op = input(MSG).strip()
    Divisões(2)
    print("")
    #Resultado para cada opção
    if op != '5':
        #opção 1
        if op == '1':
            SubMenu_Usuarios()
            MSG = "Digite a opção desejada: "
            titulo = True
        #opção 2
        elif op == '2':
            SubMenu_Livros()
            MSG = "Digite a opção desejada: "
            titulo = True
        #opção 3
        elif op == '3':
            submenuempre()
            MSG = "Digite a opção desejada: "
            titulo = True
        #opção 4
        elif op == '4':
            Relatorio()
            MSG = "Digite a opção desejada: "
            titulo = True
        #opção inválida
        else:
            ERRO("opção inválida!")
            MSG = "Tente Novamente: "
            titulo = False
    #opção 5
    else:
        Divisões(2)
        print("")
        print("----Programa Finalizado----")
        Divisões(2)
        #Espera a confirmação para continuar
        Divisões(2)
        print("")
        continuar = input("<Enter> para continuar")
        Divisões(2)
        print("")
        print("Tchau!")
