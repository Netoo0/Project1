from os import link
from PyQt5 import uic, QtWidgets
import sqlite3


class appdelogin():
    def login(self):
        usuario = tela.lineEdit.text()
        senha = tela.lineEdit_2.text()
        banco = sqlite3.connect('usuarios_cadastrados.db')
        cursor = banco.cursor()
        try:
            cursor.execute(
                "SELECT senha FROM cadastro WHERE login ='{}'".format(usuario))
            senhadb = cursor.fetchall()
            banco.close()
        except:
            print("Login não cadastrado no banco de dados")
        if senha == senhadb[0][0]:
            print("logado")
            tela.close()
            tela2.show()
        elif senha != senhadb[0][0]:
            tela.label_4.setText("Dados incorretos!!")

    def abrirtelacadastro(self):
        tela.close()
        tela3.show()

    def cadastro(self):
        nome = tela3.lineEdit.text()
        login = tela3.lineEdit_2.text()
        senha = tela3.lineEdit_3.text()
        rpsenha = tela3.lineEdit_4.text()
        if senha == rpsenha:
            if any(x.isupper() for x in senha):
                try:
                    banco = sqlite3.connect('usuarios_cadastrados.db')
                    cursor = banco.cursor()
                    cursor.execute(
                        "CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
                    cursor.execute("INSERT INTO cadastro VALUES ('" +
                                nome+"','"+login+"','"+senha+"')")
                    banco.commit()
                    banco.close()
                    tela3.label_6.setText("Você foi cadastrado com sucesso")
                    tela3.close()
                    tela.show()
                except sqlite3.Error as erro:
                    print("Erro ao inserir os dados: ", erro)
            else:
                tela3.label_6.setText("Você deve colocar letra maiuscula e minuscula")
        else:
            tela3.label_6.setText("As senhas digitadas estão diferentes")

    def sair(self):
        tela2.close()


app = QtWidgets.QApplication([])
tela = uic.loadUi("Telainicial.ui")
tela2 = uic.loadUi("tela2.ui")
tela3 = uic.loadUi("tela3.ui")
tela.pushButton.clicked.connect(appdelogin.login)
tela.pushButton_2.clicked.connect(appdelogin.abrirtelacadastro)
tela2.pushButton.clicked.connect(appdelogin.sair)
tela3.pushButton.clicked.connect(appdelogin.cadastro)


tela.show()
app.exec()
