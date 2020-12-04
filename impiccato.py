import os
import tkinter 
from tkinter import messagebox
from colorama import init
from termcolor import colored


init()

def Impiccato():
    replace=lambda repleace: mistery.pop(Pattern_found-1) and mistery.insert(Pattern_found-1, inserisci_lettera) #replace letter

    print("premi ctrl+c in qualsiasi momento per uscire")
    #liste
    lenna=[]
    mistery=[]
    database=None
    uscire=False

    while True:
        database=input("insert file name ").replace("\\","\\\\")
        if os.path.exists(database) is False:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("errore","file non dont found")
            root.destroy()
        else:
            break



    while True:
        try:
            lunghezza=int(input("insert word length "))
            if lunghezza>1:
                break
        except ValueError:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("errore","file non dont found")
            root.destroy()




    a_file = open(database)
    lines = a_file.readlines()
    print("welcome to Hagman resolutor \n\nscan " +str(len(lines))+" words")
    for line in lines:
        line=line.strip("\n")
        if len(line) ==lunghezza:
            lenna.append(line)

    print("we found " +str(len(lenna)) + " word match length")

    for x in range(lunghezza):
        mistery.append("_") #gui per vedere le lettere


    

    while len(lenna)!=1 and len(lenna)!=0:
        elimina=[]
        while True:
            print("your word:  ",mistery)
            try:
                check2="consenti"
                check=False
                inserisci = [int(x) for x in input("insert letter position if you want a multiple input separete number with space 0 for print word -1 for delete letter  ").split()]
                for x in range(0,len(inserisci)):
                    if (int(inserisci[x])>lunghezza) or inserisci[x]<=0 or inserisci is None:
                        if inserisci[0] == 0:
                            print(colored(lenna,'green'))
                            check=False
                            check2="negato"
                            break
                        
                        
                        if inserisci[0]==-1:
                            scelta=input("voi eliminare per lettera=1 o per più lettere=2 ")
                            
                            if scelta=="2":
                                while True:
                                    try:
                                        numero=int(input("dammi il numero di posizione/lettere si parte dal finale (ovvero se si digita 3) si verrano considerate le 3 ultime lettere "))
                                        if numero>0:
                                            numero*=-1
                                            break
                                        elif numero<0:
                                            break
                                        else:
                                            pass
                                    except:
                                        root = tkinter.Tk()
                                        root.withdraw()
                                        messagebox.showerror("errore","you insert a string ")
                                        root.destroy()
                                while True:
                                    stringa=input("dammi le lettere da eliminare ")
                                    if len(stringa)==numero*-1:
                                        break
                                for x in lenna:
                                    if x[numero:]==stringa:
                                        elimina.append(x)
                                        
                                elimina=list(dict.fromkeys(elimina))
                                if len(elimina)!=0:
                                    for x in elimina:
                                        lenna.remove(x)
                                check=False
                                check2="negato"
                                elimina=[]
                                
                            elif scelta=="1":
                                inserisci_lettera=input("letter to delete ")
                                for x in lenna:
                                    for i in x:
                                        if i==inserisci_lettera:
                                            elimina.append(x)
                                elimina=list(dict.fromkeys(elimina))
                                if len(elimina)!=0:
                                    for x in elimina:
                                        lenna.remove(x)
                            check=False
                            check2="negato"
                            elimina=[]
                                    
                            if len(lenna)<15 and len(lenna)!=0:
                                print(colored("\npossible word "+str(lenna),'green'))
                            break
                            
                        
                        else:
                            root = tkinter.Tk()
                            root.withdraw()
                            messagebox.showwarning("info","number not valid")
                            root.destroy()
                            check=False
                            check2="negato"
                            break
                    else:
                        check=True
                if check is True and check2 == "consenti":
                    break
            except ValueError as e:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("errore","you insert a string")
                root.destroy()
                

        
        
        inserisci_lettera=input("letter ")

        for x in lenna:
            for i in inserisci:
                if x[i-1]!=inserisci_lettera:
                    elimina.append(x)
                    
        elimina=list(dict.fromkeys(elimina))

        
        for x in elimina:
            lenna.remove(x)
            
        for Pattern_found in inserisci:
            replace(mistery)



        sicuro=input("vuoi eliminare anche tutte le parole che hanno la lettera inserita anche in parte diversi ad esempio se la parola segreta è ciao "+
                     " e come posizione della i hai scelto solo 2 questa funzione eliminera parole come civi che anche avendo la i alla posizione 2 ne ha una alla fine "+
                     " digitare si per cancellare ")
        if sicuro=="si":
            const=mistery.count(inserisci_lettera)
            elimina=[]
            for x in lenna:
                if x.count(inserisci_lettera)!=const:
                    elimina.append(x)
            for x in elimina:
                lenna.remove(x)
                
        if len(lenna)<15 and len(lenna)!=0:print(colored("\npossible word "+str(lenna),'green'))
        print("still remain " + str(len(lenna)) + " word")
        


    if len(lenna)==0:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showwarning("errore","sorry the word is not on database")
        root.destroy()
    else:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("find","the secret word is " + str(lenna[0]))
        root.destroy()


while True:
    try:
        Impiccato()
    except KeyboardInterrupt:
        pass
    x=input("digita esci per smettere di usare il programma")
    if x=="esci":
        exit()
    os.system("cls")
