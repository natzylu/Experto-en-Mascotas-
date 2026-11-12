"""
Natalia Quesada
11/12/2026
Sistema experto para recomendar una mascota.
"""

from engine import recomendar


def solicitar_opcion(pregunta, opciones):
    while True:
        print(f"\n{pregunta}")

        for numero, opcion in enumerate(opciones, start=1):
            print(f"{numero}. {opcion}")

        respuesta = input("Seleccione una opción: ").strip()

        if respuesta.isdigit():
            indice = int(respuesta) - 1

            if 0 <= indice < len(opciones):
                return opciones[indice]

        print("Opción inválida. Intente nuevamente.")


def realizar_consulta():
    hechos = {
        "espacio": solicitar_opcion(
            "Tamaño de la vivienda:",
            ["Pequeño", "Mediano", "Grande"],
        ),
        "tiempo": solicitar_opcion(
            "Tiempo libre diario:",
            ["Poco", "Medio", "Mucho"],
        ),
        "presupuesto": solicitar_opcion(
            "Presupuesto mensual:",
            ["Bajo", "Medio", "Alto"],
        ),
        "experiencia": solicitar_opcion(
            "Experiencia con mascotas:",
            ["Ninguna", "Algo", "Mucha"],
        ),
        "actividad": solicitar_opcion(
            "Nivel de actividad física:",
            ["Baja", "Media", "Alta"],
        ),
        "niños": solicitar_opcion(
            "¿Hay niños pequeños en casa?",
            ["No", "Sí"],
        ),
        "preferencia": solicitar_opcion(
            "Tipo de mascota preferida:",
            ["Mamíferos", "Peces", "Aves"],
        ),
    }

    recomendacion, reglas = recomendar(hechos)

    print("\n" + "=" * 45)
    print(f"Recomendación: {recomendacion}")
    print("=" * 45)

    if reglas:
        print("\nReglas que respaldan el resultado:")

        for regla in reglas:
            condiciones = ", ".join(
                f"{campo}: {valor}"
                for campo, valor in regla["si"].items()
            )
            print(f"- {regla['id']}: {condiciones}")
    else:
        print(
            "\nSe aplicó una recomendación general según "
            "la preferencia y el espacio disponible."
        )


def main():
    print("=" * 45)
    print("SISTEMA EXPERTO PARA ELEGIR UNA MASCOTA")
    print("=" * 45)

    while True:
        realizar_consulta()

        continuar = input(
            "\n¿Desea realizar otra consulta? (s/n): "
        ).strip().lower()

        if continuar not in {"s", "sí", "si"}:
            print("Gracias por utilizar el sistema.")
            break


if __name__ == "__main__":
    main()
