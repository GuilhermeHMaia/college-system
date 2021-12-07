
import mysql.connector as mysql
from datetime import date
from datetime import date
import getpass

db = mysql.connect(host = "localhost",
                   user = "root",
                   password = "",
                   database = "school"
                   )
cursor = db.cursor()

def cadunico():
    print("\nPreencha os campos a seguir com seus dados e os dados do seu filho")
    nome = input("Full name: ")
    email = input("Email: ")
    phone = int(input("Phone: "))
    age = int(input("age: "))
    address = input("address: ")
    sunname = input("Sun name: ")
    birth = input("Sun birth: ")
    sunage = int(input("Sun age: "))
    password = getpass.getpass("passaword: ")
    sunpass = getpass.getpass("Sun password")
    nome = nome.title()
    sunname = sunname.title()
    if nome=='' or email=='' or phone =='' or age=='' or address=='' or sunname=='' or birth=='' or password=='' or sunpass=='':
        print("Todos os campos devem ser preenchidos")
        return cadunico()

    query = "INSERT INTO parents(name, sunname, email, phone, agr, address, password) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (nome, sunname, email, phone, age, address, password)

    cursor.execute(query, values)
    db.commit()
    print(cursor.rowcount, "record inserted")

    
    query2 = "INSERT INTO student(name, namepais, addres, birth, age, telpais, emailpais, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    values2 = (sunname, nome, address, birth,sunage, phone, email, sunpass)

    cursor.execute(query2, values2)
    db.commit()
    print(cursor.rowcount, "record inserted")



    print(nome, email, phone, age, address, sunname, birth, password, sunpass)


def adminscreen():
    
    
    print("\nADMINSCREEN")
    print("(1) Cadastrar professor")
    print("(2) Aprovar matriculas")
    escolha = int(input(""))
    #Fazer com que as escolhas levem a outras funções, como Cadprof()
    if escolha == 1:
        print("\nEntre com os dados cadastrais do professor")
        name = input("Nome do professor: ")
        idade = int(input("Idade do professor: "))
        email = input("email teacher: ")
        materia = input("Matéria a ser oferecida: ")
        turmas = input("Turmas responsaveis: ")
        password = getpass.getpass("Password: ")

        if name == '' or idade =='' or materia =='' or turmas =='' or password =='':
            print("Todos os campos devem ser preenchidos")
            return adminscreen()
        query4 = "INSERT INTO teacher(name, age, password, formacao, email, turma) VALUES(%s, %s, %s, %s, %s, %s) "
        values4 = (name, idade, password, materia, email, turmas)

        cursor.execute(query4, values4)
        db.commit()
        print(cursor.rowcount, "record inserted")



    if escolha == 2:
        query = "SELECT insun, id , name, sunname, email, phone, agr, address FROM parents"
        cursor.execute(query)
        record = cursor.fetchall()

        for linha in record:
            
            if None in linha:
                print("\nFICHA CADASTRAL PARENTS")
                print("id: ", linha[1])
                print("Nome: ", linha[2])
                print("Sun name: ", linha[3])
                print("Email: ", linha[4])
                print("Phone: ", linha[5])
                print("Age: ", linha[6])
                print("Address: ", linha[7])
                inc = linha[1]

                query = "SELECT * FROM student WHERE id = %s"
                values2 = (inc,)
                cursor.execute(query, values2)
                record2 = cursor.fetchall()
                aluno = record2[0]
                print("\nFICHA CADASTRAL SUN")
                print("id: ", aluno[0])
                print("name: ", aluno[1])
                print("parents name: ", aluno[2])
                print("address: ", aluno[3])
                print("Birth: ", aluno[4])
                print("age: ", aluno[5])
                print("parents phone: ", aluno[6])
                print("parents email: ", aluno[7])

                print("\nAprovar matricula")
                escolha = int(input("(1) Yes or (2) Not"))
                if escolha == 1:
                    turma =input("Informe a turma ao qual o aluno será matriculado: ")
                    print(turma)


                    query3 = "UPDATE student SET turma = %s WHERE id = %s"
                
                    values3 = (turma,inc)
 
                    cursor.execute(query3, values3)
                    db.commit()
                    print(cursor.rowcount, "record inserted")


                    query2 = "UPDATE parents SET insun = %s WHERE id = %s"
                
                    values2 = (inc,inc)
 
                    cursor.execute(query2, values2)
                    db.commit()
                    print(cursor.rowcount, "record inserted") 

    print("Não há mais pedidos de matricula")
    return adminscreen()


def screenstudent(nome):   
    print("\nWelcome the student screen")
    # coisas como, ver nota, com desempenho, ver presença, avisos, data das provas, horário aulas.

def avisos():
    print("\nDigite seu aviso!")
    aviso = input(":")
    data = date.today()
    #data = str(mu)

    print(aviso)
    print(data)
    query = "INSERT INTO avisos(data, aviso) VALUES ( %s, %s)"
    values = (data, aviso)

    cursor.execute(query, values)
    db.commit()
    print(cursor.rowcount, "Record inserted")

def screenteacher(nome):
    #coisas como, adicionar nota, presença, avisos, data de provas, consultar ficha de aluno
    print("\nWelcome the teacher screen")   
    print("  Olá ", nome)
    print("(1) Adicionar aviso")
    print("(2) Adiconar notas")
    print("(3) Adicionar data de provas")
    print("(4) Adiconar presença")
    print("(5) Consultar ficha de aluno")
    print("(6) Exit")
    choise = int(input(""))

    #Avisos, usar id, data, e campo de avisos

    if choise == 1:
        return avisos()

    if choise == 6:
        breakpoint



              



def login():
    print("\nFaça o login no sistema")
    nome = input("Digite seu nome: ")
    password = getpass.getpass("Digite sua senha: ")
    print("Escolhar uma permição")
    fun = int(input("(1) Student or (2) teacher or (3) Parents"))

    if nome == "Administrador" and password == "2121":
        return adminscreen()

    if fun == 1:
        query = "SELECT name, password FROM student"
        cursor.execute(query)
        record= cursor.fetchall()

        for linha in record:
            if nome == linha[0]:
                if linha[1] == password:
                    return screenstudent(nome)

    if fun == 2:
        query2 = "SELECT name, password FROM teacher"
        cursor.execute(query2)
        record2 = cursor.fetchall()

        for linha in record2:
            if nome == linha[0]:
                if linha[1] == password:
                    return screenteacher(nome)
                else:
                    print("Senha errada")
                    return login()
            else:
                print("Nome não encontrado")
                return login()
            

def inicio():
    print("Bem vindo ao sistema escolar")
    print("(1) Login")
    print("(2) Cadastro/Matricula")
    escolha = int(input("Escolha uma das opções: "))
           
    
    if escolha == 2:
        return cadunico()
    if escolha == 1:
        return login()
    if escolha != (1 or 2):
        print("Escolha entre uma das opções\n")
        return inicio()

inicio()