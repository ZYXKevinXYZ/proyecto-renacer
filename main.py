# Proyecto Renacer - Primer herramienta útil

vehiculos = [
    "VIN001",
    "VIN002",
    "VIN003",
    "VIN002",
    "VIN004",
    "VIN001"
]
print ("=== ANALISIS DE VEHICULOS ===")

vistos=[]
duplicados=[]

for vin in vehiculos:
    if vin in vistos:
        duplicados.append(vin)
    else:
        vistos.append(vin)

print("\nVehículos procesados:", len(vehiculos))
print("Duplicados encontrados:", len(duplicados))
print("Lista de diplicados:", duplicados)
    