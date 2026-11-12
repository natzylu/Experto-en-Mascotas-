"""Base de conocimiento del sistema experto.

Todas las reglas que recomiendan perros o gatos exigen preferencia por mamíferos,
lo que evita resultados incompatibles con una preferencia por peces o aves.
"""

REGLAS = [
    {"id": "R01", "si": {"preferencia": "peces", "espacio": "pequeno", "tiempo": "poco"}, "entonces": "Pez Betta", "prioridad": 3},
    {"id": "R02", "si": {"preferencia": "peces", "presupuesto": "bajo"}, "entonces": "Pez Betta", "prioridad": 2},
    {"id": "R03", "si": {"preferencia": "peces", "experiencia": "ninguna"}, "entonces": "Pez Betta", "prioridad": 2},
    {"id": "R04", "si": {"preferencia": "peces", "espacio": "mediano", "presupuesto": "medio"}, "entonces": "Pecera comunitaria", "prioridad": 3},
    {"id": "R05", "si": {"preferencia": "peces", "espacio": "grande", "presupuesto": "alto"}, "entonces": "Pecera comunitaria", "prioridad": 3},

    {"id": "R06", "si": {"preferencia": "aves", "experiencia": "ninguna"}, "entonces": "Canario", "prioridad": 3},
    {"id": "R07", "si": {"preferencia": "aves", "presupuesto": "bajo"}, "entonces": "Canario", "prioridad": 2},
    {"id": "R08", "si": {"preferencia": "aves", "experiencia": "algo", "tiempo": "medio"}, "entonces": "Periquito", "prioridad": 3},
    {"id": "R09", "si": {"preferencia": "aves", "experiencia": "mucha", "tiempo": "mucho"}, "entonces": "Periquito", "prioridad": 3},

    {"id": "R10", "si": {"preferencia": "mamiferos", "espacio": "pequeno", "tiempo": "poco"}, "entonces": "Hámster", "prioridad": 3},
    {"id": "R11", "si": {"preferencia": "mamiferos", "espacio": "pequeno", "presupuesto": "bajo"}, "entonces": "Hámster", "prioridad": 3},
    {"id": "R12", "si": {"preferencia": "mamiferos", "espacio": "mediano", "actividad": "baja"}, "entonces": "Gato", "prioridad": 3},
    {"id": "R13", "si": {"preferencia": "mamiferos", "espacio": "mediano", "tiempo": "mucho"}, "entonces": "Gato", "prioridad": 2},
    {"id": "R14", "si": {"preferencia": "mamiferos", "espacio": "mediano", "actividad": "media"}, "entonces": "Perro pequeño", "prioridad": 3},
    {"id": "R15", "si": {"preferencia": "mamiferos", "espacio": "grande", "actividad": "media"}, "entonces": "Perro mediano", "prioridad": 3},
    {"id": "R16", "si": {"preferencia": "mamiferos", "espacio": "grande", "actividad": "alta", "tiempo": "mucho"}, "entonces": "Perro grande", "prioridad": 4},
    {"id": "R17", "si": {"preferencia": "mamiferos", "espacio": "grande", "presupuesto": "alto", "experiencia": "mucha"}, "entonces": "Perro grande", "prioridad": 4},
    {"id": "R18", "si": {"preferencia": "mamiferos", "ninos": "si", "espacio": "grande"}, "entonces": "Perro mediano", "prioridad": 3},
    {"id": "R19", "si": {"preferencia": "mamiferos", "ninos": "si", "espacio": "mediano", "actividad": "baja"}, "entonces": "Gato", "prioridad": 3},
    {"id": "R20", "si": {"preferencia": "mamiferos", "espacio": "mediano", "tiempo": "medio", "actividad": "baja"}, "entonces": "Conejo", "prioridad": 3},
]

RECOMENDACIONES_RESPALDO = {
    ("peces", "pequeno"): "Pez Betta",
    ("peces", "mediano"): "Pecera comunitaria",
    ("peces", "grande"): "Pecera comunitaria",
    ("peces", "cualquiera"): "Pez Betta",
    ("aves", "pequeno"): "Canario",
    ("aves", "mediano"): "Periquito",
    ("aves", "grande"): "Periquito",
    ("aves", "cualquiera"): "Canario",
    ("mamiferos", "pequeno"): "Hámster",
    ("mamiferos", "mediano"): "Gato",
    ("mamiferos", "grande"): "Perro mediano",
    ("mamiferos", "cualquiera"): "Gato",
}
