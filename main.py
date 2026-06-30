import pandas as pd
print("=== ANALISIS DESDE EXCEL ===")

# Leer archivo Excel
df = pd.read_excel("vehiculos.xlsx")

print("\nDatos cargados:")
print(df)

# Detectar duplicados por VIN
duplicados = df[df.duplicated(subset=["VIN"], keep=False)]

print("\n--- DUPLICADOS ---")
print(duplicados)

print("\n Total registros:", len(df))
print("Duplicados encontrados:", len(duplicados))

#### REPORTE DE DUPLICADOS

print("\n=== GENERANDO REPORTE ===")

# Leer archivo
df = pd.read_excel("vehiculos.xlsx")

# Detectar duplicados
duplicados = df[df.duplicated(subset=["VIN"], keep=False)]

# Crear reporte
reporte = pd.DataFrame({
    "Total_registros": [len(df)],
    "Total_duplicados": [len(duplicados)]
})

# Guardar resultados en Excel
with pd.ExcelWriter("reporte_analisis.xlsx") as writer:
    df.to_excel(writer, sheet_name="Datos_originales", index=False)
    duplicados.to_excel(writer, sheet_name="Duplicados", index=False)
    reporte.to_excel(writer, sheet_name="Resumen", index=False)

print("Reporte generado: reporte_analisis.xlsx")