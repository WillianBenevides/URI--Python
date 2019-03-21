a , b, c = map(float, input().split())
areatriangulo = (a * c) / 2 
areacirculo = 3.14159 * c**2
areatrapezio = ((a + b) * c) / 2 
areaquadrado = b * b 
arearetangulo = a * b
print("TRIANGULO: %.3f" %areatriangulo)
print("CIRCULO: %.3f" %areacirculo)
print("TRAPEZIO: %.3f" %areatrapezio)
print("QUADRADO: %.3f" %areaquadrado)
print("RETANGULO: %.3f" %arearetangulo)
