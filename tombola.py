import os
import random
import tkinter as tk
from tkinter import LEFT, messagebox
from tkinter import PhotoImage

# To build the .exe
# python -m pip install pyinstaller
# python -m PyInstaller --clean --onefile --windowed --add-data "icona_consulthink.png:." --add-data "logo_consulthink.png:." .\tombola.py

class Tabellone:
    def __init__(self, master):
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)
        
        # Colorazione del numero estratto sul tabellone 
        self.coloreEstratto = "#c0158a"
        # Colorazione del numero estratto sul tabellone 
        self.coloreBase = "#32327b"
         # Colorazione fon numero
        #self.coloreFont = "#f5f5dc"
        self.icona = PhotoImage(file = resource_path("icona_consulthink.png"))
        self.logo = PhotoImage(file = resource_path("logo_consulthink.png"))

        # Finestra tabellone
        self.master = master
        self.master.title('Tabellone Tombola Consulthink')
        self.master.iconphoto(False, self.icona)
        self.master.bind("<F11>", lambda event: self.master.attributes("-fullscreen", not self.master.attributes("-fullscreen")))
        self.master.bind("<Escape>", lambda event: self.master.attributes("-fullscreen", False)) 
        
        window_width = self.master.winfo_screenwidth()
        window_height = self.master.winfo_screenheight()
        self.master.geometry ("%dx%d"%(window_width,window_height)) # Dimensione automatica della finestra alle dimensioni dello schermo

        # Griglia numeri
        self.button = [] 
        num = 0 
        for i in range(0, 9):
            for j in range(0, 10): 
                num = num + 1
                self.button.append(tk.Button(self.master, text=str(num), bg='#241c23', fg='#f5f5dc', font=("Courier New", 60, "bold"), command = lambda c = num-1: self.man_changeColor(c)))
                self.button[-1].grid(row=i, column=j, sticky="EWNS")
                tk.Grid.rowconfigure(self.master, i, weight = 1)
                tk.Grid.columnconfigure(self.master, j, weight = 1)
        
        # Finestra utilities
        self.utilities = tk.Toplevel(self.master)
        self.utilities.geometry('800x400')
        self.utilities.title("Uilities Tombola Consulthink")
        self.utilities.iconphoto(False, self.icona)
        self.utilities.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.frame = tk.Frame(self.utilities)

        self.consulthink_btn = tk.Button(self.frame, text="", image=self.logo, compound=LEFT, bg = '#f5f5dc', fg='#241c23')
        self.consulthink_btn.grid(pady = 20)

        self.New_btn = tk.Button(self.frame, text="Pulisci Tabellone", font=("Courier New", 34, "bold"), bg = '#f5f5dc', fg='#241c23', command = lambda : self.confirm() )
        self.New_btn.grid(sticky = tk.NW)

        # To Do: estrazione automatica con generazione cartelle tombola
        #self.Estrai_btn = tk.Button(self.frame, text="Estrai Numero", font=("", 30), bg = '#9fc5e8',command = lambda : self.EstraiFair())
        #self.Estrai_btn.grid(pady = 20)

        self.status_label = tk.Label(self.frame, text="", font=("Courier New", 20, "bold"))
        self.status_label.grid(sticky = tk.SW)

        self.frame.pack()
        self.nuovaGiocataFair()

    def confirm(self):
        self.New_btn["state"] = "disabled"
        answer = messagebox.askyesno(
            title='Conferma reset tabellone',
            message='Sicuro di voler pulire il Tabellone?')

        if answer:
            self.nuovaGiocataFair()
            self.New_btn["state"] = "normal"
        else:
            self.New_btn["state"] = "normal"

    # Disabilita il pulsante X della finestra -mostra una finestra di warning.
    def disable_event(self): 
        messagebox.showwarning('Warning', 'Per terminare il programma chiudere la finestra del Tabellone.')
        pass

    # Set numeri estratti
    def nuovaGiocataFair(self):
        print('Nuova estrazione.')
        self.estratti = set() 
        
        for btn_number in range(len(self.button)):
            self.button[btn_number]["bg"] = self.coloreBase 

        self.status_label.config(text = "") 

    def EstraiFair(self):
        attuali = len(self.estratti)
        
        if attuali == 90:
            self.status_label.config(text = "Fine")
            print("Fine")
            return

        numero = random.randrange(90)
        self.estratti.add(numero)

        if len(self.estratti) == attuali: 
            self.EstraiFair() 
        else: 
            print(numero + 1) 
            self.changeColor(numero)  
            self.status_label.config(text = str(numero + 1))
   
    def changeColor(self, btn_number):
        if self.button[btn_number].cget('bg') == self.coloreBase: 
            self.button[btn_number]["bg"] = self.coloreEstratto
        else: 
            self.button[btn_number]["bg"] = self.coloreBase
    
    def man_changeColor(self, btn_number): 
        if self.button[btn_number].cget('bg') == self.coloreBase: 
            self.button[btn_number]["bg"] = self.coloreEstratto
            self.estratti.add(btn_number)
        else: 
            self.button[btn_number]["bg"] = self.coloreBase
            self.estratti.remove(btn_number)

def main(): 
    root = tk.Tk()
    Tabellone(root)
    root.mainloop()

if __name__ == '__main__':
    main()