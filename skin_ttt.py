import tkinter as tk
from player import Player


class SkinTicTacToe(tk.Tk):
    sg = 'O'
    def __init__(self):
        super(SkinTicTacToe, self).__init__()
        self._inicializa()
        
    def _inicializa(self):
        cnf = {'font':('Arial', 26), 'width':1, 'justify':tk.CENTER, 'state':'readonly'}
        self.vars = []
        
        for f in range(3):
            for c in range(3):
                var = tk.StringVar()
                en = tk.Entry(self, textvariable=var, **cnf)
                en.grid(row=f, column=c, sticky='wens')
                self.vars.append({'entry':en, 'var':var})
            self.rowconfigure(f, weight=1)
            self.columnconfigure(f, weight=1)
        
        mts = [
            self.en0, self.en1, self.en2,
            self.en3, self.en4, self.en5,
            self.en6, self.en7, self.en8
        ]
        for x in range(9):
            self.vars[x]['entry'].bind('<Button-1>', mts[x])
            
        # PLAYERS
        self.player1 = Player('O')
        self.player2 = Player('X')

    def en0(self, e):
        self.mt(self.vars[0]['var'])
        
    def en1(self, e):
        self.mt(self.vars[1]['var'])
        
    def en2(self, e):
        self.mt(self.vars[2]['var'])
        
    def en3(self, e):
        self.mt(self.vars[3]['var'])
        
    def en4(self, e):
        self.mt(self.vars[4]['var'])
        
    def en5(self, e):
        self.mt(self.vars[5]['var'])
        
    def en6(self, e):
        self.mt(self.vars[6]['var'])
        
    def en7(self, e):
        self.mt(self.vars[7]['var'])
        
    def en8(self, e):
        self.mt(self.vars[8]['var'])    
        
    def _cambia(self):
        self.sg = 'O' if self.sg=='X' else 'X'
    
    def mt(self, var):
        if var.get()=='':
            var.set(self.sg)
            self._cambia()
            
        li = self.obten_lista()
        res1 = self.player1.revisa(li)
        res2 = self.player2.revisa(li)
        if res1:
            print('1 ganaste')
        if res2:
            print('2 ganaste')
            
    def obten_lista(self):
        return [self.vars[x]['var'].get() for x in range(9)]
             
        
if __name__=="__main__":
    app = SkinTicTacToe()
    app.mainloop()
    