import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
RESET = "\033[0m"

reglas = [
    {"id": "R1", "si": {"espacio": "pequeño", "tiempo": "poco", "preferencia": "peces"}, "entonces": "Pez Betta"},
    {"id": "R2", "si": {"espacio": "pequeño", "presupuesto": "bajo", "preferencia": "peces"}, "entonces": "Pez Betta"},
    {"id": "R3", "si": {"espacio": "mediano", "presupuesto": "medio", "preferencia": "peces"}, "entonces": "Pecera comunitaria"},
    {"id": "R4", "si": {"tiempo": "poco", "presupuesto": "bajo", "preferencia": "mamíferos"}, "entonces": "Hámster"},
    {"id": "R5", "si": {"espacio": "pequeño", "tiempo": "medio", "preferencia": "mamíferos"}, "entonces": "Hámster"},
    {"id": "R6", "si": {"espacio": "mediano", "tiempo": "medio", "preferencia": "mamíferos"}, "entonces": "Conejo"},
    {"id": "R7", "si": {"espacio": "mediano", "tiempo": "mucho", "preferencia": "mamíferos"}, "entonces": "Gato"},
    {"id": "R8", "si": {"espacio": "grande", "actividad": "alta", "preferencia": "mamíferos"}, "entonces": "Perro grande"},
    {"id": "R9", "si": {"espacio": "mediano", "actividad": "media", "preferencia": "mamíferos"}, "entonces": "Perro pequeño"},
    {"id": "R10", "si": {"espacio": "grande", "actividad": "media", "preferencia": "mamíferos"}, "entonces": "Perro mediano"},
    {"id": "R11", "si": {"experiencia": "ninguna", "preferencia": "aves"}, "entonces": "Canario"},
    {"id": "R12", "si": {"experiencia": "algo", "preferencia": "aves"}, "entonces": "Periquito"},
    {"id": "R13", "si": {"experiencia": "mucha", "preferencia": "aves"}, "entonces": "Periquito"},
    {"id": "R14", "si": {"niños": "sí", "preferencia": "mamíferos", "espacio": "grande"}, "entonces": "Perro mediano"},
    {"id": "R15", "si": {"niños": "sí", "preferencia": "mamíferos", "espacio": "mediano"}, "entonces": "Gato"},
    {"id": "R16", "si": {"niños": "no", "espacio": "pequeño", "preferencia": "mamíferos"}, "entonces": "Hámster"},
    {"id": "R17", "si": {"presupuesto": "alto", "tiempo": "mucho", "espacio": "grande"}, "entonces": "Perro grande"},
    {"id": "R18", "si": {"presupuesto": "alto", "preferencia": "peces"}, "entonces": "Pecera comunitaria"},
    {"id": "R19", "si": {"presupuesto": "bajo", "preferencia": "aves"}, "entonces": "Canario"},
    {"id": "R20", "si": {"tiempo": "mucho", "actividad": "alta", "espacio": "grande"}, "entonces": "Perro grande"},
    {"id": "R21", "si": {"experiencia": "ninguna", "preferencia": "peces"}, "entonces": "Pez Betta"},
    {"id": "R22", "si": {"experiencia": "mucha", "tiempo": "mucho", "preferencia": "mamíferos"}, "entonces": "Perro mediano"},
]


def inicializar_historial():
    try:
        with open("historial_mascotas.csv", "x", newline="", encoding="utf-8") as archivo:
            csv.writer(archivo).writerow([
                "Fecha", "Espacio", "Tiempo", "Presupuesto", "Experiencia",
                "Actividad", "Niños", "Preferencia", "Recomendación"
            ])
    except FileExistsError:
        pass


def preguntar(texto, opciones):
    while True:
        print("\n" + texto)
        for clave, valor in opciones.items():
            print(f"{clave}. {valor}")
        respuesta = input("Seleccione una opción: ")
        if respuesta in opciones:
            return opciones[respuesta]
        print(ROJO + "⚠ Opción inválida. Intente nuevamente." + RESET)


def evaluar_reglas(hechos, reglas_disponibles):
    return [
        regla for regla in reglas_disponibles
        if all(hechos.get(clave) == valor for clave, valor in regla["si"].items())
    ]


def explicar_decision(activadas):
    print(AMARILLO + "\n¿Por qué se tomó esta decisión?" + RESET)
    for regla in activadas:
        condiciones = [f"{clave} = {valor}" for clave, valor in regla["si"].items()]
        print(f"- {regla['id']} porque {' y '.join(condiciones)}")


def guardar_historial(hechos, recomendacion):
    with open("historial_mascotas.csv", "a", newline="", encoding="utf-8") as archivo:
        csv.writer(archivo).writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            hechos["espacio"], hechos["tiempo"], hechos["presupuesto"],
            hechos["experiencia"], hechos["actividad"], hechos["niños"],
            hechos["preferencia"], recomendacion,
        ])


def realizar_consulta():
    hechos = {
        "espacio": preguntar("¿Qué tamaño tiene su vivienda?", {"1": "pequeño", "2": "mediano", "3": "grande"}),
        "tiempo": preguntar("¿Cuánto tiempo libre tiene al día?", {"1": "poco", "2": "medio", "3": "mucho"}),
        "presupuesto": preguntar("¿Cuál es su presupuesto mensual para la mascota?", {"1": "bajo", "2": "medio", "3": "alto"}),
        "experiencia": preguntar("¿Qué experiencia tiene cuidando mascotas?", {"1": "ninguna", "2": "algo", "3": "mucha"}),
        "actividad": preguntar("¿Cuál es su nivel de actividad física?", {"1": "baja", "2": "media", "3": "alta"}),
        "niños": preguntar("¿Hay niños pequeños en casa?", {"1": "sí", "2": "no"}),
        "preferencia": preguntar("¿Qué tipo de mascota prefiere?", {"1": "mamíferos", "2": "peces", "3": "aves"}),
    }
    activadas = evaluar_reglas(hechos, reglas)
    if activadas:
        recomendacion = activadas[0]["entonces"]
        print(VERDE + "\n===================================" + RESET)
        print(VERDE + "RECOMENDACIÓN" + RESET)
        print(VERDE + "===================================" + RESET)
        print(VERDE + f"✅ Mascota recomendada: {recomendacion}" + RESET)
        explicar_decision(activadas)
        guardar_historial(hechos, recomendacion)
        print(VERDE + "\n✅ Consulta guardada en historial_mascotas.csv" + RESET)
    else:
        print(ROJO + "\nNo se encontró una recomendación adecuada." + RESET)
        print("Intente con otras opciones.")


def interfaz_grafica():
    ventana = tk.Tk()
    ventana.title("Sistema Experto de Mascotas")
    ventana.geometry("600x400")
    ventana.configure(bg="#EAF6FF")
    tk.Label(ventana, text="Sistema Experto para Elegir una Mascota", bg="#EAF6FF", fg="#003366", font=("Arial", 16, "bold")).pack(pady=20)
    tk.Label(ventana, text="Utilice la consola para responder las preguntas.\nLos resultados se guardarán automáticamente en un archivo CSV.", bg="#EAF6FF", fg="#333333", font=("Arial", 11)).pack(pady=10)

    def mostrar_info():
        mensaje = "Este sistema recomienda mascotas según:\n\n• Espacio disponible\n• Tiempo libre\n• Presupuesto\n• Experiencia\n• Actividad física\n• Presencia de niños\n• Tipo de mascota preferida"
        messagebox.showinfo("Información", mensaje)

    tk.Button(ventana, text="Información del Sistema", command=mostrar_info, bg="#4CAF50", fg="white", width=30, height=2).pack(pady=15)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="#D9534F", fg="white", width=30, height=2).pack(pady=15)
    ventana.mainloop()


def main():
    inicializar_historial()
    print(AZUL + "==========================================" + RESET)
    print(AZUL + " SISTEMA EXPERTO PARA ELEGIR UNA MASCOTA " + RESET)
    print(AZUL + "==========================================" + RESET)
    while True:
        realizar_consulta()
        if input("\n¿Desea realizar otra consulta? (s/n): ").lower() != "s":
            print("\nGracias por utilizar el sistema.")
            break


if __name__ == "__main__":
    main()
