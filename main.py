import pandas as pd
import os

def cargar_archivo():
    ruta = input("Ingresa la ruta del archivo Excel: ")

    if not os.path.exists(ruta):
        print("❌ Archivo no encontrado")
        return None, None

    df = pd.read_excel(ruta)
    return df, ruta


def analizar(df):
    print("\n=== ANALISIS ===")
    print("Total registros:", len(df))
    print("Columnas:", list(df.columns))

    duplicados = df[df.duplicated(subset=["VIN"], keep=False)]
    print("Duplicados:", len(duplicados))

    return duplicados


def generar_reporte(df, duplicados, ruta):
    nombre = "reporte_" + os.path.basename(ruta)

    with pd.ExcelWriter(nombre) as writer:
        df.to_excel(writer, sheet_name="Datos", index=False)
        duplicados.to_excel(writer, sheet_name="Duplicados", index=False)

    print("📄 Reporte generado:", nombre)


# MENU PRINCIPAL
while True:
    print("\n=== SISTEMA RENACER ===")
    print("1. Analizar archivo Excel")
    print("2. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        df, ruta = cargar_archivo()

        if df is not None:
            duplicados = analizar(df)
            generar_reporte(df, duplicados, ruta)

    elif opcion == "2":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")