import tkinter as tk
import pymssql as sql


conn = sql.connect(server='192.168.40.16\SQLEXPRESS', user= 'giurato.fabrizio', password='xxx123##', database='giurato.fabrizio')
window = Tk()
window.title('Homepage')
window.configure(width=1000, height=800)
nome_i = tk.Entry(window)
cognome_i = tk.Entry(window)
password_i = tk.Entry(window)
nome_mod= tk.Entry(window)
cognome_mod= tk.Entry(window)


def users():

    username_label = tk.Label(root, text="Gestione Utenti:")
    username_label.grid(column=3, row=0, sticky=tk.N, padx=5, pady=5)
    
    frame = ttk.Frame(window)
    frame.columnconfigure(index = 4, weight=1)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM utenteGUI')
    usr = cursor.fetchall

    for i in enumerate(usr):
        utenti = tk.Label(window)
        utenti.grid()
        mod = tk.Button(window)
        mod.grid()
        delu= tk.Button(window)
        delu.grid()
        

    add= tk.Button(window)
    add.grid(column=3, row=0, sticky= tk.NE, padx=5, pady=5)
    

def InsertUsers():
    window2 = Tk()
    window2.title('Inserisci Dati')
    window2.configure(width=1000, height=800)
    
    labl_1 = Label(window2, text="Name",width=20,font=("bold", 10))  
    labl_1.place(x=80,y=130) 
    entry_1 = Entry(window2)  
    entry_1.place(x=240,y=130)    


    labl_2 = Label(window2, text="Surname",width=20,font=("bold", 10))  
    labl_2.place(x=80,y=130)  
    entry_2 = Entry(window2)  
    entry_2.place(x=240,y=130)  

    lb6= Label(window2, text="Enter Password", width=13,font=("arial",12))  
    lb6.place(x=19, y=320)  
    en6= Entry(window2, show='*')  
    en6.place(x=200, y=320)  


    Button(window2, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380) 
    cursor = conn.cursor()
    # inserimento dati nella tabella
    cursor.execute("INSERT INTO utenteGUI(nome, cognome,pswrd) VALUES ('%(nome_i)s', '%(cognome_i)s', '%(password_i)s')")
    conn.commit()

    conn.close()

myButton = Button(window, text="INSERISCI", command=InsertUsers,fg='white', bg='purple')
myButton.pack()
def DeleteUsers():
    cursor = conn.cursor()
    # cancella dati nella tabella
    cursor.execute("DELETE FROM utenteGUI WHERE nome='%(nome_i)s' AND cognome='%(cognome_i)s'")
    conn.commit()

def modUsers():
    cursor = conn.cursor()
    # modifica dati nella tabella
    cursor.execute("UPDATE TABLE utenteGUI SET nome='%(nome_mod)s', cognome='%(cognome_mod)s' WHERE cognome='%(cognome_i)s' AND nome='%(nome_i)s'")
    conn.commit()

def searchUsers():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utenteGUI WHERE nome LIKE '%(nome_i)s%' ANMD cognome LIKE '%(cognome_i)s'")
    conn.commit()



    button = tk.Button(window, text="Inserisci", command=InsertUsers)
    button.pack()

    button1= tk.Button(window, text="Elimina", command=DeleteUsers)
    button1.pack()

    button2= tk.Button(window, text="Modifica", command=modUsers)
    button2.pack()

    button3= tk.Button(window, text="Modifica", command=searchUsers)
    button3.pack()
    # chiusura connessione al database


window.mainloop()
    