import tkinter as tk
from tkinter import messagebox
import pymssql as sql


conn = sql.connect(server='213.140.22.237\SQLEXPRESS', user= 'giurato.fabrizio', password='xxx123##', database='giurato.fabrizio')
window = tk.tk()
nome_i = tk.Entry(window)
cognome_i = tk.Entry(window)
password_i = tk.Entry(window)


def InsertUsers():
    cursor = conn.cursor()
    # inserimento dati nella tabella
    cursor.execute("INSERT INTO utenteGUI VALUES (%(nome_i)s, %(cognome_i)s, %(password_i)s)")
    conn.commit()

    conn.close()

    button = tk.Button(window, text="Submit", command=InsertUsers)
    button.pack()

def DeleteUsers():
    cursor = conn.cursor()
    # inserimento dati nella tabella
    cursor.execute("DELETE FROM utenteGUI WHERE nome=%(nome_i)s AND cognome=%(cognome_i)s")
    conn.commit()

    button = tk.Button(window, text="Inserisci", command=InsertUsers)
    button.pack()

    button1= tk.Button(window, text="Elimina", command=DeleteUsers)
    button1.pack()
    # chiusura connessione al database

    