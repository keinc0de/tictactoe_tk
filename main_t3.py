import tkinter as tk
from w_pts import Puntaje
from w_cuadros import Cuadros


class NueveCuadros(Cuadros):
    def __init__(self, parent):
        super(NueveCuadros, self).__init__(parent)
        self._widgets_nc()

    def _widgets_nc(self):
        self.pj = Puntaje(self)
        self.pj.grid(row=0, column=4, rowspan=3)
        self.PUNTAJE_1 = 0
        self.PUNTAJE_2 = 0

        # borrar cuadros
        self.pj.bt_limpiar.config(command=self.limpia_lista)
        self.pj.bt_rp.config(command=self.reinicia_puntaje)

    def mt(self, var):
        super().mt(var)
        if self.RES1:
            self.pj.inserta_texto('GANASTE O\n')
            self.PUNTAJE_1 += 1
            self.pj.asigna_puntaje_1(self.PUNTAJE_1)
        if self.RES2:
            self.pj.inserta_texto('GANASTE X\n')
            self.PUNTAJE_2 += 1
            self.pj.asigna_puntaje_2(self.PUNTAJE_2)
        self.grafica_jugada()
        # self.after(3000, self.grafica_jugada)

    def reinicia_puntaje(self):
        self.limpia_lista()
        self.pj.reinicia_puntajes()

    def grafica_jugada(self):
        li = self.obten_lista()
        if self.RES1 or self.RES2:
            res = self.player1.grafica(li)
            self.pj.inserta_texto(f"{res}\n")
            self.limpia_lista()
            self.RES1 = False
            self.RES2 = False
        # if self.RES2:
        #     res = self.player2.grafica(li)
        #     self.pj.inserta_texto(f"{res}\n")

        
        


class Principal(tk.Tk):
    def __init__(self, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.geometry("290x170")
        self._widgets_inicia()

    def _widgets_inicia(self):
        self.rowconfigure((0), weight=1)
        self.columnconfigure(0, weight=2)
        # self.columnconfigure(1, weight=1)

        # self.c9 = Cuadros(self)
        # self.c9.grid(row=0, column=0, sticky='wens')

        self.nc = NueveCuadros(self)
        self.nc.grid(row=0, column=0, sticky='wens')
        # pj = Puntaje(self)
        # pj.grid(row=0, column=1, sticky='wens')


if __name__=="__main__":
    app = Principal()
    app.mainloop()