import unittest
from engine import recomendar
class EngineTests(unittest.TestCase):
    def test_preferencia_peces_no_da_perro(self):
        h={"espacio":"Grande","tiempo":"Mucho","presupuesto":"Alto","experiencia":"Mucha","actividad":"Alta","niños":"No","preferencia":"Peces"}
        self.assertNotIn("Perro", recomendar(h)[0])
    def test_respaldo(self):
        h={"espacio":"Grande","tiempo":"Poco","presupuesto":"Medio","experiencia":"Algo","actividad":"Baja","niños":"No","preferencia":"Mamíferos"}
        self.assertEqual(recomendar(h)[0], "Perro mediano")
if __name__ == "__main__": unittest.main()
