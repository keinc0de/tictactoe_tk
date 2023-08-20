class Player:
    def __init__(self, v='O'):
        self.v = v
    
    def revisa(self, lista):
        soluciones = ('123', '456', '789', '147', '258','369', '159', '357')
        indices = []
        resultado = False
        for x, e in enumerate(lista):
            if e!='' and e==self.v:
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