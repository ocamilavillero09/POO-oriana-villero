import math
class Circulo:
    def __inint__(self, centro, radio,area, perimetro):
        self_centro = centro 
        self_radio = radio
        self_area = area
        self_perimetro = perimetro
        
    def area (self, radio):
        self_area = math.pi * radio ** 2
    
    def perimetro (self, radio):
        self_perimetro = 2*math.pi*radio   
        
    