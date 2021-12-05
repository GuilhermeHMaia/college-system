import mysql.connector as mysql
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



    print(nome, email, phone, age, address, sunname, birth, password, sunpass)


def adminscreen():
    print("Bem vindo a screen do administrados")
    

def login():
    print("Faça o login no sistema")
    nome = input("Digite seu nome: ")
    password = input("Digite sua senha: ")

    if nome == "Administrados" and password == "2121":
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