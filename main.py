import pandas as pd
import sys
import os

print("=== SISTEMA DE ANALISIS FLEXIBLE ===")

# Pedir archivo si no viene como parámetro
if len(sys.argv) < 2:
    archivo_entrada = input("Escribe la ruta del archivo Excel: ")
else:
    archivo_entrada = sys.argv[1]

if not os.path.exists(archivo_entrada):
    print("El archivo no existe:", archivo_entrada)
    sys.exit()

# Leer Excel
df = pd.read_excel(archivo_entrada)

print("\nArchivo cargado:", archivo_entrada)
print("Total registros:", len(df))

# Detectar duplicados
duplicados = df[df.duplicated(subset=["VIN"], keep=False)]

print("Duplicados encontrados:", len(duplicados))

# Generar salida
archivo_salida = "reporte_" + os.path.basename(archivo_entrada)

with pd.ExcelWriter(archivo_salida) as writer:
    df.to_excel(writer, sheet_name="Datos", index=False)
    duplicados.to_excel(writer, sheet_name="Duplicados", index=False)

print("\nReporte generado:", archivo_salida)