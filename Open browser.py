import webbrowser
from tkinter import *

raiz = Tk( )

raiz.title('Abrir browser')
raiz.geometry('400x200')

def google():
    webbrowser.open('google.com')
mygoogle = Button(raiz, text = 'Abrir o google', command = google).pack(pady = 20)

raiz.mainloop()
