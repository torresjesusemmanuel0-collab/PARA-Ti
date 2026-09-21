import turtle
import time

def configurar_pantalla():
    pantalla = turtle.Screen()
    pantalla.setup(width=800, height=800)
    pantalla.bgcolor("#111111")
    pantalla.title("Flores Amarillas para Ti 🌻")
    return pantalla

def dibujar_flor(t, x, y, tamano):
    # Tallo
    t.penup()
    t.goto(x, y - tamano * 1.5)
    t.pendown()
    t.color("#2d8a4e")
    t.pensize(5)
    t.setheading(90)
    t.circle(200, 25)
    
    # Hojas del tallo
    t.penup()
    t.goto(x + 5, y - tamano * 0.8)
    t.setheading(30)
    t.pendown()
    t.begin_fill()
    t.circle(30, 90)
    t.left(90)
    t.circle(30, 90)
    t.end_fill()

    # Pétalos
    t.penup()
    t.goto(x, y)
    t.pensize(2)
    t.color("#ffd700", "#ffeb3b") # Amarillo brillante
    
    for _ in range(12):
        t.pendown()
        t.begin_fill()
        t.setheading(t.heading() + 30)
        t.circle(tamano, 60)
        t.left(120)
        t.circle(tamano, 60)
        t.end_fill()

    # Centro de la flor
    t.penup()
    t.goto(x, y - (tamano * 0.3))
    t.setheading(0)
    t.color("#5c3a21", "#8b5a2b") # Café cálido
    t.pendown()
    t.begin_fill()
    t.circle(tamano * 0.3)
    t.end_fill()

def escribir_nota():
    escritor = turtle.Turtle()
    escritor.hideturtle()
    escritor.color("#ffffff")
    escritor.penup()
    escritor.goto(0, -320)
    
    # Mensaje de la nota
    linea1 = "✨ ¡Feliz día de las Flores Amarillas! ✨"
    linea2 = "Tal vez no sea un ramo en físico, pero este fue programado"
    linea3 = "línea por línea especialmente para ti. ❤️"
    
    escritor.goto(0, -290)
    escritor.write(linea1, align="center", font=("Courier", 16, "bold"))
    
    escritor.goto(0, -320)
    escritor.write(linea2, align="center", font=("Courier", 12, "normal"))
    
    escritor.goto(0, -345)
    escritor.write(linea3, align="center", font=("Courier", 12, "italic"))

def main():
    pantalla = configurar_pantalla()
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    # Lazos/Envoltorio del Ramo
    t.penup()
    t.goto(0, -220)
    t.color("#e0a96d", "#c59b27")
    t.pendown()
    t.begin_fill()
    t.goto(-60, -80)
    t.goto(60, -80)
    t.goto(0, -220)
    t.end_fill()

    # Posiciones del ramo (X, Y, Tamaño)
    flores = [
        (0, 80, 45),       # Flor Central Superior
        (-70, 40, 40),     # Izquierda Central
        (70, 40, 40),      # Derecha Central
        (-130, -10, 35),   # Izquierda Abajo
        (130, -10, 35),    # Derecha Abajo
        (-50, 140, 38),    # Arriba Izquierda
        (50, 140, 38)      # Arriba Derecha
    ]

    for x, y, tam in flores:
        dibujar_flor(t, x, y, tam)
        
    escribir_nota()
    pantalla.mainloop()

if __name__ == "__main__":
    main()
