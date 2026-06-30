# Proyecto Renacer - Primer herramienta útil

vehiculos = [
    {"vin": "VIN001", "patio": "A", "fecha": "2026-06-01"},
    {"vin": "VIN002", "patio": "A", "fecha": "2026-06-01"},
    {"vin": "VIN003", "patio": "B", "fecha": "2026-06-02"},
    {"vin": "VIN002", "patio": "B", "fecha": "2026-06-02"},
    {"vin": "VIN004", "patio": "A", "fecha": "2026-06-03"},
    {"vin": "VIN001", "paito": "C", "fecha": "2026-06-03"}
]
print ("=== ANALISIS DE VEHICULOS ===")

vistos = set()
duplicados = []

for v in vehiculos:
    clave = v["vin"]
    if clave in vistos:
        duplicados.append(v)
    else:
        vistos.add(clave)

print("\nTotal de registros:", len(vehiculos))
print("Duplicados encontrados:", len(duplicados))

print("\n--- DETALLE DE DUPLICADOS---")
for d in duplicados:
    print(d)
    