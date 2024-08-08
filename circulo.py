import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro 
        self.radio = radio
    
    def area(self,radio):
        self.area = math.pi * self.radio ** 2
    
    def perimetro(self,radio):
        self.perimetro =  2 * math.pi * self.radio   
    
    def punto_pertenece(self, punto):
        distancia_al_centro = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia_al_centro <= self.radio

        
    
