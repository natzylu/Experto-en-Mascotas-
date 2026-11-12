import unittest
from main import evaluar_reglas, seleccionar_recomendacion


class SistemaExpertoTests(unittest.TestCase):
    def test_peces_no_recomienda_perro(self):
        hechos = {"espacio": "grande", "tiempo": "mucho", "presupuesto": "alto", "experiencia": "mucha", "actividad": "alta", "ninos": "no", "preferencia": "peces"}
        activadas = evaluar_reglas(hechos)
        recomendacion, _ = seleccionar_recomendacion(hechos, activadas)
        self.assertNotIn("Perro", recomendacion)

    def test_respaldo_siempre_entrega_resultado(self):
        hechos = {"espacio": "grande", "tiempo": "poco", "presupuesto": "medio", "experiencia": "algo", "actividad": "baja", "ninos": "no", "preferencia": "mamiferos"}
        recomendacion, reglas = seleccionar_recomendacion(hechos, [])
        self.assertEqual(recomendacion, "Perro mediano")
        self.assertEqual(reglas, [])

    def test_explicacion_solo_usa_reglas_ganadoras(self):
        hechos = {"espacio": "mediano", "tiempo": "mucho", "presupuesto": "medio", "experiencia": "mucha", "actividad": "baja", "ninos": "si", "preferencia": "mamiferos"}
        activadas = evaluar_reglas(hechos)
        recomendacion, ganadoras = seleccionar_recomendacion(hechos, activadas)
        self.assertTrue(all(r["entonces"] == recomendacion for r in ganadoras))


if __name__ == "__main__":
    unittest.main()
