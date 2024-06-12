from turtle import * # Importa todas las funciones de turtle
import colorsys# Importa el módulo colorsys para manejo de colores

bgcolor('black') # Establece el color de fondo a negro
tracer(2)# Controla la velocidad de animación (actualización cada 2 pasos)
pensize(2)# Establece el grosor del lápiz a 2 píxeles
h = 0 # Inicializa la variable del tono (hue) para los colores

for i in range(250):# Bucle que se ejecuta 250 veces(0-249)
    color = colorsys.hsv_to_rgb(h, 0.9, 1)  # Convierte h a un color RGB
    h += 0.006 # Incrementa el tono para el próximo color
    pencolor(color)# Establece el color del lápiz

    lt(179)# Gira 179 grados a la izquierda
    backward(i * 0.1) # Mueve hacia atrás una distancia proporcional a i
    circle(i * 0.3, 120) # Dibuja un arco de círculo (radio i*0.3, ángulo 120 grados)

    rt(14) # Gira 14 grados a la derecha
    forward(i * 0.1)# Mueve hacia adelante una distancia proporcional a i
    circle(i * 0.3, 120)# Dibuja otro arco de círculo

done()


