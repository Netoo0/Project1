from os import link
from PyQt5 import uic, QtWidgets
import sqlite3


class AppDeLogin:
    def __init__(self):
        self.tela = uic.loadUi("Telainicial.ui")
        self.tela2 = uic.loadUi("tela2.ui")
        self.tela3 = uic.loadUi("tela3.ui")
        
        self.tela.pushButton.clicked.connect(self.login)
        self.tela.pushButton_2.clicked.connect(self.abrir_tela_cadastro)
        self.tela2.pushButton.clicked.connect(self.sair)
        self.tela3.pushButton.clicked.connect(self.cadastrar_usuario)
        
        self.banco = sqlite3.connect('usuarios_cadastrados.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, login text, senha text)")
        
    def login(self):
        usuario = self.tela.lineEdit.text()
        senha = self.tela.lineEdit_2.text()
        
        try:
            self.cursor.execute(
                "SELECT senha FROM cadastro WHERE login = ?", (usuario,))
            senhadb = self.cursor.fetchone()
        except sqlite3.Error:
            print("Login não cadastrado no banco de dados")
            return
        
        if senhadb is not None and senha == senhadb[0]:
            print("logado")
            self.tela.close()
            self.tela2.show()
        else:
            self.tela.label_4.setText("Dados incorretos!!")

    def abrir_tela_cadastro(self):
        self.tela.close()
        self.tela3.show()

    def cadastrar_usuario(self):
        nome = self.tela3.lineEdit.text()
        login = self.tela3.lineEdit_2.text()
        senha = self.tela3.lineEdit_3.text()
        rpsenha = self.tela3.lineEdit_4.text()
        
        if senha == rpsenha and any(x.isupper() for x in senha):
            try:
                self.cursor.execute("INSERT INTO cadastro VALUES (?, ?, ?)", (nome, login, senha))
                self.banco.commit()
                self.tela3.label_6.setText("Você foi cadastrado com sucesso")
                self.tela3.close()
                self.tela.show()
            except sqlite3.Error as erro:
                print("Erro ao inserir os dados: ", erro)
        else:
            self.tela3.label_6.setText("As senhas digitadas estão diferentes ou não contém letra maiúscula e minúscula")
            
    def sair(self):
        self.tela2.close()
        
    def executar(self):
        self.tela.show()
        QtWidgets.QApplication.instance().exec_()


if __name__ == '__main__':
    app = AppDeLogin()
    app.executar()
