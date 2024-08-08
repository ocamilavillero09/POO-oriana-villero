#punto 1
class Vehiculo:
    def __init__(self, velocidadmax, kilometraje):
        self.velocidadmax = velocidadmax
        self.kilometraje = kilometraje
#Aqui verificamos que la clase creada esta correcta     
#vehiculo = Vehiculo(100, 10000)            
#print(vehiculo.kilometraje)

#punto2
import math
class Punto:
    def __init__(self,x,y,distancia):
        self.x = x
        self.y = y
        self.distancia= distancia

#punto 3
    def mostar(self,x,y):
        print (x,y)
        
    def mover(self,nueva_x,nueva_y):
        self.x = nueva_x
        self.y = nueva_y
        
    def calcular_distancia(self,nueva_x,nueva_y,z,p):
        self.distancia = math.sqrt((nueva_x-nueva_y)**2+(z-p)**2)


#punto 4
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

#punto 5
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
        

        

        
