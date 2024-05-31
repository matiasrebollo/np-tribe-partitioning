import unittest
from main import aprox_pakku, backtracking, obtener_suma, parse

class Test(unittest.TestCase):
    def test_drive_5_2(self):
        k, maestros = parse("pruebas_drive/5_2.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        grupos_bt = backtracking(maestros, k)
        self.assertEqual(obtener_suma(grupos_aprox), 1894340)
        self.assertEqual(obtener_suma(grupos_bt), 1894340)
    
    def test_drive_6_3(self):
        k, maestros = parse("pruebas_drive/6_3.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        grupos_bt = backtracking(maestros, k)
        self.assertEqual(obtener_suma(grupos_aprox), 1640690)
        self.assertEqual(obtener_suma(grupos_bt), 1640690)
    
    def test_drive_6_4(self):
        k, maestros = parse("pruebas_drive/6_4.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        grupos_bt = backtracking(maestros, k)
        self.assertEqual(obtener_suma(grupos_aprox), 807418)
        self.assertEqual(obtener_suma(grupos_bt), 807418)
        
    def test_drive_8_3(self):
        k, maestros = parse("pruebas_drive/8_3.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        grupos_bt = backtracking(maestros, k)
        self.assertEqual(obtener_suma(grupos_aprox), 4298131)
        self.assertEqual(obtener_suma(grupos_bt), 4298131)
        
    def test_drive_10_3(self):
        k, maestros = parse("pruebas_drive/10_3.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        grupos_bt = backtracking(maestros, k)
        self.assertEqual(obtener_suma(grupos_aprox), 385249)
        self.assertEqual(obtener_suma(grupos_bt), 385249)
        
    def test_drive_10_5(self):
        k, maestros = parse("pruebas_drive/10_5.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        grupos_bt = backtracking(maestros, k)
        self.assertEqual(obtener_suma(grupos_aprox), 355882)
        self.assertEqual(obtener_suma(grupos_bt), 355882)
        
    def test_drive_10_10(self): # . sec solo, 126.4 sec con todos los anteriores
        k, maestros = parse("pruebas_drive/10_10.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        grupos_bt = backtracking(maestros, k)
        self.assertEqual(obtener_suma(grupos_aprox), 172295)
        self.assertEqual(obtener_suma(grupos_bt), 172295)
        
    def test_drive_11_5(self):
        k, maestros = parse("pruebas_drive/11_5.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        self.assertEqual(obtener_suma(grupos_aprox), 2906564)
        # self.assertEqual(obtener_suma(grupos_bt), 2906564)
        
    def test_drive_14_3(self):
        k, maestros = parse("pruebas_drive/14_3.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 15659106)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 15659106
    
    def test_drive_14_4(self):
        k, maestros = parse("pruebas_drive/14_4.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 15292055)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 15292055)

    def test_drive_14_6(self):
        k, maestros = parse("pruebas_drive/14_6.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 10694510)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 10694510)
        
    def test_drive_15_4(self):
        k, maestros = parse("pruebas_drive/15_4.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 4311889)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 4311889)
        
    def test_drive_15_6(self):
        k, maestros = parse("pruebas_drive/15_6.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 6377225)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 6377225)
        
    def test_drive_17_5(self):
        k, maestros = parse("pruebas_drive/17_5.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 15974095)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 15974095)
    
    def test_drive_17_7(self):
        k, maestros = parse("pruebas_drive/17_7.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        self.assertEqual(obtener_suma(grupos_aprox), 11513230)
        # self.assertEqual(obtener_suma(grupos_bt), 11513230)

    def test_drive_17_10(self):
        k, maestros = parse("pruebas_drive/17_10.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 5427764)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 5427764)

    def test_drive_18_6(self):
        k, maestros = parse("pruebas_drive/18_6.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 10322822)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 10322822)

    def test_drive_18_8(self):
        k, maestros = parse("pruebas_drive/18_8.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 11971097)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 11971097)

    def test_drive_20_4(self):
        k, maestros = parse("pruebas_drive/20_4.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 21081875)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 21081875)

    def test_drive_20_5(self):
        k, maestros = parse("pruebas_drive/20_5.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 16828799)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 16828799)
    
    def test_drive_20_8(self):
        k, maestros = parse("pruebas_drive/20_8.txt")
        grupos_aprox = aprox_pakku(maestros, k)
        # grupos_bt = backtracking(maestros, k)
        # self.assertEqual(obtener_suma(grupos_aprox), 11423730)  # no da la solucion optima
        # self.assertEqual(obtener_suma(grupos_bt), 11423730)

if __name__ == '__main__':
    unittest.main()