from knowledge_base import REGLAS, RESPALDO

def evaluar_reglas(hechos):
    return [r for r in REGLAS if all(hechos.get(k) == v for k, v in r["si"].items())]

def recomendar(hechos):
    activadas = evaluar_reglas(hechos)
    if not activadas:
        return RESPALDO[(hechos["preferencia"], hechos["espacio"])], []
    candidatos = {}
    for r in activadas:
        d = candidatos.setdefault(r["entonces"], [0, 0, 0])
        d[0] += 1
        d[1] += len(r["si"])
        d[2] += r.get("prioridad", 0)
    ganador = max(candidatos, key=lambda n: (*candidatos[n], n))
    return ganador, [r for r in activadas if r["entonces"] == ganador]
