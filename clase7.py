import pandas as pd
import numpy as np
print (pd.__version__)

# Crear un DataFrame con datos de clientes
clientes = pd.DataFrame({
    'empresa': ['Tech Corp', 'Finance Ltd', 'Retail SA', 'Energy Co', 'Health Inc'],
    'sector': ['Tecnología', 'Finanzas', 'Retail', 'Energía', 'Salud'],
    'facturacion_anual': [250000, 180000, 320000, 290000, 195000],
    'proyectos_activos': [3, 2, 5, 4, 2],
    'años_relacion': [2, 5, 1, 3, 4]
})

# 1. Visualizar el DataFrame
print("Portfolio de Clientes:")
print(clientes)

# 2. Calcular métricas clave
clientes['facturacion_por_proyecto'] = (
    clientes['facturacion_anual'] / clientes['proyectos_activos']
)

# 3. Identificar clientes VIP (facturación > 200k)
clientes['es_vip'] = clientes['facturacion_anual'] > 200000

print("\nAnálisis del Portfolio:")
print(clientes[['empresa', 'facturacion_por_proyecto', 'es_vip']])

clientes['facturacion_por_proyecto'] = clientes['facturacion_anual'] / clientes['proyectos_activos']
clientes['es_vip'] = clientes['facturacion_anual'] > 200000

print("Clientes:")

# Dataset de proyectos
proyectos = pd.DataFrame({
    'codigo': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'cliente': ['Tech Corp', 'Finance Ltd', 'Retail SA', 'Tech Corp', 'Energy Co'],
    'consultor_lead': ['C001', 'C003', 'C002', 'C004', 'C005'],
    'presupuesto': [75000, 120000, 45000, 95000, 150000],
    'estado': ['Activo', 'Completado', 'Activo', 'Activo', 'Planificado']
})

# 1. Proyectos activos
activos = proyectos[proyectos['estado'] == 'Activo']
print("Proyectos activos:")
print(activos)

# 2. Proyectos de alto valor (>80k) de Tech Corp
tech_alto_valor = proyectos[
    (proyectos['cliente'] == 'Tech Corp') & 
    (proyectos['presupuesto'] > 80000)
]
print("\nProyectos Tech Corp > 80k:")
print(tech_alto_valor)

# 3. Información del consultor lead para proyectos activos
info_leads = proyectos.loc[
    proyectos['estado'] == 'Activo',
    ['codigo', 'consultor_lead', 'presupuesto']
]
print("\nConsultores lead de proyectos activos:")
print(info_leads)


# Preparar datos de ejemplo
import pandas as pd
import os

# Crear directorio si no existe
os.makedirs('datos', exist_ok=True)
            
# Crear archivo CSV de ventas
ventas_csv = """fecha,cliente,producto,cantidad,precio_unitario,total
2024-01-15,Empresa A,Consultoría,40,150,6000
2024-01-16,Empresa B,Análisis,20,200,4000
2024-01-17,Empresa C,Desarrollo,60,180,10800
2024-01-18,Empresa A,Consultoría,30,150,4500
2024-01-19,Empresa D,Análisis,25,200,5000"""

with open('datos/ventas.csv', 'w', encoding='utf-8') as f:
    f.write(ventas_csv)

    df_ventas = pd.read_csv('datos/ventas.csv')
   # Leer el archivo
df_ventas = pd.read_csv('datos/ventas.csv')
print("Datos de ventas:")
print(df_ventas)
