"""Sistema experto para recomendar una mascota.

Diseñado para ejecutarse en consola, incluida la terminal de GitHub Codespaces.
"""

from collections import Counter
from datetime import datetime
import csv
from pathlib import Path

from knowledge_base import REGLAS, RECOMENDACIONES_RESPALDO

HISTORIAL = Path("historial_mascotas.csv")
CAMPOS = ("espacio", "tiempo", "presupuesto", "experiencia", "actividad", "ninos", "preferencia")

PREGUNTAS = {
    "espacio": ("¿Qué tamaño tiene su vivienda?", {"1": "pequeno", "2": "mediano", "3": "grande"}),
    "tiempo": ("¿Cuánto tiempo libre tiene al día?", {"1": "poco", "2": "medio", "3": "mucho"}),
    "presupuesto": ("¿Cuál es su presupuesto mensual para la mascota?", {"1": "bajo", "2": "medio", "3": "alto"}),
    "experiencia": ("¿Qué experiencia tiene cuidando mascotas?", {"1": "ninguna", "2": "algo", "3": "mucha"}),
    "actividad": ("¿Cuál es su nivel de actividad física?", {"1": "baja", "2": "media", "3": "alta"}),
    "ninos": ("¿Hay niños pequeños en casa?", {"1": "si", "2": "no"}),
    "preferencia": ("¿Qué tipo de mascota prefiere?", {"1": "mamiferos", "2": "peces", "3": "aves"}),
}


def inicializar_historial(ruta=HISTORIAL):
    """Crea el CSV con encabezados si todavía no existe."""
    if ruta.exists():
        return
    try:
        with ruta.open("w", newline="", encoding="utf-8") as archivo:
            csv.writer(archivo).writerow(["fecha", *CAMPOS, "recomendacion", "reglas"])
    except OSError as error:
        print(f"Aviso: no se pudo crear el historial: {error}")


def preguntar(texto, opciones):
    while True:
        print(f"\n{texto}")
        for clave, valor in opciones.items():
            print(f"  {clave}. {valor.capitalize()}")
        respuesta = input("Seleccione una opción: ").strip()
        if respuesta in opciones:
            return opciones[respuesta]
        print("Opción inválida. Escriba uno de los números mostrados.")


def obtener_hechos():
    return {campo: preguntar(*PREGUNTAS[campo]) for campo in CAMPOS}


def evaluar_reglas(hechos, reglas=REGLAS):
    """Devuelve todas las reglas cuyas condiciones coinciden con los hechos."""
    return [
        regla for regla in reglas
        if all(hechos.get(campo) == valor for campo, valor in regla["si"].items())
    ]


def seleccionar_recomendacion(hechos, reglas_activadas):
    """Resuelve conflictos por votos, especificidad y prioridad.

    1. Gana la recomendación respaldada por más reglas.
    2. En empate, gana la de mayor especificidad total.
    3. Si continúa el empate, gana la de mayor prioridad total.
    4. Si no hay reglas, usa un respaldo compatible con la preferencia y el espacio.
    """
    if not reglas_activadas:
        clave = (hechos["preferencia"], hechos["espacio"])
        recomendacion = RECOMENDACIONES_RESPALDO.get(
            clave, RECOMENDACIONES_RESPALDO[(hechos["preferencia"], "cualquiera")]
        )
        return recomendacion, []

    candidatos = {}
    for regla in reglas_activadas:
        resultado = regla["entonces"]
        datos = candidatos.setdefault(resultado, {"votos": 0, "especificidad": 0, "prioridad": 0})
        datos["votos"] += 1
        datos["especificidad"] += len(regla["si"])
        datos["prioridad"] += regla.get("prioridad", 0)

    ganador = max(
        candidatos,
        key=lambda nombre: (
            candidatos[nombre]["votos"],
            candidatos[nombre]["especificidad"],
            candidatos[nombre]["prioridad"],
            nombre,
        ),
    )
    reglas_ganadoras = [r for r in reglas_activadas if r["entonces"] == ganador]
    return ganador, reglas_ganadoras


def explicar_decision(recomendacion, reglas_ganadoras):
    print("\n¿Por qué se recomienda esta mascota?")
    if not reglas_ganadoras:
        print("- Se utilizó una recomendación general compatible con su preferencia y espacio.")
        return
    for regla in reglas_ganadoras:
        condiciones = ", ".join(f"{campo}={valor}" for campo, valor in regla["si"].items())
        print(f"- {regla['id']}: {condiciones}.")


def guardar_historial(hechos, recomendacion, reglas_ganadoras, ruta=HISTORIAL):
    try:
        with ruta.open("a", newline="", encoding="utf-8") as archivo:
            csv.writer(archivo).writerow([
                datetime.now().isoformat(timespec="seconds"),
                *(hechos[campo] for campo in CAMPOS),
                recomendacion,
                ",".join(regla["id"] for regla in reglas_ganadoras) or "RESPALDO",
            ])
        return True
    except (PermissionError, OSError) as error:
        print(f"Aviso: no se pudo guardar el historial: {error}")
        return False


def realizar_consulta():
    hechos = obtener_hechos()
    activadas = evaluar_reglas(hechos)
    recomendacion, ganadoras = seleccionar_recomendacion(hechos, activadas)

    print("\n" + "=" * 48)
    print(f"RECOMENDACIÓN: {recomendacion}")
    print("=" * 48)
    explicar_decision(recomendacion, ganadoras)

    if guardar_historial(hechos, recomendacion, ganadoras):
        print("\nConsulta guardada en historial_mascotas.csv.")


def main():
    inicializar_historial()
    print("=" * 48)
    print("SISTEMA EXPERTO PARA ELEGIR UNA MASCOTA")
    print("=" * 48)
    while True:
        realizar_consulta()
        continuar = input("\n¿Desea realizar otra consulta? (s/n): ").strip().lower()
        if continuar not in {"s", "si", "sí"}:
            print("Gracias por utilizar el sistema.")
            break


if __name__ == "__main__":
    main()
