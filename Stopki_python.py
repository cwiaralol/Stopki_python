import tkinter as tk
from tkinter import * 
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
import unicodedata
import os 

#                     #
# INTERFEJS GRAFICZNY #
#                     #

window = tk.Tk()
window.title('Program do tworzenia stopek')
window.geometry('500x250+50+50')

#informacja po wciśnięciu przycisku 
def buttonCallBack():
    tkMessageBox.showinfo("","Wykonano!")
    createHTML()

#imie input
L1 = tk.Label(window, text="Imię: ")
L1.place(x=45, y=10)
E1 = tk.Entry(window, bd =3)
E1.place(x=50, y=30)
#imie input
L2 = tk.Label(window, text="Nazwisko: ")
L2.place(x=45, y=60)
E2 = tk.Entry(window, bd =3)
E2.place(x=50, y=80)
#wybranie domeny maila np. cinkciarz.pl 
Lb1 = tk.Listbox(window,width=17,height=3,selectmode=SINGLE)
Lb1.place(x=350,y=150)
Lb1.insert(1,"cinkciarz.pl")
Lb1.insert(2,"pl.conotoxia.com")
Lb1.insert(3,"us.conotoxia.com")
#przycisk
button=tk.Button(window,text = "Generuj", command = buttonCallBack).place(x=200, y=200)


#treeview do działów i stanowisk



tree = ttk.Treeview(window,height=5,show="tree")
tree.place(x=250, y=20)

# dodawanie działów

tree.insert('', '0', 'IT Support', text ='IT Support')
tree.insert('', '1', 'i2', text ='Księgowość')
tree.insert('', '2', 'i3', text ='AML')


#dodawanie stanowisk działu IT Support 
tree.insert('IT Support','3', text='Junior IT Specialist')
tree.insert('IT Support','4', text='IT Specialist')
tree.insert('IT Support','5', text='Senior IT Specialist')

#dodawanie stanowisk działu Ksiegowość 



#dodawanie stanowisk działu AML 



# scrollbar dla treeview
scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x=435,y=45)




#                                  #
# PROGRAM DO TWORZENIA PLIKÓW HTML #
#                                  #

def createHTML():
    #GENERACJA MAILA
    imie=E1.get()
    nazwisko=E2.get()
    item_iid=tree.selection()[0] #id stanowiska
    parent_iid=tree.parent(item_iid) #id dzialu 
    dzial=tree.item(parent_iid)['text'] #przypisanie wartosci dzialu do zmiennej
    stanowisko=tree.item(item_iid)['text'] #przypisanie wartosci stanowiska do zmiennej
    tkMessageBox.showinfo("",dzial)
    tkMessageBox.showinfo("",stanowisko)

    emailEND=Lb1.get(ACTIVE)
    email=imie[0].lower() + "." + nazwisko.lower() + "@" + emailEND.lower()
    email=unicodedata.normalize('NFD', email).replace('ł','l').encode('ascii', 'ignore') #usunięcie polskich znaków 
    email=email.decode("utf-8") 
    tkMessageBox.showinfo("",email)

    #koniec generacji maila

    #Wczytanie przykladowej stopki
    # Open a file: file
    file = open('wzor.html',mode='r',encoding='utf-8')
    # read all lines at once
    all_footer_text = file.read()
    # close the file
    file.close()

    #Zamiana danych 
    all_footer_text=all_footer_text.replace('imiex',imie)
    all_footer_text=all_footer_text.replace('nazwiskox',nazwisko)
    all_footer_text=all_footer_text.replace('dzialx',dzial)
    all_footer_text=all_footer_text.replace('stanowiskox',stanowisko)
    all_footer_text=all_footer_text.replace('emailx',email)

    #POBIERZ NAZWĘ DZIAŁU  


    if dzial=='IT Support' :
       dzial_skrot = 'IT'
    if dzial=='Księgowość' :
       dzial_skrot = 'KSG'
    if dzial=='AML' :
       dzial_skrot = 'AML'

    #utworzenie nazwy 
    dzial_skrot=dzial_skrot+'-'+imie[0].upper() + nazwisko[0].upper()+".html" 
    dzial_skrot=unicodedata.normalize('NFD', dzial_skrot).replace('ł','l').encode('ascii', 'ignore')

    f = open(dzial_skrot, "w",encoding='utf-8')
    f.write(all_footer_text)
    f.close()





window.mainloop()


