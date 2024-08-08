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
        

        

        
