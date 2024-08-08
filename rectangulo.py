class Rectangulo:
    def __init__(self,p1,p2,pmt,area):
        self.p1 = p1
        self.p2 = p2
        self.pmt = pmt
        self.area = area
    
    def calcular_perimetro(self,p1,p2):
        self.pmt= 2*(p1+p2)
    
    #def calcular_area(self,p1,p2):
        #self.area=  