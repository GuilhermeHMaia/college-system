
import mysql.connector as mysql
from datetime import date
from datetime import date

db = mysql.connect(host = "localhost",
                   user = "root",
                   password = "",
                   database = "school"
                   )
cursor = db.cursor()

def cadunico():
    print("Preencha os campos a seguir com seus dados e os dados do seu filho")
    nome = input("Full name: ")
    email = input("Email: ")
    phone = int(input("Phone: "))
    age = int(input("age: "))
    address = input("address: ")
    sunname = input("Sun name: ")
    birth = input("Sun birth: ")
    sunage = int(input("Sun age: "))
    password = input("passaword: ")
    sunpass = input("Sun password")
    nome = nome.title()
    sunname = sunname.title()
    if nome=='' or email=='' or phone =='' or age=='' or address=='' or sunname=='' or birth=='' or password=='' or sunpass=='':
        print("Todos os campos devem ser preenchidos")
        return cadunico

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
    print("Bem vindo a screen do administrador")
    print("Admin Screen")
    print("(1) Cadastrar professor")
    print("(2) Aprovar matriculas")
    escolha = int(input(""))
    
    if escolha == 2:
        query = "SELECT insun, id , name, sunname, email, phone, agr, address FROM parents"
        cursor.execute(query)
        record = cursor.fetchall()

        for linha in record:
            
            if None in linha:
                print("id: ", linha[1])
                print("Nome: ", linha[2])
                print("Sun name: ", linha[3])
                print("Email: ", linha[4])
                print("Phone: ", linha[5])
                print("Age: ", linha[6])
                print("Address: ", linha[7])
                inc = linha[1]

                
                

                """query2 = "UPDATE parents SET insun = %s WHERE id = %s"
                
                values2 = (inc,inc)

                cursor.execute(query2, values2)
                db.commit()
                print(cursor.rowcount, "record inserted")"""
            
            
                



def login():
    print("Faça o login no sistema")
    nome = input("Digite seu nome: ")
    password = input("Digite sua senha: ")

    if nome == "Administrador" and password == "2121":
        return adminscreen()

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