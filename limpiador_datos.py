import os
import csv

def crear_archivo_sucio():
    """Crea un archivo CSV de prueba con datos sucios y desordenados."""
    print("🛠️ Generando archivo CSV con datos sucios de prueba...")
    
    datos_sucios = [
        ["ID", "Cliente", "Ciudad", "Monto"],
        ["101", "  carlos perez ", "MONTERIA", "1500000"],
        ["102", "Ana Gomez", "bogota", "  2000000 "],
        ["101", "  carlos perez ", "MONTERIA", "1500000"], # Duplicado exacto
        ["103", "", "medellin", "800000"],                 # Nombre vacío
        ["104", "Luis Torres", "CARTAGENA", "invalid_val"], # Monto no numérico
        ["105", "Maria Ruiz", "cali", "1200000"]
    ]
    
    with open("datos_brutos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(datos_sucios)
        
    print("✅ Archivo 'datos_brutos.csv' creado con éxito.")

def limpiar_datos():
    if not os.path.exists("datos_brutos.csv"):
        crear_archivo_sucio()
        
    print("\n🧹 Iniciando proceso de limpieza y validación de datos...")
    
    transacciones_limpias = []
    duplicados_eliminados = 0
    registros_invalidos = 0
    
    # Para detectar duplicados únicos
    vistos = set()
    
    with open("datos_brutos.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        encabezados = next(reader)
        transacciones_limpias.append(encabezados)
        
        for fila in reader:
            id_transaccion, cliente, ciudad, monto_str = fila
            
            # 1. Validar campos vacíos esenciales
            if not id_transaccion.strip() or not cliente.strip():
                registros_invalidos += 1
                continue
                
            # 2. Limpiar espacios y estandarizar mayúsculas (Capitalizar nombre, Ciudad en mayúsculas)
            cliente_limpio = cliente.strip().title()
            ciudad_limpia = ciudad.strip().upper()
            
            # 3. Validar y convertir el monto a número
            try:
                monto = float(monto_str.strip())
            except ValueError:
                registros_invalidos += 1
                continue # Descarta filas con montos no numéricos
                
            # 4. Construir tupla para verificar duplicados exactos
            fila_actual = (id_transaccion.strip(), cliente_limpio, ciudad_limpia, str(monto))
            
            if fila_actual in vistos:
                duplicados_eliminados += 1
                continue
                
            vistos.add(fila_actual)
            transacciones_limpias.append([id_transaccion.strip(), cliente_limpio, ciudad_limpia, monto])
            
    # Guardar el resultado limpio en un nuevo archivo
    archivo_salida = "datos_limpios_final.csv"
    with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(transacciones_limpias)
        
    print("\n" + "="*40)
    print("✨ REPORTE DE LIMPIEZA DE DATOS")
    print("="*40)
    print(f"🗑️ Duplicados eliminados:     {duplicados_eliminados}")
    print(f"❌ Registros inválidos o vacíos: {registros_invalidos}")
    print(f"✅ Registros limpios y guardados: {len(transacciones_limpias) - 1}")
    print("="*40)
    print(f"📂 Archivo limpio exportado: {archivo_salida}")

if __name__ == "__main__":
    limpiar_datos()