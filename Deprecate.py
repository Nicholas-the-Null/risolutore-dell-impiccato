import os
import tkinter 
from tkinter import messagebox

replace=lambda repleace: mistery.pop(Pattern_found-1) and mistery.insert(Pattern_found-1, inserisci_lettera) #replace letter

#liste
lenna=[]
mistery=[]
database=None

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
            inserisci = [int(x) for x in input("insert letter position if you want a multiple input separete number with space ").split()]
            for x in range(0,len(inserisci)):
                if (int(inserisci[x])>lunghezza) or inserisci[0]<=0 or inserisci is None:
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
        except ValueError:
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
        if len(lenna)<15 and len(lenna)!=0:print("\npossible word ",lenna) #stampa possibilita solo se sono minori di 15
        replace(mistery)


if len(lenna)==0:
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showwarning("errore","sorry the word is not on database")
    root.destroy()
else:
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("errore","the secret word is " + str(lenna[0]))
    root.destroy()

