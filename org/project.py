
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


class Cadastro:     

    def salvarbanco(values):
        query = "INSERT INTO parents(name, sunname, email, phone, agr, address, password) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        values1 = (values[0], values[5], values[1], values[2], values[3], values[4], values[9])

        cursor.execute(query, values1)
        db.commit()
        print(cursor.rowcount, "record inserted")

        query2 = "INSERT INTO student(name, namepais, addres, birth, age, telpais, emailpais, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        values2 = (values[5], values[0], values[4], values[6], values[7], values[2], values[1], values[9])

        cursor.execute(query2, values2)
        db.commit()
        print(cursor.rowcount, "record inserted")

        
    def cadastrar():
        dic = {'name': None, 'email': None, 'phone': None, 'age': None, 'address': None, 'sun name': None, 'birth sun': None, 'sun age': None, 'password': None, 'sun password': None }
        values = []
        for i in dic:
            v = input(i, " :")
            dic[i] = v
        if ('' in dic.values()):
            print('complete todos os campos')
            return Cadastro.cadastrar()

        for i in dic:
            values.append(dic[i])
        return Cadastro.salvarbanco(values)



class adminscreen():
    def __init__():
        permi = [t.__name__ for t in adminscreen.__subclasses__()]
        print("Escolha uma opção")
        for i, t in enumerate(permi):
            print(f'{i}) {t}')
        escolha = int(input(""))
        return adminscreen.__subclasses__()[escolha]()

class SaveCadProf():
    def __init__(dados):
        query4 = "INSERT INTO teacher(name, age, password, formacao, email, turma) VALUES(%s, %s, %s, %s, %s, %s) "
        values4 = (dados[0], dados[1], dados[5], dados[3], dados[2], dados[4])

        cursor.execute(query4, values4)
        db.commit()
        print(cursor.rowcount, "record inserted")

class CadProf(adminscreen):
    def __init__(self):
        dadoprof = {'name': None, 'idade': None, 'email': None, 'materia': None, 'turmas':[], 'password': None}
        dados = []
        for i in dadoprof:
            v = input(i, " :")
            dadoprof[i] = v
        if ('' in dadoprof.values()):
            print('complete todos os campos')
        return CadProf()

        for i in dadoprof:
            dados.append(dadoprof[i])
        return SaveCadProf(dados)

class AprovaMatri(adminscreen):
    def __init__(self):
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

class sair(adminscreen):
    def __init__(self):
        return inicio()


class studentscreen():
    def __init__(self, nome, turma, id):
        permi = [t.__name__ for t in studentscreen.__subclasses__()]
        print("Escolha uma opção")
        for i, t in enumerate(permi):
            print(f'{i}) {t}')
        escolha = int(input(""))
        return studentscreen.__subclasses__()[escolha](nome, turma, id)


class notas(studentscreen):
    def __init__(self, nome, turma, id):
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

class aviso(studentscreen):
    def __init__(self, nome, turma, id):
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


class provas(studentscreen):
    def __init__(self, nome, turma, id):
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

class sair(studentscreen):
    def __init__(self, nome, turma, id):
        return inicio()



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

class Login:
    def login():
        print("\n LOGIN  ")
        nome = input("Nome: ")
        password = input("Password: ")
        if nome == "Administrador" and password == 12345:
            return adminscreen 
        permi = [t.__name__ for t in Login.__subclasses__()]
        print("Escolha uma permição")
        for i, t in enumerate(permi):
            print(f'{i}) {t}')
        permição = int(input('Permição : '))
        return Login.__subclasses__()[permição](nome, password)
     

class student(Login):
    def __init__(self, nome, password):
        query = "SELECT name, password, turma, id FROM student"
        cursor.execute(query)
        record= cursor.fetchall()

        for linha in record:
            print(linha)
            if nome == linha[0]:
                if linha[1] == password:
                    turma = linha[2]
                    id = linha[3]
                    return studentscreen(nome, turma, id)

                else:
                    print("Senha errada")
                    return Login.login()
        else:
            print("Nome não encontrado")
            return Login.login()

class professor(Login):
    def __init__(self, nome, password):
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
                    return Login.login()
        else:
            print("Nome não encontrado")
            return Login.login()
            

def inicio():
    print("Bem vindo ao sistemaa escolar")
    print("(1) Login")
    print("(2) Cadastro/Matricula")
    escolha = int(input("Escolha uma das opções: "))
           
    
    if escolha == 2:
        return Cadastro.cadastrar()
    if escolha == 1:
        return Login.login()
    if escolha != (1 or 2):
        print("Escolha entre uma das opções\n")
        return inicio()


#Bateria de teste (pyteste, seliniun)
inicio()