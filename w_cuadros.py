import tkinter as tk
from jugada import Jugada

class Cuadros(tk.Frame):
    SIGNO = "O"
    def __init__(self, parent, bg="white"):
        tk.Frame.__init__(self, parent)
        self.bg = bg
        self._widgets_cuadros()

    def _widgets_cuadros(self):
        cnf = {
            'font':('Arial', 26), 'width':1,
            'justify':tk.CENTER,
            'state':'readonly',
            # 'bg':self.bg,
            'readonlybackground':self.bg,
            'relief':tk.SUNKEN
        }
        self.VARS = []

        for f in range(3):
            for c in range(3):
                var = tk.StringVar()
                en = tk.Entry(self, textvariable=var, **cnf)
                en.grid(row=f, column=c, sticky="wens")
                self.VARS.append({'entry':en, 'var':var})
            self.rowconfigure(f, weight=1)
            self.columnconfigure(f, weight=1)

        self.player1 = Jugada('O')
        self.player2 = Jugada('X')

        mts = [
            self.en0, self.en1, self.en2,
            self.en3, self.en4, self.en5,
            self.en6, self.en7, self.en8
        ]
        for x in range(9):
            self.VARS[x]['entry'].bind('<Button-1>', mts[x])

        self.RES1 = False
        self.RES2 = False
        self._cambia_cursor("circle")

    def mt(self, var):
        if var.get()=='':
            var.set(self.SIGNO)
            self._cambia()
            
        li = self.obten_lista()
        self.RES1 = self.player1.revisa(li)
        self.RES2 = self.player2.revisa(li)

    def _cambia(self):
        if self.SIGNO=="X":
            self.SIGNO = 'O'
            self._cambia_cursor("circle")
        else:
            self.SIGNO = 'X'
            self._cambia_cursor("X_cursor")

    def _cambia_cursor(self, sg):
        for x in range(9):
            self.VARS[x]['entry'].config(cursor=sg)

    def obten_lista(self):
        return [self.VARS[x]['var'].get() for x in range(9)]
    
    def limpia_lista(self):
        for d in self.VARS:
            d['var'].set('')

    def en0(self, e):
        self.mt(self.VARS[0]['var'])
        
    def en1(self, e):
        self.mt(self.VARS[1]['var'])
        
    def en2(self, e):
        self.mt(self.VARS[2]['var'])
        
    def en3(self, e):
        self.mt(self.VARS[3]['var'])
        
    def en4(self, e):
        self.mt(self.VARS[4]['var'])
        
    def en5(self, e):
        self.mt(self.VARS[5]['var'])
        
    def en6(self, e):
        self.mt(self.VARS[6]['var'])
        
    def en7(self, e):
        self.mt(self.VARS[7]['var'])
        
    def en8(self, e):
        self.mt(self.VARS[8]['var']) 