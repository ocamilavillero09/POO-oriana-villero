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
    def __init__(self, p1, p2):
        self.p1 = p1  # p1 y p2 son las coordenadas de las esquinas opuestas del rectángulo
        self.p2 = p2

    def calcular_perimetro(self):
        # Calculamos la longitud de los lados
        lado1 = abs(self.p1[0] - self.p2[0])
        lado2 = abs(self.p1[1] - self.p2[1])
        # Calculamos el perímetro
        return 2 * (lado1 + lado2)

    def calcular_area(self):
        # Calculamos la longitud de los lados
        lado1 = abs(self.p1[0] - self.p2[0])
        lado2 = abs(self.p1[1] - self.p2[1])
        # Calculamos el área
        return lado1 * lado2

    def es_cuadrado(self):
        # Un rectángulo es un cuadrado si ambos lados son iguales
        lado1 = abs(self.p1[0] - self.p2[0])
        lado2 = abs(self.p1[1] - self.p2[1])
        return lado1 == lado2

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

#punto 6
    class Carta:
    #se definen las constantes antes que todo
    ROSADO = "Rosado"
    MORADO = "Morado"
    AZUL = "Azul"
    AMARILLO = "Amarillo"
    def __init__(self,valor, pinta):
        self.valor = valor
        if pinta in {Carta.ROSADO, Carta.MORADO, Carta.AZUL, Carta.AMARILLO}:
            self.pinta = pinta

#punto 7
    class CuentaBancaria:
    def __init__(self, ncuenta, propietarios, balance):
        self.ncuenta = ncuenta
        self.propietarios = propietarios
        self.balance = balance

#punto 8   
    def depositar (self, balance, deposito):
        self.balance += deposito
#punto 9
    def retirar (self,balance, retiro):
        if retiro <= self.balance:
            self.balance -= retiro
        else:
            print("Fondos insuficientes")
#punto 10
    def cuota_manejo (self, balance):
        self.balance -= self.balance * 0.02
#punto 11
    def mostar_detalles (ncuenta, propietarios, balance):
        print (ncuenta, propietarios, balance)

        

        
