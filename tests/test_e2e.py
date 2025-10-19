import subprocess

def test_app_e2e():
    resultado = subprocess.run(
        ["python", "app.py"],
        capture_output=True,
        text=True
    )
    
    assert "Suma: 5 + 3 = 8" in resultado.stdout
    assert "Dato guardado recuperado: 8" in resultado.stdout
    assert "Flujo de operaciones completado." in resultado.stdout