#Criação do datebase
"""import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
    )

cursor = db.cursor()

cursor.execute("CREATE DATABASE school")"""

#Criação da Table Student Profile
# inscrição, Nome dos pais,nome do aluno, endereço, data de nascimento, idade, genero, telefone e email dos pais, turma, password
"""import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "school"
    )

cursor = db.cursor()

#cursor.execute("CREATE TABLE student( name VARCHAR(255), namepais VARCHAR(255), addres VARCHAR(255), birth VARCHAR(255), age INT(11), telpais INT(11), emailpais VARCHAR(255), turma VARCHAR(255), password VARCHAR(255))") 
cursor.execute("ALTER TABLE student ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
cursor.execute("DESC student")"""


#criação da Table Pais:
#Nome, nome do filho, email, telefone, endereço, idade, password, inscrição filho

"""import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "school"
    )

cursor = db.cursor()

#cursor.execute("CREATE TABLE parents(name VARCHAR(255), sunname VARCHAR(255), email VARCHAR(255), phone INT(11), agr INT(11), address VARCHAR(255), password VARCHAR(255), insun INT(11))")
cursor.execute("ALTER TABLE parents ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
cursor.execute("DESC parents")"""


#Criação da Table professor
#nome, idade, password, formação, email

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "school"
    )

cursor = db.cursor()

#cursor.execute("CREATE TABLE teacher(name VARCHAR(255), age INT(11), password VARCHAR(255), formacao VARCHAR(255), email VARCHAR(255))") 
#cursor.execute("ALTER TABLE teacher ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
cursor.execute("ALTER TABLE teacher ADD COLUMN turma VARCHAR(255)")
cursor.execute("DESC teacher")