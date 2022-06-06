#//Crie uma interface para registro de clientes utilizando a biblioteca PySimpleGUI para registrar em um banco de dados sqlite.


import sqlite3
import PySimpleGUI as sg



cnxn = sqlite3.connect('cliente.db')
cursor = cnxn.cursor()
cursor = cnxn.execute("CREATE TABLE IF NOT EXISTS cliente (nome VARCHAR(50), cpf VARCHAR(11), email VARCHAR(50), telefone VARCHAR(11))")
cnxn.commit()




def inserir(nome, cpf, email, telefone):
    cursor = cnxn.execute("INSERT INTO cliente (nome, cpf, email, telefone) VALUES (?, ?, ?, ?)", (nome, cpf, email, telefone))
    cnxn.commit()
    


def consultar():
    
    cursor = cnxn.execute("SELECT * FROM cliente")
    for row in cursor:
        print(row)


def excluir(cpf):
    cursor = cnxn.execute("DELETE FROM cliente WHERE cpf ={0}".format(cpf))
    cnxn.commit()
    


def alterar(nome, cpf, email, telefone):
    
    cursor = cnxn.execute("UPDATE cliente SET nome = ?, cpf = ?, email = ? WHERE telefone = ?", (nome, cpf, email, telefone))
    cnxn.commit()

   

def main():
    layout = [
        [sg.Text('Nome'), sg.InputText(key='nome')],
        [sg.Text('CPF'), sg.InputText(key='cpf')],
        [sg.Text('Email'), sg.InputText(key='email')],
        [sg.Text('Telefone'), sg.InputText(key='telefone')],
        [sg.Button('Inserir'), sg.Button('Consultar'), sg.Button('Excluir pelo CPF'), sg.Button('Alterar')],
        [sg.Output(size=(80, 20))]
    ]
    window = sg.Window('CRUD Cliente', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'Inserir':
            inserir(values['nome'], values['cpf'], values['email'], values['telefone'])
        if event == 'Consultar':
            consultar()
        if event == 'Excluir pelo CPF':
            excluir(values['cpf'])
        if event == 'Alterar':
            alterar(values['nome'], values['cpf'], values['email'], values['telefone'])
    window.close()


if __name__ == '__main__':
    main()
