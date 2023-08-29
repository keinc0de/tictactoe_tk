class Jugada:
    def __init__(self, signo="O"):
        self.signo = signo

    def revisa(self, lista):
        soluciones = ('123', '456', '789', '147', '258','369', '159', '357')
        indices = []
        resultado = False
        for x, e in enumerate(lista):
            if e!='' and e==self.signo:
                indices.append(x+1)
                
        for sol in soluciones:
            contador = 0
            for i in indices:
                if str(i) in sol:
                    contador+=1
                if contador==3:
                    resultado = True
                    break
        return resultado
    
    def grafica(self, lista):
        lista = [e if e!='' else ' ' for e in lista]
        _ = " {0} | {1} | {2} \n"\
            " {3} | {4} | {5} \n"\
            " {6} | {7} | {8} \n"
        return _.format(*lista)