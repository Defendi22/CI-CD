# tests.py - Prova que funciona
from app import somar

def test_somar():
    assert somar(2, 3) == 5
    assert somar(0, 0) == 0
    print("✅ Testes passaram!")

if __name__ == "__main__":
    test_somar()
