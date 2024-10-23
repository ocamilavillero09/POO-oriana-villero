from typing import Tuple, List, Dict 

class DatosMeteorologicos:

    def __init__(self, datos: str):
        self.datos = datos
    
    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperatura, humedad, presion, velocidad, direccion = [], [], [], [], []
        
        with open("datos.txt", 'r') as file:
            for linea in file:
                partes = linea.strip().split(',')
                if len(partes) == 6:
                    fecha, temp, hum, press, vel, dir_viento = partes
                    temperatura.append(float(temp))
                    humedad.append(float(hum))
                    presion.append(float(press))
                    velocidad.append(float(vel))
                    direccion.append(dir_viento)
        
        temp_promedio = sum(temperatura) / len(temperatura)
        hum_promedio = sum(humedad) / len(humedad) 
        press_promedio = sum(presion) / len(presion) 
        vel_promedio = sum(velocidad) / len(velocidad) 
        
        print(f"La temperatura promedio: {temp_promedio}")
        print(f"La humedad promedio: {hum_promedio}")
        print(f"La presión promedio: {press_promedio}")
        print(f"La velocidad promedio: {vel_promedio}")
        
        return temp_promedio, hum_promedio, press_promedio, vel_promedio, direccion



        
                    
                
            