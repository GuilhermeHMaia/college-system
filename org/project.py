def cadunico():
    print("ok")

def login():
    print("ok")


def inicio():
    print("Bem vindo ao sistema escolar")
    print("(1) Login")
    print("(2) Cadastro")
    escolha = int(input("Escolha uma das opções: "))
           
    
    if escolha == 2:
        return cadunico()
    if escolha == 1:
        return login()
    if escolha != (1 or 2):
        print("Escolha entre uma das opções\n")
        return inicio()

inicio()