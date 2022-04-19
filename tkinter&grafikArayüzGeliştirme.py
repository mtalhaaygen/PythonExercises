import tkinter as tk
pencere = tk.Tk()
def cıkıs():
    etiket['text'] ="elveda zalım dünya"
    dügme["text"] = "Bekleyin..."
    dügme["state"] = "disable"
    pencere.after(2000,pencere.destroy())
pencere.geometry('300x300')
etiket = tk.Label(text = "Merhaba zalimm dünya")
etiket.pack()
dügme = tk.Button(text = "ÇIK",command=cıkıs)
dügme.pack()
pencere.protocol('WM_DELETE_WINDOW',cıkıs)
pencere.mainloop()
