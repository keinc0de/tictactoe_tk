import tkinter as tk


class Puntaje(tk.Frame):
    def __init__(self, parent, bg='white'):
        tk.Frame.__init__(self, parent)
        self.bg = bg
        self._widgets_pj()
    
    def _widgets_pj(self):
        self.rowconfigure(0, weight=1, minsize=80)
        self.rowconfigure(1, weight=1, minsize=20)
        self.columnconfigure(0, weight=1)
        # self.rowconfigure(3, weight=8)

        bg = self.bg
        fm0 = tk.Frame(self, bg=bg)
        fm0.grid(row=0, column=0, sticky="wens")
        fm0.rowconfigure((0), weight=1, minsize=20)
        fm0.rowconfigure((1,2), weight=1, minsize=12)
        fm0.rowconfigure((3), weight=1, minsize=20)
        # fm0.columnconfigure((0,1), weight=1)

        # Limpiar
        self.bt_rp = tk.Button(fm0, text='PTS a 0')
        self.bt_rp.grid(row=0, column=0)
        self.bt_limpiar = tk.Button(fm0, text='LIMPIAR')
        self.bt_limpiar.grid(row=0, column=1)

        fo0 = ('consolas', 8)
        lb_ptj = tk.Label(fm0, text="PUNTAJE", font=fo0, fg="gray60", bg=bg)
        lb_ptj.grid(row=1, column=0, sticky='we', columnspan=2)
        lb_p1 = tk.Label(fm0, text="PLAYER O", font=fo0, bg=bg)
        lb_p1.grid(row=2, column=0)
        lb_p2 = tk.Label(fm0, text="PLAYER X", font=fo0, bg=bg)
        lb_p2.grid(row=2, column=1)

        fop = ("Segoe UI", 18)
        self.lb_puntaje_1 = tk.Label(fm0, font=fop, bg=bg)
        self.lb_puntaje_1.grid(row=3, column=0)
        self.lb_puntaje_2 = tk.Label(fm0, font=fop, bg=bg)
        self.lb_puntaje_2.grid(row=3, column=1)
        self.reinicia_puntajes()

        fm = tk.Frame(self, bg=self.bg)
        fm.rowconfigure(0, weight=1)
        fm.grid(row=1, column=0, sticky='wens', pady=0)
        fo2 = ('consolas', 8)
        # e_ = {'family': 'Segoe UI', 'size': 9, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
        self.wtexto = tk.Text(fm, font=fo2, relief='flat', bg=bg)
        self.wtexto.grid(row=0, column=0, sticky='ns')
        # self.wtexto.pack(side='left', fill='both', expand=1)
        scroll = tk.Scrollbar(fm, orient='vertical', command=self.wtexto.yview)
        self.wtexto.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns")
        # scroll.pack(side='left', fill='y')
        self.wtexto.config(width=16)


    def asigna_puntaje_1(self, num=0):
        self.lb_puntaje_1.config(text=str(num))

    def asigna_puntaje_2(self, num=0):
        self.lb_puntaje_2.config(text=str(num))

    def reinicia_puntajes(self):
        self.asigna_puntaje_1()
        self.asigna_puntaje_2()

    def inserta_texto(self, texto):
        self.wtexto.insert(tk.END, texto)
        self.wtexto.see(tk.END)


class Principal(tk.Tk):
    def __init__(self, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.geometry("400x100")

        self.rowconfigure((0), weight=1)
        self.columnconfigure((0), weight=1)
        pj = Puntaje(self)
        pj.grid(row=0, column=0, sticky='wens')


if __name__=="__main__":
    app = Principal()
    app.mainloop()