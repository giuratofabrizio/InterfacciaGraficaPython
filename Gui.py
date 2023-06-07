#Gruppo:  Fabrizio Giurato, Gabriel Goycochea, Alessandro Tag


import tkinter as tk
import pymssql as sql

# conn = sql.connect(server='192.168.40.16\SQLEXPRESS', user= 'giurato.fabrizio', password='xxx123##', database='giurato.fabrizio')
window = tk.Tk()
window.title('Homepage')
window.geometry("550x450")
window.resizable(False, False)




def users():
    username_label = tk.Label(root, text="Gestione Utenti:")
    username_label.grid(column=3, row=0, sticky=tk.N, padx=5, pady=5)
    
    frame = tk.Frame(window)
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


def Inserisci():
    global nome_i, cognome_i, password_i

    window2 = tk.Tk()
    window2.title('Inserisci Dati')
    window2.resizable(False, False)
    window2.geometry("800x600")
    
    labl_1 = tk.Label(window2, text="Enter Name",width=20,font=("bold", 10))  
    labl_1.place(x=80,y=130) 
    nome_i = tk.Entry(window2)  
    nome_i.place(x=240,y=130)    


    labl_2 = tk.Label(window2, text="Enter Surname",width=20,font=("bold", 10))  
    labl_2.place(x=80,y=180)  
    cognome_i = tk.Entry(window2)  
    cognome_i.place(x=240,y=180)  

    lb6= tk.Label(window2, text="Enter Password", width=20,font=("bold",10))  
    lb6.place(x=80, y=230)  
    password_i= tk.Entry(window2, show='*')  
    password_i.place(x=240, y=230)  

    tk.Button(window2, text='Submit', command = InsertUsers, width=20,bg='brown',fg='white').place(x=240,y=290) 
    
def Elimina():
    global nome_e, cognome_e

    window2 = tk.Tk()
    window2.title('Elimina Dati')
    window2.resizable(False, False)
    window2.geometry("800x600")
    
    labl_1 = tk.Label(window2, text="Enter Name",width=20,font=("bold", 10))  
    labl_1.place(x=80,y=130) 
    nome_e = tk.Entry(window2)  
    nome_e.place(x=240,y=130)    


    labl_2 = tk.Label(window2, text="Enter Surname",width=20,font=("bold", 10))  
    labl_2.place(x=80,y=180)  
    cognome_e = tk.Entry(window2)  
    cognome_e.place(x=240,y=180)  


    tk.Button(window2, text='Submit', command = DeleteUsers, width=20,bg='brown',fg='white').place(x=240,y=290)

def Modifica():
    global nome_m, cognome_m, password_m, nome_m2, cognome_m2, password_m2

    window2 = tk.Tk()
    window2.title('Modifica Dati')
    window2.resizable(False, False)
    window2.geometry("800x600")
    
    labl_1 = tk.Label(window2, text="Old Name",width=20,font=("bold", 10))  
    labl_1.place(x=80,y=130) 
    nome_m = tk.Entry(window2)  
    nome_m.place(x=240,y=130)

    labl_12 = tk.Label(window2, text="New Name",width=20,font=("bold", 10))  
    labl_12.place(x=380,y=130) 
    nome_m2 = tk.Entry(window2)  
    nome_m2.place(x=530,y=130)    


    labl_2 = tk.Label(window2, text="Old Surname",width=20,font=("bold", 10))  
    labl_2.place(x=80,y=180)  
    cognome_m = tk.Entry(window2)  
    cognome_m.place(x=240,y=180)

    labl_22 = tk.Label(window2, text="New Surname",width=20,font=("bold", 10))  
    labl_22.place(x=380,y=180)  
    cognome_m2 = tk.Entry(window2)  
    cognome_m2.place(x=530,y=180)

    labl_3 = tk.Label(window2, text="Old Password",width=20,font=("bold", 10))  
    labl_3.place(x=80,y=230)  
    password_m = tk.Entry(window2)  
    password_m.place(x=240,y=230)

    labl_32 = tk.Label(window2, text="New Password",width=20,font=("bold", 10))  
    labl_32.place(x=380,y=230)  
    password_m2 = tk.Entry(window2)  
    password_m2.place(x=530,y=230)  


    tk.Button(window2, text='Submit', command = modUsers, width=20,bg='brown',fg='white').place(x=310,y=290)

myButton = tk.Button(window, text="INSERISCI", command=Inserisci, fg='white', bg='purple')
myButton.pack()
myButton.place(x=100, y=100)

myButton2 = tk.Button(window, text="ELIMINA", command=Elimina, fg='white', bg='purple')
myButton2.pack()
myButton2.place(x=350, y=100)

myButton3 = tk.Button(window, text="MODIFICA", command=Modifica, fg='white', bg='purple')
myButton3.pack()
myButton3.place(x=220, y=195)


def InsertUsers():

    cursor = conn.cursor()
    # inserimento dati nella tabella
    cursor.execute("INSERT INTO utenteGUI(nome, cognome, pswrd) VALUES ('%(nome_i)s', '%(cognome_i)s', '%(password_i)s')")
    conn.commit()

    conn.close()


def DeleteUsers():
    cursor = conn.cursor()
    # cancella dati nella tabella
    cursor.execute("DELETE FROM utenteGUI WHERE nome='%(nome_e)s' AND cognome='%(cognome_e)s'")
    conn.commit()

def modUsers():
    cursor = conn.cursor()
    # modifica dati nella tabella
    cursor.execute("UPDATE TABLE utenteGUI SET nome='%(nome_m2)s', cognome='%(cognome_mod2)s', pswrd='%(password_mod2)s' WHERE cognome='%(cognome_m)s' AND nome='%(nome_m)s' AND pswrd='%(password_m)s' ")
    conn.commit()


window.mainloop()
    