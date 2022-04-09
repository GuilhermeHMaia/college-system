
from logging import log
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
    print("(3) Sair")
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



    if escolha == 3:
        return inicio()
    
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
                    turma = turma.upper()
                    turma = turma.replace(' ', '')
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

    


def studentscreen(nome, turma, id):   
    print("\nWelcome the student screen")
    print("(1) Ver notas")
    print("(2) Avisos")
    print("(3) ver data de provas")
    print("(4) Sair")
    escolha = int(input(""))
    nome = nome
    turma = turma
    id = id
    # coisas como, ver nota, com desempenho, ver presença, avisos, data das provas, horário aulas.

    if escolha == 1:
        query = "SELECT data, nota, sequencia, materia, comentariO FROM notas WHERE id = %s"
        values = (id,)

        cursor.execute(query, values)
        record = cursor.fetchall()
        for x in range(len(record)):
            data = record[x][0]
            nota = record[x][1]
            sequencia = record[x][2]
            materia = record[x][3]
            comentario = record[x][4]
            print(" Dia: ", data ,", Matéria: ", materia  ,", Sequencia", sequencia  ,", Nota: ", nota  ,", Comentários: ", comentario)
        
        toque = input("")
        if toque == '':
            return studentscreen(nome, turma, id)

    if escolha == 2:
        query2 = "SELECT data, aviso FROM avisos WHERE turma = %s"
        values2 = (turma, )

        cursor.execute(query2, values2)
        record = cursor.fetchall()
        for x in range(len(record)):
            data = record[x][0]
            aviso = record[x][1]
            print("Data: ", data , "- Aviso: ", aviso)
        toque = input("")
        if toque == '':
            return studentscreen(nome, turma, id)

    if escolha == 3:
        query3 = "SELECT data, sequencia, comentario FROM provas WHERE turma = %s"
        values3 = (turma,)

        cursor.execute(query3, values3)
        record = cursor.fetchall()
        for x in range(len(record)):
            data = record[x][0]
            sequencia = record[x][1]
            comentario = record[x][2]
            print("Data da prova: ", data , " - Sequência: ", sequencia , "- Comentário: ", comentario)
        toque = input("")
        if toque == '':
            return studentscreen(nome, turma, id)

    if escolha == 4:
        return studentscreen(nome, turma, id)

def avisos(nome, formacao):
    print("\nDigite seu aviso!")
    aviso = input(":")
    turma = input("Digite a turma: ")
    turma = turma.upper()
    turma = turma.replace(' ', '')
    data = date.today()

    print(aviso)
    print(data)
    query = "INSERT INTO avisos(data, aviso, turma) VALUES ( %s, %s, %s)"
    values = (data, aviso, turma)

    cursor.execute(query, values)
    db.commit()
    print(cursor.rowcount, "Record inserted")
    return teacherscreen(nome, formacao)

def nota(nome,formacao):
    # escolha da turma, filtragem com nome e id,nota, data que a prova foi aplicada e sequência da prova ( primeira, segunda), comentario?
    turma = input("\nEscolha uma turma: ")
    prova = input("Digite o dia em que a prova foi aplicada")
    sequen = input("Digite a ordem da prova, (Primeira, Segunda ...")
    turma = turma.upper()
    turma = turma.replace(' ', '')
    print(turma)
    query = "SELECT name, id FROM student WHERE turma = %s"
    values = (turma, )

    cursor.execute(query, values)
    record = cursor.fetchall()
    for linha in record:
        print("Aluno: ", linha[0])
        nota = int(input("Digite a nota do aluno :"))
        comentário = input("Digite um comentário: ")
        aluno = str(linha[0])
        mat = int(linha[1])
    
        query2 = "INSERT INTO notas (id, data, name, nota, sequencia, turma, materia, comentario) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        values2 = (mat, prova, aluno, nota, sequen, turma, formacao, comentário)

        cursor.execute(query2, values2)
        db.commit()
        print(cursor.rowcount, "Record inserted")
    return teacherscreen(nome, formacao)

    
def teacherscreen(nome, formacao):
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

    if choise == 2:
        return nota(nome, formacao)

    if choise == 1:
        return avisos(nome, formacao)

    if choise == 3:
        #sequencia da prova, turma, dia da prova, comentário
        turma = input("Para qual turma será aplicada a prova: ")
        turma = turma.upper()
        turma = turma.replace(' ', '')
        prova = input("Digite o dia da prova: ")
        sequen = input("Digite a sequencia da prova (primeira, segunda)")
        comentario = input("Comentário: ")

        query3 = "INSERT INTO provas(data, turma, sequencia, comentario) VALUES (%s, %s, %s, %s)"
        values3 = (prova, turma, sequen, comentario)

        cursor.execute(query3, values3)
        db.commit()
        print(cursor.rowcount, "Record Inserted")        

    if choise == 5:
        query2 = "SELECT * FROM student"
        cursor.execute(query2)
        record = cursor.fetchall()
        aluno = int(input("Digite o id do aluno:"))
        for linha in record:
            if linha[0] == aluno:
                print("Id: ", linha[0])
                print("Aluno: ", linha[1])
                print("Parents: ", linha[2])
                print("Address: ", linha[3])
                print("Birth: ", linha[4])
                print("Age: ", linha[5])
                print("Contato: ", linha[6])
                print("Turma: ", linha[8])

    if choise == 6:
        return inicio()


def login():
    print("\nFaça o login no sistema")
    nome = input("Digite seu nome: ")
    password = getpass.getpass("Digite sua senha: ")
    print("Escolhar uma permição")
    fun = int(input("(1) Student or (2) teacher or (3) Parents"))

    #Criar as excessões
    

    if nome == "Administrador" and password == "2121":
        return adminscreen()

    if fun == 1:
        query = "SELECT name, password, turma, id FROM student"
        cursor.execute(query)
        record= cursor.fetchall()

        for linha in record:
            if nome == linha[0]:
                if linha[1] == password:
                    turma = linha[2]
                    id = linha[3]
                    return studentscreen(nome, turma, id)

                else:
                    print("Senha errada")
                    return login()
            else:
                print("Nome não encontrado")
                return login()

    if fun == 2:
        query2 = "SELECT name, password, formacao FROM teacher"
        cursor.execute(query2)
        record2 = cursor.fetchall()

        for linha in record2:
            if nome == linha[0]:
                if linha[1] == password:
                    formacao = linha[2]
                    return teacherscreen(nome, formacao)
                else:
                    print("Senha errada")
                    return login()
            else:
                print("Nome não encontrado")
                return login()
            

def inicio():
    print("Bem vindo ao sistemaa escolar")
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